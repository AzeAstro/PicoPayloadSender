from PyQt6 import QtWidgets
from PyQt6.QtWidgets import QMessageBox
import socket
from PyQt6.QtGui import QIcon
import traceback
from Keycode import Keycode
from struct import pack

from ui.PayloadSenderUI_ui import Ui_PayloadSender

duckyCommands = {
    'WINDOWS': Keycode.WINDOWS,'WIN': Keycode.WINDOWS, 'GUI': Keycode.GUI,
    'APP': Keycode.APPLICATION, 'MENU': Keycode.APPLICATION, 'SHIFT': Keycode.SHIFT,
    'ALT': Keycode.ALT, 'CONTROL': Keycode.CONTROL, 'CTRL': Keycode.CONTROL,
    'DOWNARROW': Keycode.DOWN_ARROW, 'DOWN': Keycode.DOWN_ARROW, 'LEFTARROW': Keycode.LEFT_ARROW,
    'LEFT': Keycode.LEFT_ARROW, 'RIGHTARROW': Keycode.RIGHT_ARROW, 'RIGHT': Keycode.RIGHT_ARROW,
    'UPARROW': Keycode.UP_ARROW, 'UP': Keycode.UP_ARROW, 'BREAK': Keycode.PAUSE,
    'PAUSE': Keycode.PAUSE, 'CAPSLOCK': Keycode.CAPS_LOCK, 'DELETE': Keycode.DELETE,
    'END': Keycode.END, 'ESC': Keycode.ESCAPE, 'ESCAPE': Keycode.ESCAPE, 'HOME': Keycode.HOME,
    'INSERT': Keycode.INSERT, 'NUMLOCK': Keycode.KEYPAD_NUMLOCK, 'PAGEUP': Keycode.PAGE_UP,
    'PAGEDOWN': Keycode.PAGE_DOWN, 'PRINTSCREEN': Keycode.PRINT_SCREEN, 'ENTER': Keycode.ENTER,
    'SCROLLLOCK': Keycode.SCROLL_LOCK, 'SPACE': Keycode.SPACE, 'TAB': Keycode.TAB,
    'A': Keycode.A, 'B': Keycode.B, 'C': Keycode.C, 'D': Keycode.D, 'E': Keycode.E,
    'F': Keycode.F, 'G': Keycode.G, 'H': Keycode.H, 'I': Keycode.I, 'J': Keycode.J,
    'K': Keycode.K, 'L': Keycode.L, 'M': Keycode.M, 'N': Keycode.N, 'O': Keycode.O,
    'P': Keycode.P, 'Q': Keycode.Q, 'R': Keycode.R, 'S': Keycode.S, 'T': Keycode.T,
    'U': Keycode.U, 'V': Keycode.V, 'W': Keycode.W, 'X': Keycode.X, 'Y': Keycode.Y,
    'Z': Keycode.Z, 'F1': Keycode.F1, 'F2': Keycode.F2, 'F3': Keycode.F3,
    'F4': Keycode.F4, 'F5': Keycode.F5, 'F6': Keycode.F6, 'F7': Keycode.F7,
    'F8': Keycode.F8, 'F9': Keycode.F9, 'F10': Keycode.F10, 'F11': Keycode.F11,
    'F12': Keycode.F12,
}


class MainWindow(QtWidgets.QMainWindow, Ui_PayloadSender):
    def __init__(self) -> None:
        super(MainWindow, self).__init__(None)
        self.setupUi(self)
        self.socket=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        self.socket.settimeout(3)
        self.connectionButton.clicked.connect(self.selectConnectionAction)
        self.sendPayloadButton.clicked.connect(self.sendPayload)
        self.stopPicoButton.clicked.connect(self.stopPico)
        self.payloadParts(False)
        self.connected=False
        self.setWindowIcon(QIcon('ui/icon.png'))

    def payloadParts(self,value:bool):
        value=not value
        self.sendPayloadButton.setDisabled(value)
        self.payloadTextEdit.setDisabled(value)
        self.stopPicoButton.setDisabled(value)
        if value:
            self.payloadTextEdit.setPlaceholderText("Connect to Pico first.")
        else:
            self.payloadTextEdit.setPlaceholderText("Enter duckyscript to send.")


    def generatePayloadPack(self,payload:str):
        return pack("l",len(payload)), payload.encode()


    def sendText(self,text:str):
        length,payload=self.generatePayloadPack(text)
        try:
            self.socket.send(length)
            self.socket.send(payload)
            return True
        except:
            return False
        

    def selectConnectionAction(self):
        if self.connected:
            self.disconnectFromPico()
            self.connectionButton.setText("Connect")
        elif self.connected==False:
            self.connectToPico()



    def connectToPico(self):
        self.socket=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        self.socket.settimeout(5)
        self.connectionStatusLabel.setText("Connection status: trying...")
        addr=self.connectionAddressLineEdit.text()
        try:
            ip,port=addr.split(":")
            port=int(port)
            self.socket.connect((ip,port))
            self.connectionStatusLabel.setText("Connection status: Connected")
            self.payloadParts(True)
            self.connectionButton.setText("Disconnect")
            self.connected=True
        except Exception:
            print(traceback.format_exc())
            self.connectionStatusLabel.setText("Connection status: Failed")

    def sendPayload(self):
        payloadText=self.payloadTextEdit.toPlainText()
        if self.checkPayload(payloadText):
            self.sendText(payloadText)
            self.payloadStatusLabel.setText("Payload status: Sent")
        else:
            dlg = QMessageBox(self)
            dlg.setWindowTitle("Payload error")
            dlg.setText("Syntax error.\nCheck the payload again.")
            dlg.setStandardButtons(QMessageBox.StandardButton.Ok)
            dlg.setWindowIcon(QIcon('ui/icon.png'))
            dlg.setIcon(QMessageBox.Icon.Critical)
            dlg.exec()


    def disconnectFromPico(self):
        self.sendText("!disconnect")
        self.socket.close()
        self.payloadStatusLabel.setText("Payload status: None")
        self.connectionStatusLabel.setText("Connection status: Disconnected")
        self.connected=False
        self.payloadParts(False)

    def stopPico(self):
        self.sendText("!stop")
        self.connectionStatusLabel.setText("Connection status: Disconnected")
        self.payloadStatusLabel.setText("Payload status: None")
        self.connectionButton.setText("Connect")
        self.payloadParts(False)
        self.connected=False
        self.socket.close()

    





    def checkLine(self,line):
        for key in filter(None, line.split(" ")):
            key = key.upper()
            command_keycode = duckyCommands.get(key, None)
            if command_keycode is not None:
                pass
            elif hasattr(Keycode, key):
                pass
            else:
                return False
        return True

    def checkPayload(self,payload:str):
        payloadLines=payload.splitlines()
        for line in payloadLines:
            if(line[0:3] == "REM"):
                pass
            elif(line[0:6]=="REPEAT"):
                try:
                    int(line[6:])
                except:
                    return False
            elif(line[0:5] == "DELAY"):
                try:
                    float(line[6:])/1000
                except:
                    return False
            elif(line[0:6] == "STRING"):
                pass
            elif(line[0:13] == "DEFAULT_DELAY"):
                try:
                    int(line[14:]) * 10
                except:
                    return False
            elif(line[0:12] == "DEFAULTDELAY"):
                try:
                    int(line[13:]) * 10
                except:
                    return False
            else:
                if self.checkLine(line)!=True:
                    return False
        return True





app = QtWidgets.QApplication([])

window = MainWindow()
window.show()
app.exec()