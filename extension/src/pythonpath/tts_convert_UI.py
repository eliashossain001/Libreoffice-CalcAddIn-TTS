# -*- coding: utf-8 -*-
#!/usr/bin/env python

# =============================================================================
#
# Dialog implementation generated from a XDL file.
#

import uno
import unohelper
from com.sun.star.awt import XActionListener
from com.sun.star.task import XJobExecutor


class tts_convert_UI(unohelper.Base, XActionListener, XJobExecutor):
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
        self.DialogModel.PositionX = "192"
        self.DialogModel.PositionY = "18"
        self.DialogModel.Width = 284
        self.DialogModel.Height = 341
        self.DialogModel.Closeable = True
        self.DialogModel.Moveable = True

        
        # --------- create an instance of ProgressBar control, set properties ---
        self.ProgressBar1 = self.DialogModel.createInstance("com.sun.star.awt.UnoControlProgressBarModel")

        self.ProgressBar1.Name = "ProgressBar1"
        self.ProgressBar1.TabIndex = 0
        self.ProgressBar1.PositionX = "77"
        self.ProgressBar1.PositionY = "127"
        self.ProgressBar1.Width = 62
        self.ProgressBar1.Height = 26
        self.ProgressBar1.ProgressValue = -10

        # inserts the control model into the dialog model
        self.DialogModel.insertByName("ProgressBar1", self.ProgressBar1)

        # --------- create an instance of Button control, set properties ---
        self.CommandButton3 = self.DialogModel.createInstance("com.sun.star.awt.UnoControlButtonModel")

        self.CommandButton3.Name = "CommandButton3"
        self.CommandButton3.TabIndex = 1
        self.CommandButton3.PositionX = "137"
        self.CommandButton3.PositionY = "124"
        self.CommandButton3.Width = 71
        self.CommandButton3.Height = 24
        self.CommandButton3.Label = "UNICODE"

        # inserts the control model into the dialog model
        self.DialogModel.insertByName("CommandButton3", self.CommandButton3)

        # add the action listener
        self.DialogContainer.getControl('CommandButton3').addActionListener(self)
        self.DialogContainer.getControl('CommandButton3').setActionCommand('CommandButton3_OnClick')

        # --------- create an instance of Button control, set properties ---
        self.CommandButton4 = self.DialogModel.createInstance("com.sun.star.awt.UnoControlButtonModel")

        self.CommandButton4.Name = "CommandButton4"
        self.CommandButton4.TabIndex = 2
        self.CommandButton4.PositionX = "80"
        self.CommandButton4.PositionY = "175"
        self.CommandButton4.Width = 58
        self.CommandButton4.Height = 24
        self.CommandButton4.Label = "PLAY"

        # inserts the control model into the dialog model
        self.DialogModel.insertByName("CommandButton4", self.CommandButton4)

        # add the action listener
        self.DialogContainer.getControl('CommandButton4').addActionListener(self)
        self.DialogContainer.getControl('CommandButton4').setActionCommand('CommandButton4_OnClick')

        # --------- create an instance of Button control, set properties ---
        self.CommandButton1 = self.DialogModel.createInstance("com.sun.star.awt.UnoControlButtonModel")

        self.CommandButton1.Name = "CommandButton1"
        self.CommandButton1.TabIndex = 7
        self.CommandButton1.PositionX = "66"
        self.CommandButton1.PositionY = "124"
        self.CommandButton1.Width = 71
        self.CommandButton1.Height = 24
        self.CommandButton1.Label = "ANSI"

        # inserts the control model into the dialog model
        self.DialogModel.insertByName("CommandButton1", self.CommandButton1)

        # add the action listener
        self.DialogContainer.getControl('CommandButton1').addActionListener(self)
        self.DialogContainer.getControl('CommandButton1').setActionCommand('CommandButton1_OnClick')

        # --------- create an instance of Button control, set properties ---
        self.CommandButton2 = self.DialogModel.createInstance("com.sun.star.awt.UnoControlButtonModel")

        self.CommandButton2.Name = "CommandButton2"
        self.CommandButton2.TabIndex = 8
        self.CommandButton2.PositionX = "68"
        self.CommandButton2.PositionY = "88"
        self.CommandButton2.Width = 71
        self.CommandButton2.Height = 24
        self.CommandButton2.Label = "TEXT"

        # inserts the control model into the dialog model
        self.DialogModel.insertByName("CommandButton2", self.CommandButton2)

        # add the action listener
        self.DialogContainer.getControl('CommandButton2').addActionListener(self)
        self.DialogContainer.getControl('CommandButton2').setActionCommand('CommandButton2_OnClick')

        # --------- create an instance of Button control, set properties ---
        self.CommandButton5 = self.DialogModel.createInstance("com.sun.star.awt.UnoControlButtonModel")

        self.CommandButton5.Name = "CommandButton5"
        self.CommandButton5.TabIndex = 9
        self.CommandButton5.PositionX = "139"
        self.CommandButton5.PositionY = "88"
        self.CommandButton5.Width = 71
        self.CommandButton5.Height = 24
        self.CommandButton5.Label = "SSML"

        # inserts the control model into the dialog model
        self.DialogModel.insertByName("CommandButton5", self.CommandButton5)

        # add the action listener
        self.DialogContainer.getControl('CommandButton5').addActionListener(self)
        self.DialogContainer.getControl('CommandButton5').setActionCommand('CommandButton5_OnClick')

        # --------- create an instance of Button control, set properties ---
        self.CommandButton6 = self.DialogModel.createInstance("com.sun.star.awt.UnoControlButtonModel")

        self.CommandButton6.Name = "CommandButton6"
        self.CommandButton6.TabIndex = 10
        self.CommandButton6.PositionX = "143"
        self.CommandButton6.PositionY = "175"
        self.CommandButton6.Width = 58
        self.CommandButton6.Height = 24
        self.CommandButton6.Label = "CLEAR"

        # inserts the control model into the dialog model
        self.DialogModel.insertByName("CommandButton6", self.CommandButton6)

        # add the action listener
        self.DialogContainer.getControl('CommandButton6').addActionListener(self)
        self.DialogContainer.getControl('CommandButton6').setActionCommand('CommandButton6_OnClick')

        # --------- create an instance of RadioButton control, set properties ---
        self.OptionButton2 = self.DialogModel.createInstance("com.sun.star.awt.UnoControlRadioButtonModel")

        self.OptionButton2.Name = "OptionButton2"
        self.OptionButton2.TabIndex = 3
        self.OptionButton2.PositionX = "130"
        self.OptionButton2.PositionY = "57"
        self.OptionButton2.Width = 45
        self.OptionButton2.Height = 10
        self.OptionButton2.Label = "অপ্রাপ্তবয়স্ক"

        # inserts the control model into the dialog model
        self.DialogModel.insertByName("OptionButton2", self.OptionButton2)

        # --------- create an instance of RadioButton control, set properties ---
        self.OptionButton1 = self.DialogModel.createInstance("com.sun.star.awt.UnoControlRadioButtonModel")

        self.OptionButton1.Name = "OptionButton1"
        self.OptionButton1.TabIndex = 4
        self.OptionButton1.PositionX = "83"
        self.OptionButton1.PositionY = "57"
        self.OptionButton1.Width = 38
        self.OptionButton1.Height = 10
        self.OptionButton1.Label = "প্রাপ্তবয়স্ক"

        # inserts the control model into the dialog model
        self.DialogModel.insertByName("OptionButton1", self.OptionButton1)

        # --------- create an instance of RadioButton control, set properties ---
        self.OptionButton3 = self.DialogModel.createInstance("com.sun.star.awt.UnoControlRadioButtonModel")

        self.OptionButton3.Name = "OptionButton3"
        self.OptionButton3.TabIndex = 5
        self.OptionButton3.PositionX = "85"
        self.OptionButton3.PositionY = "40"
        self.OptionButton3.Width = 36
        self.OptionButton3.Height = 10
        self.OptionButton3.Label = "পুরুষ"

        # inserts the control model into the dialog model
        self.DialogModel.insertByName("OptionButton3", self.OptionButton3)

        # --------- create an instance of RadioButton control, set properties ---
        self.OptionButton4 = self.DialogModel.createInstance("com.sun.star.awt.UnoControlRadioButtonModel")

        self.OptionButton4.Name = "OptionButton4"
        self.OptionButton4.TabIndex = 6
        self.OptionButton4.PositionX = "130"
        self.OptionButton4.PositionY = "40"
        self.OptionButton4.Width = 45
        self.OptionButton4.Height = 10
        self.OptionButton4.Label = "নারী"

        # inserts the control model into the dialog model
        self.DialogModel.insertByName("OptionButton4", self.OptionButton4)

        # --------- create an instance of RadioButton control, set properties ---
        self.OptionButton5 = self.DialogModel.createInstance("com.sun.star.awt.UnoControlRadioButtonModel")

        self.OptionButton5.Name = "OptionButton5"
        self.OptionButton5.TabIndex = 11
        self.OptionButton5.PositionX = "49"
        self.OptionButton5.PositionY = "229"
        self.OptionButton5.Width = 36
        self.OptionButton5.Height = 10
        self.OptionButton5.Label = "-2x"

        # inserts the control model into the dialog model
        self.DialogModel.insertByName("OptionButton5", self.OptionButton5)

        # --------- create an instance of RadioButton control, set properties ---
        self.OptionButton6 = self.DialogModel.createInstance("com.sun.star.awt.UnoControlRadioButtonModel")

        self.OptionButton6.Name = "OptionButton6"
        self.OptionButton6.TabIndex = 12
        self.OptionButton6.PositionX = "94"
        self.OptionButton6.PositionY = "229"
        self.OptionButton6.Width = 36
        self.OptionButton6.Height = 10
        self.OptionButton6.Label = "-1x"

        # inserts the control model into the dialog model
        self.DialogModel.insertByName("OptionButton6", self.OptionButton6)

        # --------- create an instance of RadioButton control, set properties ---
        self.OptionButton7 = self.DialogModel.createInstance("com.sun.star.awt.UnoControlRadioButtonModel")

        self.OptionButton7.Name = "OptionButton7"
        self.OptionButton7.TabIndex = 13
        self.OptionButton7.PositionX = "139"
        self.OptionButton7.PositionY = "229"
        self.OptionButton7.Width = 36
        self.OptionButton7.Height = 10
        self.OptionButton7.Label = "0"

        # inserts the control model into the dialog model
        self.DialogModel.insertByName("OptionButton7", self.OptionButton7)

        # --------- create an instance of RadioButton control, set properties ---
        self.OptionButton8 = self.DialogModel.createInstance("com.sun.star.awt.UnoControlRadioButtonModel")

        self.OptionButton8.Name = "OptionButton8"
        self.OptionButton8.TabIndex = 14
        self.OptionButton8.PositionX = "186"
        self.OptionButton8.PositionY = "229"
        self.OptionButton8.Width = 36
        self.OptionButton8.Height = 10
        self.OptionButton8.Label = "1X"

        # inserts the control model into the dialog model
        self.DialogModel.insertByName("OptionButton8", self.OptionButton8)

        # --------- create an instance of RadioButton control, set properties ---
        self.OptionButton9 = self.DialogModel.createInstance("com.sun.star.awt.UnoControlRadioButtonModel")

        self.OptionButton9.Name = "OptionButton9"
        self.OptionButton9.TabIndex = 15
        self.OptionButton9.PositionX = "227"
        self.OptionButton9.PositionY = "229"
        self.OptionButton9.Width = 36
        self.OptionButton9.Height = 10
        self.OptionButton9.Label = "2X"

        # inserts the control model into the dialog model
        self.DialogModel.insertByName("OptionButton9", self.OptionButton9)

        # --------- create an instance of RadioButton control, set properties ---
        self.OptionButton10 = self.DialogModel.createInstance("com.sun.star.awt.UnoControlRadioButtonModel")

        self.OptionButton10.Name = "OptionButton10"
        self.OptionButton10.TabIndex = 17
        self.OptionButton10.PositionX = "49"
        self.OptionButton10.PositionY = "255"
        self.OptionButton10.Width = 36
        self.OptionButton10.Height = 10
        self.OptionButton10.Label = "-2x"

        # inserts the control model into the dialog model
        self.DialogModel.insertByName("OptionButton10", self.OptionButton10)

        # --------- create an instance of RadioButton control, set properties ---
        self.OptionButton11 = self.DialogModel.createInstance("com.sun.star.awt.UnoControlRadioButtonModel")

        self.OptionButton11.Name = "OptionButton11"
        self.OptionButton11.TabIndex = 18
        self.OptionButton11.PositionX = "94"
        self.OptionButton11.PositionY = "255"
        self.OptionButton11.Width = 36
        self.OptionButton11.Height = 10
        self.OptionButton11.Label = "-1x"

        # inserts the control model into the dialog model
        self.DialogModel.insertByName("OptionButton11", self.OptionButton11)

        # --------- create an instance of RadioButton control, set properties ---
        self.OptionButton12 = self.DialogModel.createInstance("com.sun.star.awt.UnoControlRadioButtonModel")

        self.OptionButton12.Name = "OptionButton12"
        self.OptionButton12.TabIndex = 19
        self.OptionButton12.PositionX = "139"
        self.OptionButton12.PositionY = "255"
        self.OptionButton12.Width = 36
        self.OptionButton12.Height = 10
        self.OptionButton12.Label = "0"

        # inserts the control model into the dialog model
        self.DialogModel.insertByName("OptionButton12", self.OptionButton12)

        # --------- create an instance of RadioButton control, set properties ---
        self.OptionButton13 = self.DialogModel.createInstance("com.sun.star.awt.UnoControlRadioButtonModel")

        self.OptionButton13.Name = "OptionButton13"
        self.OptionButton13.TabIndex = 20
        self.OptionButton13.PositionX = "187"
        self.OptionButton13.PositionY = "255"
        self.OptionButton13.Width = 36
        self.OptionButton13.Height = 10
        self.OptionButton13.Label = "1X"

        # inserts the control model into the dialog model
        self.DialogModel.insertByName("OptionButton13", self.OptionButton13)

        # --------- create an instance of RadioButton control, set properties ---
        self.OptionButton14 = self.DialogModel.createInstance("com.sun.star.awt.UnoControlRadioButtonModel")

        self.OptionButton14.Name = "OptionButton14"
        self.OptionButton14.TabIndex = 21
        self.OptionButton14.PositionX = "228"
        self.OptionButton14.PositionY = "255"
        self.OptionButton14.Width = 36
        self.OptionButton14.Height = 10
        self.OptionButton14.Label = "2X"

        # inserts the control model into the dialog model
        self.DialogModel.insertByName("OptionButton14", self.OptionButton14)

        # --------- create an instance of Edit control, set properties ---
        self.TextField1 = self.DialogModel.createInstance("com.sun.star.awt.UnoControlEditModel")

        self.TextField1.Name = "TextField1"
        self.TextField1.TabIndex = 16
        self.TextField1.PositionX = "8"
        self.TextField1.PositionY = "227"
        self.TextField1.Width = 32
        self.TextField1.Height = 14
        self.TextField1.Text = "গতি"

        # inserts the control model into the dialog model
        self.DialogModel.insertByName("TextField1", self.TextField1)

        # --------- create an instance of Edit control, set properties ---
        self.TextField2 = self.DialogModel.createInstance("com.sun.star.awt.UnoControlEditModel")

        self.TextField2.Name = "TextField2"
        self.TextField2.TabIndex = 22
        self.TextField2.PositionX = "8"
        self.TextField2.PositionY = "253"
        self.TextField2.Width = 32
        self.TextField2.Height = 14
        self.TextField2.Text = "পিচ"

        # inserts the control model into the dialog model
        self.DialogModel.insertByName("TextField2", self.TextField2)

    # -----------------------------------------------------------
    #               Action events
    # -----------------------------------------------------------

    def actionPerformed(self, oActionEvent):
        
        if oActionEvent.ActionCommand == 'CommandButton3_OnClick':
            self.CommandButton3_OnClick()

        if oActionEvent.ActionCommand == 'CommandButton4_OnClick':
            self.CommandButton4_OnClick()

        if oActionEvent.ActionCommand == 'CommandButton1_OnClick':
            self.CommandButton1_OnClick()

        if oActionEvent.ActionCommand == 'CommandButton2_OnClick':
            self.CommandButton2_OnClick()

        if oActionEvent.ActionCommand == 'CommandButton5_OnClick':
            self.CommandButton5_OnClick()

        if oActionEvent.ActionCommand == 'CommandButton6_OnClick':
            self.CommandButton6_OnClick()


# ----------------- END GENERATED CODE ----------------------------------------