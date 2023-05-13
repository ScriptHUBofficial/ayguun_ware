import os
import socket
import threading
from termcolor import colored

def find_subdomains(target):
    os.system('cls' if os.name == 'nt' else 'clear')

    with open("wordlist.txt") as f:
        wordlist = f.read().splitlines()

    found_subdomains = []

    class SubdomainThread(threading.Thread):
        def __init__(self, subdomain):
            threading.Thread.__init__(self)
            self.subdomain = subdomain

        def run(self):
            try:
                s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                s.settimeout(1)
                s.connect((self.subdomain + "." + target, 80))
                print(colored("[+] " + self.subdomain + "." + target + " bulundu!", 'blue'))
                found_subdomains.append(self.subdomain)
                s.close()

            except socket.error:
                print(colored("[-] " + self.subdomain + "." + target + " bulunamadı!", 'red'))


    threads = []
    for subdomain in wordlist:
        t = SubdomainThread(subdomain)
        threads.append(t)
        t.start()


    for t in threads:
        t.join()

    if found_subdomains:
        with open("gulum.txt", "w") as f:
            for subdomain in found_subdomains:
                f.write(subdomain + "." + target + "\n")

        print(colored("[+]", 'green'))
    else:
        print(colored("[-]", 'red'))
