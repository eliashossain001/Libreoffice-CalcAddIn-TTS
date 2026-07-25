# -*- coding: utf-8 -*-
#!/usr/bin/env python

# =============================================================================
#
# Dialog implementation generated from a XDL file.
#
# Created: Sun Jul 16 16:09:45 2023
#      by: unodit 0.8.0
#
# WARNING! All changes made in this file will be overwritten
#          if the file is generated again!
#
# =============================================================================

import uno
import unohelper
from com.sun.star.awt import XActionListener
from com.sun.star.task import XJobExecutor


class tts_calc_UI(unohelper.Base, XActionListener, XJobExecutor):
    """
    Class documentation...AAAAAAAAAAAAAAAAAAAAAAA
    """
    def __init__(self, ctx=uno.getComponentContext()):
        self.LocalContext = ctx
        self.ServiceManager = self.LocalContext.ServiceManager
        self.Toolkit = self.ServiceManager.createInstanceWithContext("com.sun.star.awt.ExtToolkit", self.LocalContext)

        # -----------------------------------------------------------
        #               Create dialog and insert controls
        # -----------------------------------------------------------

        # --------------create dialog container and set model and properties
        self.DialogContainer = self.ServiceManager.createInstanceWithContext("com.sun.star.awt.UnoControlDialog", self.LocalContext)
        self.DialogModel = self.ServiceManager.createInstance("com.sun.star.awt.UnoControlDialogModel")
        self.DialogContainer.setModel(self.DialogModel)

        self.DialogModel.Name = "Dialog1"
        self.DialogModel.PositionX = "203"
        self.DialogModel.PositionY = "24"
        self.DialogModel.Width = 276
        self.DialogModel.Height = 383
        self.DialogModel.Closeable = True
        self.DialogModel.Moveable = True
        self.DialogModel.Title = "পুরুষ"

        
        # --------- create an instance of Button control, set properties ---
        self.convertToText = self.DialogModel.createInstance("com.sun.star.awt.UnoControlButtonModel")

        self.convertToText.Name = "convertToText"
        self.convertToText.TabIndex = 0
        self.convertToText.PositionX = "37"
        self.convertToText.PositionY = "70"
        self.convertToText.Width = 95
        self.convertToText.Height = 30
        self.convertToText.Label = "TEXT"

        # inserts the control model into the dialog model
        self.DialogModel.insertByName("convertToText", self.convertToText)

        # add the action listener
        self.DialogContainer.getControl('convertToText').addActionListener(self)
        self.DialogContainer.getControl('convertToText').setActionCommand('convertToText_OnClick')

        # --------- create an instance of Button control, set properties ---
        self.convertToSSML = self.DialogModel.createInstance("com.sun.star.awt.UnoControlButtonModel")

        self.convertToSSML.Name = "convertToSSML"
        self.convertToSSML.TabIndex = 1
        self.convertToSSML.PositionX = "131"
        self.convertToSSML.PositionY = "70"
        self.convertToSSML.Width = 95
        self.convertToSSML.Height = 30
        self.convertToSSML.Label = "SSML"

        # inserts the control model into the dialog model
        self.DialogModel.insertByName("convertToSSML", self.convertToSSML)

        # add the action listener
        self.DialogContainer.getControl('convertToSSML').addActionListener(self)
        self.DialogContainer.getControl('convertToSSML').setActionCommand('convertToSSML_OnClick')

        # --------- create an instance of Button control, set properties ---
        self.convertToANSI = self.DialogModel.createInstance("com.sun.star.awt.UnoControlButtonModel")

        self.convertToANSI.Name = "convertToANSI"
        self.convertToANSI.TabIndex = 2
        self.convertToANSI.PositionX = "37"
        self.convertToANSI.PositionY = "113"
        self.convertToANSI.Width = 95
        self.convertToANSI.Height = 30
        self.convertToANSI.Label = "ANSI"

        # inserts the control model into the dialog model
        self.DialogModel.insertByName("convertToANSI", self.convertToANSI)

        # add the action listener
        self.DialogContainer.getControl('convertToANSI').addActionListener(self)
        self.DialogContainer.getControl('convertToANSI').setActionCommand('convertToANSI_OnClick')

        # --------- create an instance of Button control, set properties ---
        self.convertToUnicode = self.DialogModel.createInstance("com.sun.star.awt.UnoControlButtonModel")

        self.convertToUnicode.Name = "convertToUnicode"
        self.convertToUnicode.TabIndex = 3
        self.convertToUnicode.PositionX = "131"
        self.convertToUnicode.PositionY = "113"
        self.convertToUnicode.Width = 95
        self.convertToUnicode.Height = 30
        self.convertToUnicode.Label = "UNICODE"

        # inserts the control model into the dialog model
        self.DialogModel.insertByName("convertToUnicode", self.convertToUnicode)

        # add the action listener
        self.DialogContainer.getControl('convertToUnicode').addActionListener(self)
        self.DialogContainer.getControl('convertToUnicode').setActionCommand('convertToUnicode_OnClick')

        # --------- create an instance of Button control, set properties ---
        self.playAudio = self.DialogModel.createInstance("com.sun.star.awt.UnoControlButtonModel")

        self.playAudio.Name = "playAudio"
        self.playAudio.TabIndex = 7
        self.playAudio.PositionX = "53"
        self.playAudio.PositionY = "304"
        self.playAudio.Width = 86
        self.playAudio.Height = 30
        self.playAudio.Label = "PLAY"

        # inserts the control model into the dialog model
        self.DialogModel.insertByName("playAudio", self.playAudio)

        # add the action listener
        self.DialogContainer.getControl('playAudio').addActionListener(self)
        self.DialogContainer.getControl('playAudio').setActionCommand('playAudio_OnClick')

        # --------- create an instance of Button control, set properties ---
        self.clearText = self.DialogModel.createInstance("com.sun.star.awt.UnoControlButtonModel")

        self.clearText.Name = "clearText"
        self.clearText.TabIndex = 9
        self.clearText.PositionX = "143"
        self.clearText.PositionY = "304"
        self.clearText.Width = 86
        self.clearText.Height = 30
        self.clearText.Label = "CLEAR"

        # inserts the control model into the dialog model
        self.DialogModel.insertByName("clearText", self.clearText)

        # add the action listener
        self.DialogContainer.getControl('clearText').addActionListener(self)
        self.DialogContainer.getControl('clearText').setActionCommand('clearText_OnClick')

        # --------- create an instance of Button control, set properties ---
        self.closeWindowButton = self.DialogModel.createInstance("com.sun.star.awt.UnoControlButtonModel")

        self.closeWindowButton.Name = "closeWindowButton"
        self.closeWindowButton.TabIndex = 15
        self.closeWindowButton.PositionX = "237"
        self.closeWindowButton.PositionY = "12"
        self.closeWindowButton.Width = 36
        self.closeWindowButton.Height = 44
        self.closeWindowButton.Label = "CLOSE"

        # inserts the control model into the dialog model
        self.DialogModel.insertByName("closeWindowButton", self.closeWindowButton)

        # add the action listener
        self.DialogContainer.getControl('closeWindowButton').addActionListener(self)
        self.DialogContainer.getControl('closeWindowButton').setActionCommand('closeWindowButton_OnClick')

        # --------- create an instance of RadioButton control, set properties ---
        self.selectMale = self.DialogModel.createInstance("com.sun.star.awt.UnoControlRadioButtonModel")

        self.selectMale.Name = "selectMale"
        self.selectMale.TabIndex = 4
        self.selectMale.PositionX = "88"
        self.selectMale.PositionY = "159"
        self.selectMale.Width = 36
        self.selectMale.Height = 20
        self.selectMale.Label = "পুরুষ"

        # inserts the control model into the dialog model
        self.DialogModel.insertByName("selectMale", self.selectMale)

        self.DialogContainer.getControl('selectMale').addActionListener(self)
        self.DialogContainer.getControl('selectMale').setActionCommand('selectMale_onClick')

        # --------- create an instance of RadioButton control, set properties ---
        self.selectFemale = self.DialogModel.createInstance("com.sun.star.awt.UnoControlRadioButtonModel")

        self.selectFemale.Name = "selectFemale"
        self.selectFemale.TabIndex = 10
        self.selectFemale.PositionX = "141"
        self.selectFemale.PositionY = "159"
        self.selectFemale.Width = 36
        self.selectFemale.Height = 20
        self.selectFemale.Label = "নারী"

        # inserts the control model into the dialog model
        self.DialogModel.insertByName("selectFemale", self.selectFemale)
        self.DialogContainer.getControl('selectFemale').addActionListener(self)
        self.DialogContainer.getControl('selectFemale').setActionCommand('selectFemale_onClick')

        # --------- create an instance of RadioButton control, set properties ---
        self.selectMature = self.DialogModel.createInstance("com.sun.star.awt.UnoControlRadioButtonModel")

        self.selectMature.Name = "selectMature"
        self.selectMature.TabIndex = 11
        self.selectMature.PositionX = "88"
        self.selectMature.PositionY = "179"
        self.selectMature.Width = 50
        self.selectMature.Height = 20
        self.selectMature.Label = "প্রাপ্তবয়স্ক"

        # inserts the control model into the dialog model
        self.DialogModel.insertByName("selectMature", self.selectMature)

        self.DialogContainer.getControl('selectMature').addActionListener(self)
        self.DialogContainer.getControl('selectMature').setActionCommand('selectMature_onClick')

        # --------- create an instance of RadioButton control, set properties ---
        self.selectImmature = self.DialogModel.createInstance("com.sun.star.awt.UnoControlRadioButtonModel")

        self.selectImmature.Name = "selectImmature"
        self.selectImmature.TabIndex = 12
        self.selectImmature.PositionX = "141"
        self.selectImmature.PositionY = "179"
        self.selectImmature.Width = 50
        self.selectImmature.Height = 20
        self.selectImmature.Label = "অপ্রাপ্তবয়স্ক"

        # inserts the control model into the dialog model
        self.DialogModel.insertByName("selectImmature", self.selectImmature)

        self.DialogContainer.getControl('selectImmature').addActionListener(self)
        self.DialogContainer.getControl('selectImmature').setActionCommand('selectImmature_OnClick')

        # --------- create an instance of FixedText control, set properties ---
        self.Label1 = self.DialogModel.createInstance("com.sun.star.awt.UnoControlFixedTextModel")

        self.Label1.Name = "Label1"
        self.Label1.TabIndex = 5
        self.Label1.PositionX = "70"
        self.Label1.PositionY = "231"
        self.Label1.Width = 21
        self.Label1.Height = 20
        self.Label1.Label = "গতি"

        # inserts the control model into the dialog model
        self.DialogModel.insertByName("Label1", self.Label1)

        # --------- create an instance of FixedText control, set properties ---
        self.Label2 = self.DialogModel.createInstance("com.sun.star.awt.UnoControlFixedTextModel")

        self.Label2.Name = "Label2"
        self.Label2.TabIndex = 6
        self.Label2.PositionX = "72"
        self.Label2.PositionY = "271"
        self.Label2.Width = 21
        self.Label2.Height = 20
        self.Label2.Label = "পিচ"

        # inserts the control model into the dialog model
        self.DialogModel.insertByName("Label2", self.Label2)

        # --------- create an instance of ImageControl control, set properties ---
        self.taskpaneLogo = self.DialogModel.createInstance("com.sun.star.awt.UnoControlImageControlModel")

        self.taskpaneLogo.Name = "taskpaneLogo"
        self.taskpaneLogo.TabIndex = 8
        self.taskpaneLogo.PositionX = "37"
        self.taskpaneLogo.PositionY = "10"
        self.taskpaneLogo.Width = 189
        self.taskpaneLogo.Height = 49

        # inserts the control model into the dialog model
        self.DialogModel.insertByName("taskpaneLogo", self.taskpaneLogo)

        # --------- create an instance of ListBox control, set properties ---
        self.adjustSpeed = self.DialogModel.createInstance("com.sun.star.awt.UnoControlListBoxModel")

        self.adjustSpeed.Name = "adjustSpeed"
        self.adjustSpeed.TabIndex = 13
        self.adjustSpeed.PositionX = "97"
        self.adjustSpeed.PositionY = "231"
        self.adjustSpeed.Width = 56
        self.adjustSpeed.Height = 18
        self.adjustSpeed.Dropdown= True
        self.adjustSpeed.Align= 1
        self.adjustSpeed.StringItemList=('-2X', '-1X', '0', '1X', '2X', '-2X', '-1X', '0', '1X', '2X')
        self.adjustSpeed.SelectedItems= ['2']

        # inserts the control model into the dialog model
        self.DialogModel.insertByName("adjustSpeed", self.adjustSpeed)

        # --------- create an instance of ListBox control, set properties ---
        self.adjustPitch = self.DialogModel.createInstance("com.sun.star.awt.UnoControlListBoxModel")

        self.adjustPitch.Name = "adjustPitch"
        self.adjustPitch.TabIndex = 14
        self.adjustPitch.PositionX = "98"
        self.adjustPitch.PositionY = "271"
        self.adjustPitch.Width = 56
        self.adjustPitch.Height = 18
        self.adjustPitch.Dropdown= True
        self.adjustPitch.Align=1
        self.adjustPitch.StringItemList=('-2X', '-1X', '0', '1X', '2X', '-2X', '-1X', '0', '1X', '2X')
        self.adjustPitch.SelectedItems= ['2']

        # inserts the control model into the dialog model
        self.DialogModel.insertByName("adjustPitch", self.adjustPitch)


    # -----------------------------------------------------------
    #               Action events
    # -----------------------------------------------------------

    def actionPerformed(self, oActionEvent):
        
        if oActionEvent.ActionCommand == 'convertToText_OnClick':
            self.convertToText_OnClick()

        if oActionEvent.ActionCommand == 'convertToSSML_OnClick':
            self.convertToSSML_OnClick()

        if oActionEvent.ActionCommand == 'convertToANSI_OnClick':
            self.convertToANSI_OnClick()

        if oActionEvent.ActionCommand == 'convertToUnicode_OnClick':
            self.convertToUnicode_OnClick()

        if oActionEvent.ActionCommand == 'playAudio_OnClick':
            self.playAudio_OnClick()

        if oActionEvent.ActionCommand == 'clearText_OnClick':
            self.clearText_OnClick()
        
        if oActionEvent.ActionCommand == 'selectMale_onClick':
            self.selectMale_onClick(oActionEvent)

        if oActionEvent.ActionCommand == 'selectFemale_onClick':
            self.selectFemale_onClick(oActionEvent)

        if oActionEvent.ActionCommand == 'selectMature_onClick':
            self.selectMature_onClick(oActionEvent)
    
        if oActionEvent.ActionCommand == 'selectImmature_OnClick':
            self.selectImmature_OnClick(oActionEvent)
        
        if oActionEvent.ActionCommand == 'closeWindowButton_OnClick':
            self.closeWindowButton_OnClick()


# ----------------- END GENERATED CODE ----------------------------------------