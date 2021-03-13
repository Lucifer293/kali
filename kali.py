import os
import time
print("="*30)
print("Please wait.....")
print("="*30)
time.sleep(0.5)
print("\033[0;32m _       _   _   _____   _   _____   _____   _____   ")
time.sleep(0.5)
print("\033[0;31m| |     | | | | /  ___| | | |  ___| | ____| |  _  \  ")
time.sleep(0.5)
print("\033[0;34m| |     | | | | | |     | | | |__   | |__   | |_| |  ")
time.sleep(0.5)
print("\033[0;36m| |     | | | | | |     | | |  __|  |  __|  |  _  /  ")
time.sleep(0.5)
print("\033[0;37m| |___  | |_| | | |___  | | | |     | |___  | | \ \  ")
time.sleep(0.5)
print("\033[0;31m|_____| \_____/ \_____| |_| |_|     |_____| |_|  \_\ ")
time.sleep(0.5)

Black="\[\033[0;30m\]" # Black
Red="\[\033[0;31m\]" # Red
Green="\[\033[0;32m\]" # Green
Yellow="\[\033[0;33m\]" # Yellow
Blue="\[\033[0;34m\]" # Blue
Purple="\[\033[0;35m\]" # Purple
Cyan="\[\033[0;36m\]" # Cyan
White="\[\033[0;37m\]" # White
# Bold
BBlack="\[\033[1;30m\]" # Black
BRed="\[\033[1;31m\]" # Red
BGreen="\[\033[1;32m\]" # Green
BYellow="\[\033[1;33m\]" # Yellow
BBlue="\[\033[1;34m\]" # Blue
BPurple="\[\033[1;35m\]" # Purple
BCyan="\[\033[1;36m\]" # Cyan
BWhite="\[\033[1;37m\]" # White

print("\033[1;33m="*30)
print("\033[1;31mProgrammer : \033[1;33mLucifer ")
print("="*30)
time.sleep(2)
print("\033[1;31minsta : \033[1;33m@7.7.6.6.1")
print("="*30)
time.sleep(2)
print("\033[1;31mChannel Telegram : \033[1;33mpy910")
print("="*30)
print("\n")

L = input("Install KALI ?      y/n       ")
if L == "y":
	os.system("pkg update")
	os.system("pkg upgrade")
	os.system("termux-setup-storage")
	os.system("wget -O install-nethunter-termux https://offs.ec/2MceZWr")
	os.system("chmod +x install-nethunter-termux")
	os.system("./install-nethunter-termux")


if L == "n":
	os.system("exit")
