import os
import sys
from termcolor import colored

from subdomain import find_subdomains
from admin import admin_panel_finder

import shutil
os.system('cls' if os.name == 'nt' else 'clear')


from tabulate import tabulate

# İletişim bilgileri tablosu
contact_info = [
    ['Twitter : @example'],
    ['E-posta : example@mail.com'],
    ['Telefon : +90 (555) 555 55 55'],
    ['Adres   : Örnek Mahallesi, Örnek Sokak No:1, İstanbul'],
    ['Bu araç belirtilen hedefe ait alt alan adlarını bulmak için kullanılır.\ndeneme falan fistan '],

]

contact_info2 = [
    ['1  ', 'Subdomain taraması'],
    ['2  ', 'Admin Panel Bulucu'],
    ['3  ', 'Çıkış yap']
]



contact_table = tabulate(contact_info, headers=[" BEN SANA GÜLÜM DİYEMEM , GÜLÜN ÖMRÜ KISA OLUR ", ""], tablefmt="pretty")
contact_angara = tabulate(contact_info2, headers=["NUM", " TASK "], tablefmt="rst")

console_width = shutil.get_terminal_size().columns
table_width = len(contact_table.split('\n')[0])
table_width2 = len(contact_angara.split('\n')[0])
padding = (console_width - table_width) // 2
padding2 = (console_width - table_width2) // 2

padded_table = '\n'.join([' ' * padding + line for line in contact_table.split('\n')])
padded_table2 = '\n'.join([' ' * padding2 + line for line in contact_angara.split('\n')])






print(colored(r'''
                                                                                                        o$$
                                                                                                      $$$$$              ooo
                                                                                                    $$$$$$$$          o$$$" ""oo
                                                                                                  o$$$"$$"$$ o"$$$"oo$"$$$  $$o $
                                                                                                o$$$$ $$$ o $o"     o""""""$o"$$oo"$
                                                                                               o$$$o$o$$$"  $o$$$$$""" oo$$$$$o$$$ "
                                                                                               $$$"$$$$$$ ooo$$""$"  o$$$$$o "$o"$$
                                                                                               $$$ o"$$$$$"  $$$"ooo$ $$$""$$o$$" $o $
                                                                                              "$$$ooo$$$$   $oo$$""$$$$$$  $o$"$ $"$ $
                                                                                               "$$"$$$$$"   $$$    o$$$$oo""o$"  $$ $ $
                                                                                                $$"o$""$    $$$$    "$$$$$o$$"  o$"$$"$
                                                                                                 """ $$$    $$$$o    $$$o$o ""$$$  "$
                                                                                                   oo$"$$    $$$$$" "$$$$ $$ooooo"""""
                                                                                                 o$$"$" $$o  $$$$$$   "o$$o$
                                                                                               o$"" $$oo$$$$o$$$$$$$$$o$$$$
                                                                                             o"$" o$$"  "$$$$$$$"$$"$$$$$$$
                                                                                            o$$o$"""$o    "$$$o"o"o$$"    ""
                                                                                           $$$""     ""o oooo""""""
                                                                                        $o$$"          $$$$$$$$o
                                                                                       o$$$            $"$$$$o$""$o
                                                                                      o$$$"           $$$$$$$$oo"" $
                                                                                     o$oo$            $$"$$$$$$$$"$"$
                                                                                    o$o"$               "$$$$$$$$$$ oo$
                                                                                    oo$$"               ""$ $$$$$$$$$ $
                                                                                    $$"$$                  "ooo$""$$$$$o
                                                                                    $$$"                      ""$$o$"$o"
                                                                                    $$$                           """"$
                                                                                    $$$
                                                                                    $$
                                                                                    $$
                                                                        oo         $$$
                                                                       $$$         $$$  oooo$$ooo$o$oo
                                                                      o$$$$o       $$o$$$$$$$$$$$$$$"
                                                                      $$$$$$o      $$$$$$$$$$$$$$$$"
                                                                     $$$$$$$$o     o$$$$$$$$$o$$$$"
                                                                     $$$$$$$$$o   $$$$$$$$$$$$$$"
                                                                    $$$$$$$$$$$$ o$$$$$$$$$$$$"
                                                                    $$$$$$$$$$$$ oo$"$$$$$$""
                                                                     $$$$$$$$$$$$$"$
                                                                     "$$$$$$$$$$$  $
                                                                       ""$$$$"$$$$ "
                                                                              $$ $$"
                                                                              $$ $$
                                                                              $$ $$
                                                                              "$$$$
                                                                               "$$$

                                                                 █████╗  ██╗   ██╗  ██████╗  ██╗   ██╗ ██╗   ██╗ ███╗   ██╗
                                                                ██╔══██╗ ╚██╗ ██╔╝ ██╔════╝  ██║   ██║ ██║   ██║ ████╗  ██║
                                                                ███████║  ╚████╔╝  ██║  ███╗ ██║   ██║ ██║   ██║ ██╔██╗ ██║
                                                                ██╔══██║   ╚██╔╝   ██║   ██║ ██║   ██║ ██║   ██║ ██║╚██╗██║
                                                                ██║  ██║    ██║    ╚██████╔╝ ╚██████╔╝ ╚██████╔╝ ██║ ╚████║
                                                                ╚═╝  ╚═╝    ╚═╝     ╚═════╝   ╚═════╝   ╚═════╝  ╚═╝  ╚═══╝
''', 'red'))



while True:
    print(colored(padded_table, 'magenta'))
    print(colored(padded_table2, 'cyan'))
    choice = input(colored("[root@ayguun] ", 'white'))

    if choice == "1":
        target = input("Hedef: ")
        find_subdomains(target)
    elif choice == "2":
        target = input("Hedef: ")
        admin_panel_finder(target)
    else:
        print(colored("[-]"))
