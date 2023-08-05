# PicoPayloadSender
DuckyScript sender for [PicoDuckyExecuter](https://github.com/AzeAstro/PicoDuckyExecuter)


## Installation
1) Install Python 3
2) Install PyQt6 library
  
  
## Usage
1) Run `main.py`

## UI
![image](https://github.com/AzeAstro/PicoPayloadSender/assets/46817089/4da29395-64f0-4a8f-be93-5134afea8b3f)  
Here, in `Address to connect` section you have to enter the address to connect. (Example: `192.168.1.3:9999`)  
After that you can press to connect button. It will activate `Stop Pico`, `Send payload` buttons and `Payload` section to input the payload.

![image](https://github.com/AzeAstro/PicoPayloadSender/assets/46817089/7b0d5bc2-30bc-4d72-b1ba-9ada3853ff4e)  
As you see, you can type in payload box. If something wrong at script, app will show warning about it before sending the script.  
Use `send payload` button to send the payload typed in payload box.

Here, stop pico sends `!exit` command to pico and pico raises error to stop the whole script.
Disconnect sends `!disconnect` command to pico and pico TCP server still runs in background. You can reconnect it whenever you want.


Simple as this


## Donations
If you really want to send donation contact me. (No matter how much. Anything that is 1 USD or higher is accepted.)  
Social media accounts:

Instagram: [@atlas_c0](https://www.instagram.com/atlas_c0/)  
Discord: @atlas_c0
