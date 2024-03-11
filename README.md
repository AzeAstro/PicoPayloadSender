# PicoPayloadSender
DuckyScript sender for [PicoDuckyExecuter](https://github.com/AzeAstro/PicoDuckyExecuter)


## Installation
1) Install Python 3
2) Install PyQt6 library
  
  
## Usage
1) Run `main.py`

## UI
![image](https://raw.githubusercontent.com/AzeAstro/PicoPayloadSender/main/pictures/DisconnectedUI.png)  
Here, in `Address to connect` section you have to enter the address to connect. (Example: `192.168.1.3:9999`)  
After that you can press to connect button. It will activate `Stop Pico`, `Send payload` buttons and `Payload` section to input the payload.

![image](https://raw.githubusercontent.com/AzeAstro/PicoPayloadSender/main/pictures/ConnectedUI.png)  
As you see, you can type in payload box. If something wrong at script, app will show warning about it before sending the script.  
Use `send payload` button to send the payload typed in payload box.

Here, stop pico sends `!exit` command to pico and pico raises error to stop the whole script.
Disconnect sends `!disconnect` command to pico and pico TCP server still runs in background. You can reconnect it whenever you want.


Simple as this
