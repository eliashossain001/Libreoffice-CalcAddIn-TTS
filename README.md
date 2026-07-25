# Bangla TTS Add-in for LibreOffice Calc

A LibreOffice Calc extension, written in Python on the UNO API, that reads Bangla spreadsheet content aloud. Select a cell range, click Play, and the add-in synthesizes speech through any self-hosted TTS inference service. It also converts legacy Bijoy (ANSI) encoded Bangla text to Unicode in place.

## Features

- **Text-to-speech for cell ranges.** Select cells in Calc and listen to their content as Bangla speech.
- **Low-latency playback through chunking.** Text is split on punctuation and a word-count limit, so the first audio segment starts playing while the rest is still being synthesized.
- **Multi-threaded synthesis pipeline.** Each chunk is requested in its own thread with automatic retries, and playback proceeds sequentially in the original order.
- **Bijoy (ANSI) to Unicode conversion.** Legacy-encoded Bangla cells are detected and converted in place using the `bijoy2unicode` library.
- **Voice options.** Dialog controls for gender (male or female) and voice maturity.
- **Native LibreOffice integration.** A UNO dialog registered under `Tools > Add-Ons`, generated with the UNO Dialog Tools (unodit) workflow.

## Architecture at a Glance

```
Selected cell range
        |
        v
UNO API  (SheetCellRange traversal)
        |
        v
Chunker: split on punctuation, cap at 20 words per chunk
        |
        v
TTS inference server  (POST /infer, one thread per chunk, up to 5 retries)
        |
        v
Base64 WAV -> pydub AudioSegment -> ordered playback
```

## Project Structure

```
.
├── extension/                  # Contents of the .oxt extension package
│   ├── src/
│   │   ├── tts_calc.py         # Main add-in: TTS playback and Unicode conversion
│   │   ├── tts_convert.py      # Converter-focused variant of the add-in
│   │   └── pythonpath/         # Generated dialog UI classes
│   ├── META-INF/manifest.xml   # Package manifest
│   ├── description.xml         # Extension metadata
│   ├── Addons.xcu              # Tools > Add-Ons menu registration
│   ├── description/            # Title and short description shown in Extension Manager
│   └── registration/           # License text
├── dialogs/
│   └── Default.xdl             # Dialog layout (Basic Dialog Editor format)
├── config.ini                  # unodit project configuration
└── requirements.txt            # Python dependencies
```

## Prerequisites

- LibreOffice 6 or later with Python 3 scripting support
- A reachable TTS inference endpoint (see the API contract below)
- Python packages, installed into the Python interpreter that LibreOffice uses:

```bash
pip install -r requirements.txt
```

## TTS Server API Contract

The add-in is server-agnostic. Any endpoint that implements the following contract will work.

Request:

```http
POST /infer HTTP/1.1
Content-Type: application/json

{
  "text":   "<text chunk>",
  "model":  "FastSpeech2",
  "gender": "Male"
}
```

Response:

```json
{
  "output": "<base64-encoded WAV audio>"
}
```

## Configuration

The endpoint is read from the `TTS_API_URL` environment variable, with a fallback to the `URL` constant at the top of [extension/src/tts_calc.py](extension/src/tts_calc.py):

```bash
export TTS_API_URL="https://your-tts-server.example.com/infer"
soffice --calc
```

## Installation

1. Package the `extension/` directory as an `.oxt` file (an `.oxt` is a zip of the extension contents):

   ```bash
   cd extension && zip -r ../bangla-tts-calc.oxt . && cd ..
   ```

   Alternatively, regenerate the package with [unodit](https://github.com/kelsa-pi/unodit) using the settings in `config.ini`.

2. Install it through `Tools > Extension Manager > Add`, or from the command line:

   ```bash
   unopkg add bangla-tts-calc.oxt
   ```

3. Restart LibreOffice Calc. The add-in appears under `Tools > Add-Ons > Bangla TTS`.

## Usage

1. Open a spreadsheet containing Bangla text.
2. Select the cell range you want to hear.
3. Launch the add-in from `Tools > Add-Ons > Bangla TTS`.
4. Choose the voice options and click **Play**.
5. Click **Unicode** to convert Bijoy (ANSI) encoded cells in the selection to Unicode in place.

## How Playback Works

1. Text from the selected range is collected and split into chunks on Bangla and Latin punctuation (danda, question mark, comma, semicolon, colon, and line breaks).
2. Any chunk longer than 20 words is split again at the word level, keeping each request small enough for fast synthesis.
3. Every chunk is posted to the TTS endpoint in its own thread. Failed requests are retried up to five times before the chunk is skipped.
4. Responses arrive as base64-encoded WAV data and are decoded with `pydub`.
5. Playback starts as soon as the first chunk is ready and proceeds strictly in the original text order, so users hear continuous speech while later chunks are still being synthesized.

## Development

To debug outside LibreOffice's embedded Python, start LibreOffice with a UNO socket and run the script from your IDE:

```bash
soffice "--accept=socket,host=127.0.0.1,port=2002,tcpNoDelay=1;urp;StarOffice.ComponentContext" --norestore
python3 extension/src/tts_calc.py
```

The dialog UI classes under `extension/src/pythonpath/` are generated from [dialogs/Default.xdl](dialogs/Default.xdl) with [unodit](https://github.com/kelsa-pi/unodit). Regenerating them overwrites manual changes, so application logic belongs in `tts_calc.py` and `tts_convert.py`, which subclass the generated code.

## Troubleshooting

- **No audio plays.** Confirm the endpoint is reachable and returns the expected JSON shape. Run LibreOffice from a terminal to see the script's console output.
- **Import errors for `requests`, `pydub`, or `bijoy2unicode`.** The packages must be installed into the same Python environment that LibreOffice embeds, not just the system interpreter.
- **The menu entry does not appear.** Verify the extension installed without errors in `Tools > Extension Manager`, then restart LibreOffice completely (including the quickstarter).

## License

The extension scaffolding is based on [UNO Dialog Tools (unodit)](https://github.com/kelsa-pi/unodit), released under the GNU GPL v3.

## 👨‍💼 Author

**Elias Hossain**  
_Machine Learning Researcher | PhD Student | AI x Reasoning Enthusiast_

[![GitHub](https://img.shields.io/badge/GitHub-EliasHossain001-blue?logo=github)](https://github.com/EliasHossain001)
