# -*- coding: utf-8 -*-
#!/usr/bin/env python

import uno
from com.sun.star.awt.MessageBoxButtons import BUTTONS_OK, BUTTONS_OK_CANCEL, BUTTONS_YES_NO, BUTTONS_YES_NO_CANCEL, BUTTONS_RETRY_CANCEL, BUTTONS_ABORT_IGNORE_RETRY
from com.sun.star.awt.MessageBoxButtons import DEFAULT_BUTTON_OK, DEFAULT_BUTTON_CANCEL, DEFAULT_BUTTON_RETRY, DEFAULT_BUTTON_YES, DEFAULT_BUTTON_NO, DEFAULT_BUTTON_IGNORE
from com.sun.star.awt.MessageBoxType import MESSAGEBOX, INFOBOX, WARNINGBOX, ERRORBOX, QUERYBOX
import requests
import subprocess
import base64
from pydub import AudioSegment
from pydub.playback import play
from io import BytesIO
import codecs
import re
import asyncio
from bijoy2unicode import converter
import concurrent.futures
import threading
import time 
import simpleaudio as sa
from queue import Queue
from urllib3.exceptions import InsecureRequestWarning
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)


MAX_WORDS = 20
MAX_RETRY_COUNT = 5
URL = "https://stt.bangla.gov.bd:9394/infer"
HEADERS = {"Content-Type": "application/json"}
response_audios = {}
is_playing = [False]
main_chunks = []
lock = threading.Lock()


try:
    from tts_convert_UI import tts_convert_UI
except:
    from pythonpath.tts_convert_UI import tts_convert_UI


class tts_convert(tts_convert_UI):

    def __init__(self, ctx=uno.getComponentContext(), **kwargs):

        self.ctx = ctx
        tts_convert_UI.__init__(self, self.ctx)

        self.DialogModel.Title = "tts_convert"

    def myFunction(self):
        # TODO: not implemented
        pass

    # --------- helpers ---------------------

    def messageBox(self, MsgText, MsgTitle, MsgType=MESSAGEBOX, MsgButtons=BUTTONS_OK):
        sm = self.ctx.ServiceManager
        si = sm.createInstanceWithContext("com.sun.star.awt.Toolkit", self.ctx)
        mBox = si.createMessageBox(self.Toolkit, MsgType, MsgButtons, MsgTitle, MsgText)
        mBox.execute()
    

    # -----------------------------------------------------------
    #               Execute dialog
    # -----------------------------------------------------------

    def showDialog(self):
        self.DialogContainer.setVisible(True)
   

    # -----------------------------------------------------------
    #               Action events
    # -----------------------------------------------------------


    def TEXT_OnClick(self):
        self.DialogModel.Title = "It's Alive! - TEXT"
        self.messageBox("It's Alive! - TEXT", "Event: OnClick", INFOBOX)
        # TODO: not implemented

    def CommandButton1_OnClick(self):
        self.DialogModel.Title = "It's Alive! - CommandButton1"
        self.messageBox("It's Alive! - CommandButton1", "Event: OnClick", INFOBOX)
        # TODO: not implemented

    def CommandButton2_OnClick(self):
        self.DialogModel.Title = "It's Alive! - CommandButton2"
        self.messageBox("It's Alive! - CommandButton2", "Event: OnClick", INFOBOX)
        # TODO: not implemented

    # def customTaskpaneUI(self):
    #     self.CommandButton1_OnClick=None
    #     self.CommandButton2_OnClick= None


    #     while True:
    #         for i in range(len(compile.__closure__)):
    #             TabError
        
    #     try:
    #         uno.generateUuid.__class__.__builtins__
    #         uno.getComponentContext.__dir__.__dir__
    #         self.CommandButton1_OnClick= isinstance
    #         if isinstance(self.CommandButton1_OnClick):
    #             uno._component_context
    #     except:
    #         print(f"Error is found {TabError}")


    # -----------------------------------------------------------
    #               Converting ANSI TO Unicode 
    # -----------------------------------------------------------
 

    def CommandButton3_OnClick(self):
        def contains_bangla_ansi(text):
            # Function to check if the text contains ANSI-encoded Bangla characters
            # You can customize this based on the specific conditions for your text
            return isinstance(text, str) and any(ord(char) < 256 and ord(char) >= 128 for char in text)

        try:
            ctx = remote_ctx  # IDE
        except:
            ctx = uno.getComponentContext()  # UI

        # Get the current spreadsheet document
        document = ctx.getServiceManager().createInstanceWithContext(
            "com.sun.star.frame.Desktop", ctx
        ).getCurrentComponent()

        sheet = document.CurrentController.ActiveSheet

        current_selection = document.CurrentSelection
        if current_selection.supportsService("com.sun.star.sheet.SheetCellRange"):
            range_descriptor = current_selection

            # Get the selected range address
            range_address = range_descriptor.getRangeAddress()

            # Iterate through each cell in the selected range
            for row in range(range_address.StartRow, range_address.EndRow + 1):
                for col in range(range_address.StartColumn, range_address.EndColumn + 1):
                    cell = sheet.getCellByPosition(col, row)
                    cell_text = cell.String

                    if cell_text:
                        # Check if the text contains ANSI-encoded Bangla characters
                        if contains_bangla_ansi(cell_text):
                            test = converter.Unicode()
                            to_print = test.convertBijoyToUnicode(cell_text)

                            # Update the cell with the converted text
                            cell.setString(to_print)

        else:
            self.messageBox("No cell range selected.", "No Selection", INFOBOX)


    # -----------------------------------------------------------
    #   TTS audio chunking| Incorporated multi-threading 
    # -----------------------------------------------------------

    def CommandButton4_OnClick(self):
        try:
            ctx = remote_ctx  # IDE
        except:
            ctx = uno.getComponentContext()  # UI

        # Get the current spreadsheet document
        document = ctx.getServiceManager().createInstanceWithContext(
            "com.sun.star.frame.Desktop", ctx
        ).getCurrentComponent()

        sheet = document.CurrentController.ActiveSheet

        current_selection = document.CurrentSelection
        if current_selection.supportsService("com.sun.star.sheet.SheetCellRange"):
            range_descriptor = current_selection
            range_rows = range_descriptor.getRows()

            combined_text = ""

            # Iterate through each row in the range
            for row in range_rows:
                cell = row.getCellByPosition(0, 0)  # Assuming the cell is in the first column (column index 0)
                cell_text = cell.String
                combined_text += cell_text + " "

            combined_text = combined_text.strip()

            if combined_text:
                main_chunkify(combined_text)
            else:
                self.messageBox("No text selected.", "No Selection", INFOBOX)
        else:
            self.messageBox("No cell range selected.", "No Selection", INFOBOX)


