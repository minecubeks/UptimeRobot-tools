from colorama import Fore
import ctypes
import json
import os
import requests
this_ver = '1.0.0'

cyan = Fore.CYAN
red = Fore.RED
lightblack = Fore.LIGHTBLACK_EX
freset = Fore.RESET
green = Fore.GREEN
blue = Fore.BLUE
yellow = Fore.YELLOW

def banner():
    print(f"""{Fore.RED}

                           █ █ █▀█ ▀█▀ █ █▀▄▀█ █▀▀ █▀█ █▀█ █▄▄ █▀█ ▀█▀    ▀█▀ █▀█ █▀█ █   █▀
                           █▄█ █▀▀  █  █ █ ▀ █ ██▄ █▀▄ █▄█ █▄█ █▄█  █      █  █▄█ █▄█ █▄▄ ▄█
                           
────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────
""" + Fore.RESET)

def setTitle(_str):
	ctypes.windll.kernel32.SetConsoleTitleW(f"{_str}")

headers = {
		'cache-control': "no-cache",
		'content-type': "application/x-www-form-urlencoded"
	}

with open('config.json') as config_file:
	config = json.load(config_file)
apikey = config['api_key']