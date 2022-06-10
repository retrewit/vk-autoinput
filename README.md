# VK AUTOINPUT MESSAGES
## Linux:
Install:
```
apt update && apt upgrade -y
apt install python python3 python3-pip git
git clone https://github.com/retrewit/vk-autoinput.git
cd vk-autoinput
pip3 install -r requirements.txt
```
Launch:
```
cd vk-autoinput
python3 main.py [-t VK_TOKEN] user
```
## Termux:
Install:
```
pkg update -y
pkg install python3 git
git clone https://github.com/retrewit/vk-autoinput.git
cd vk-autoinput
pip3 install -r requirements.txt
```
Launch:
```
cd vk-autoinput
python3 main.py [-t VK_TOKEN] user
```