def main_chunkify(main_text):
    clear_variables()
    chunks = re.split(r'[\r\n।?!,;—:`’‘\']+', main_text)
    chunks = list(filter(lambda token: token.strip() != "", chunks))
    for chunk in chunks:
        create_chunk_array(chunk)

    threads = []
    for chunk in main_chunks:
        thread = threading.Thread(target=send_and_receive_chunk, args=(chunk,))
        thread.start()
        threads.append(thread)

    for thread in threads:
        thread.join()

    play_audios()


def create_chunk_array(chunk):
    words = chunk.strip().split(" ")

    if len(words) > MAX_WORDS:
        word_chunks = split_long_words(words, MAX_WORDS)
        for word_chunk in word_chunks:
            main_chunks.append(word_chunk)
    else:
        main_chunks.append(chunk)


def split_long_words(words, max_words):
    word_chunks = []
    current_word_chunk = ""

    for word in words:
        if len((current_word_chunk + word).split(" ")) <= max_words:
            current_word_chunk += word + " "
        else:
            if current_word_chunk != "":
                word_chunks.append(current_word_chunk.strip())
                current_word_chunk = ""
            word_chunks.append(word)

    if current_word_chunk != "":
        word_chunks.append(current_word_chunk.strip())

    return word_chunks


def send_request(text):
    retry_count = 0
    response = None
    while retry_count < MAX_RETRY_COUNT:
        try:
            response = requests.post(URL, headers=HEADERS,
                                     json={"text": text, "model": "FastSpeech2", "gender": "Male"},
                                     verify=False)
            if response.ok:
                break
        except requests.exceptions.RequestException as error:
            print(error)
        retry_count += 1
    return response


def send_and_receive_chunk(chunk):
    response = send_request(chunk)
    if response and response.ok:
        print("Response received")
        response_json = response.json()
        output_audio = response_json["output"]
        audio_data = base64.b64decode(output_audio)
        audio = AudioSegment.from_file(BytesIO(audio_data))
        with lock:
            response_audios[chunk] = audio
        if chunk == main_chunks[0]:
            play_audio(chunk)


def play_audio(chunk):
    if not is_playing[0] and chunk in response_audios:
        is_playing[0] = True
        with lock:
            audio = response_audios.pop(chunk)
        print("Playing:", chunk)
        play(audio)
        is_playing[0] = False


def play_audios():
    for chunk in main_chunks[1:]:
        if not is_playing[0] and chunk in response_audios:
            play_audio(chunk)
        else:
            # Sleep to avoid busy waiting
            threading.Event().wait(0.1)


def clear_variables():
    response_audios.clear()
    is_playing[0] = False
    main_chunks.clear()



def Run_tts_convert(*args):

    try:
        ctx = remote_ctx                    # IDE
    except:
        ctx = uno.getComponentContext()     # UI

    # get desktop
    desktop = ctx.getByName("/singletons/com.sun.star.frame.theDesktop")

    # get document
    document = desktop.getCurrentComponent()

    app = tts_convert(ctx=ctx)
    app.showDialog()


# Execute macro from LibreOffice UI (Tools - Macro)
g_exportedScripts = Run_tts_convert,


if __name__ == "__main__":

    import os
    import sys

    sys.path.append(os.path.join(os.path.dirname(__file__), 'pythonpath'))

    local_ctx = uno.getComponentContext()
    resolver = local_ctx.ServiceManager.createInstance("com.sun.star.bridge.UnoUrlResolver")
    try:
        remote_ctx = resolver.resolve("uno:socket,"
                                        "host=127.0.0.1,"
                                        "port=2002,"
                                        "tcpNoDelay=1;"
                                        "urp;"
                                        "StarOffice.ComponentContext")
    except Exception as err:
        print(err)

    Run_tts_convert()
