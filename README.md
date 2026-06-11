# interactive-display-boards

A Raspberry Pi-based interactive video playback system that triggers VLC to jump to custom timestamps based on PIR sensor input. The Python code uses a setup with physical pin numbers, not GPIO numbers.  

Created for Garden International School to showcase coursework, community events and fundraisers.

## Built with:
### Software
  - Raspberry Pi OS
  - Python (libraries used: **RPi.GPIO**, **python-vlc**)
  - VLC Media Player

### Hardware
  - Digital display
  - Raspberry Pi 2 (3 and 4 are also compatible)
  - HC-SR501 PIR

Wiring is PIR **VCC** → Pin 2, PIR **GND** → Pin 6, PIR **OUT** → Pin 11

## Installation
sudo apt update  
sudo apt upgrade -y  
sudo apt install vlc python3-pip -y  
pip3 install python-vlc RPi.GPIO  
