from pyfiglet import Figlet
from colorama import init, Fore, Back, Style
import ctypes
import time
import random
import string
import sys
from os import system, name

ctypes.windll.kernel32.SetConsoleTitleW("HIDDENMINER VERSION 1.0 - STATUS: IDLE")

def clear():
  
    # Windows
    if name == 'nt':
        _ = system('cls')
  
    # Mac & Linux
    else:
        _ = system('clear')
clear()
def render(text):
    f = Figlet() 
    print('\n'*1)
    print(f.renderText(text))
render('HIDDENMINER')
print("\n")
print(Fore.WHITE + "Made by Clxpz#5854")
print('\n')
time.sleep(2)
print(Fore.WHITE + "[" + Fore.CYAN + "+" + Fore.WHITE + "]" + Fore.BLUE + " Connected to pool #3")
time.sleep(1)
print(Fore.WHITE + "[" + Fore.CYAN + "+" + Fore.WHITE + "]" + Fore.BLUE + " Loading Proxies...")
time.sleep(1)
print(Fore.WHITE + "[" + Fore.CYAN + "+" + Fore.WHITE + "]" + Fore.BLUE + " Finding your Deposit Wallet...")
time.sleep(0.5)
print('')
print(Fore.WHITE + "[" + Fore.RED + "!" + Fore.WHITE + "]" + Fore.BLUE + " Not Found!")
time.sleep(1)
print('')
input(Fore.WHITE + "[" + Fore.CYAN + "+" + Fore.WHITE + "]" + Fore.BLUE + " Enter your BTC Wallet Adress: ")
time.sleep(1)
print(Fore.WHITE + "[" + Fore.CYAN + "+" + Fore.WHITE + "]" + Fore.BLUE + " Sucesssfull!")
time.sleep(3)
ctypes.windll.kernel32.SetConsoleTitleW("HIDDENMINER VERSION 1.0 - STATUS: MINING")

def get_random_string(length):
    letters = string.ascii_uppercase + string.digits
    result_str = ''.join(random.choice(letters) for i in range(length))
    print(Fore.WHITE + "[" + Fore.BLUE + "+" + Fore.WHITE + "]" + "  Private " + Fore.RED + result_str + Fore.WHITE + "  [" + "BALANCE: " + Fore.YELLOW + "0.00 BTC" + Fore.WHITE + "] " + Fore.WHITE + " [" + Fore.RED + "0€" + Fore.WHITE + "]")

for i in range(50000):
    get_random_string(46)
    time.sleep(0.002)

def get_random_win(length):
    letters = string.ascii_uppercase + string.digits
    result_str = ''.join(random.choice(letters) for i in range(length))
    print(Fore.WHITE + "[" + Fore.GREEN + "+" + Fore.WHITE + "]" + "  Public " + Fore.GREEN + result_str + Fore.WHITE + "  [" + "BALANCE: " + Fore.GREEN + "1 BTC" + Fore.WHITE + "] " + Fore.WHITE + " [" + Fore.GREEN + "$32 084" + Fore.WHITE + "]")

time.sleep(0.3)

get_random_win(46)

time.sleep(0.5)

ctypes.windll.kernel32.SetConsoleTitleW("HIDDENMINER VERSION 1.0 - STATUS: FOUND BTC!")

print("")
print("")
time.sleep(1)
print(Fore.WHITE + "[" + Fore.CYAN + "HiddenMiner" + Fore.WHITE + "]" + Fore.LIGHTGREEN_EX + " SENDING 1 BTC TO YOUR WALLET" + Fore.WHITE + "  [" + "BALANCE: " + Fore.GREEN + "SUCCESS" + Fore.WHITE + "]") 
time.sleep(1)
print("")
print(Fore.MAGENTA + "HIDDENMINER IS NOW CLOSING...")
time.sleep(1)

closing = Fore.CYAN + "HIDDENMINER 2022"
for char in closing:
    sys.stdout.write(char)
    sys.stdout.flush()
    time.sleep(0.07)

time.sleep(1)
print(Fore.RESET)