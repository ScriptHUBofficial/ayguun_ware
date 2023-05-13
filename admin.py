import requests
import threading
from termcolor import colored
import os

def admin_panel_finder(target):
    os.system('cls' if os.name == 'nt' else 'clear')

    with open("adminler.txt") as f:
        wordlist = f.read().splitlines()

    found_admins = []

    class AdminThread(threading.Thread):
        def __init__(self, admin):
            threading.Thread.__init__(self)
            self.admin = admin

        def run(self):
            try:
                url = "https://" + target + "/" + self.admin
                response = requests.get(url, allow_redirects=False)
                if response.status_code == 200:
                    print(colored("[+] " + url + " bulundu!", 'green'))
                    found_admins.append(url)
                else:
                    print(colored("[-] " + url + " bulunamadı!", 'red'))
            except:
                pass

    threads = []
    for admin in wordlist:
        t = AdminThread(admin)
        threads.append(t)
        t.start()

    for t in threads:
        t.join()

    if found_admins:
        with open("adminler_bulunan.txt", "w") as f:
            for admin in found_admins:
                f.write(admin + "\n")

        os.system('cls' if os.name == 'nt' else 'clear')

    else:
        print(colored("\nHiçbir Admin Paneli Bulunamadı!", 'red'))
