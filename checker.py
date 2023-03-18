from colorama import Fore, Style
import requests
from tkinter import filedialog
from tkinter import *

def check_usernames(server, usernames):
    for username in usernames:
        url = f'{servers[server]}/api/public/users?name={username}'
        response = requests.get(url)
        if response.status_code == 404:
            print(Fore.LIGHTGREEN_EX + f"[-] {username} is not taken")
            with open("usernames.txt", "a", encoding="ISO-8859-9") as file:  #You might like to change encoding to UTF-8
                file.write(f"[-] {username} is not taken\n")
        elif response.status_code == 200:
            print(Fore.LIGHTRED_EX + f"[+] {username} is taken")
            with open("usernames.txt", "a", encoding="ISO-8859-9") as file:  #You might like to change encoding to UTF-8
                file.write(f"[+] {username} is taken\n")
        else:
            print(Fore.LIGHTRED_EX + f"An error occurred with status code {response.status_code}")

print(Fore.LIGHTCYAN_EX + """
 ██░ ██  ▄████▄   ██░ ██ ▓█████  ▄████▄   ██ ▄█▀
▓██░ ██▒▒██▀ ▀█  ▓██░ ██▒▓█   ▀ ▒██▀ ▀█   ██▄█▒ 
▒██▀▀██░▒▓█    ▄ ▒██▀▀██░▒███   ▒▓█    ▄ ▓███▄░ 
░▓█ ░██ ▒▓▓▄ ▄██▒░▓█ ░██ ▒▓█  ▄ ▒▓▓▄ ▄██▒▓██ █▄ 
░▓█▒░██▓▒ ▓███▀ ░░▓█▒░██▓░▒████▒▒ ▓███▀ ░▒██▒ █▄
 ▒ ░░▒░▒░ ░▒ ▒  ░ ▒ ░░▒░▒░░ ▒░ ░░ ░▒ ▒  ░▒ ▒▒ ▓▒
 ▒ ░▒░ ░  ░  ▒    ▒ ░▒░ ░ ░ ░  ░  ░  ▒   ░ ░▒ ▒░
 ░  ░░ ░░         ░  ░░ ░   ░   ░        ░ ░░ ░ 
 ░  ░  ░░ ░       ░  ░  ░   ░  ░░ ░      ░  ░   
        ░                       ░               

Servers: 9                 by @iamyarkin
    """)

servers = {'COM': 'https://www.habbo.com', 'TR': 'https://www.habbo.com.tr', 'DE': 'https://www.habbo.de', 'FR': 'https://www.habbo.fr', 'FI': 'https://www.habbo.fi', 'IT': 'https://www.habbo.it', 'NL': 'https://www.habbo.nl', 'ES': 'https://www.habbo.es', 'BR': 'https://www.habbo.com.br'}

while True:
    server = input(Fore.LIGHTCYAN_EX + "Enter the server to check (COM, TR, DE, FR, FI, IT, NL, ES, BR): ")
    if server.strip() == "":
        print("You must select a server to check.")
        continue
    if server not in servers:
        print("Invalid server code. Please use one of the provided codes.")
        continue
    root = Tk()
    root.withdraw()
    file_path = filedialog.askopenfilename()
    with open(file_path, 'r') as f:
        usernames = f.read().splitlines()
    check_usernames(server, usernames)

    user_input = input(Fore.LIGHTRED_EX + "Enter 'exit' to exit or 'return' to check another file: ")
    if user_input.lower() == "exit":
        exit()
    elif user_input.lower() == "return":
        print("")
