import os, time, webbrowser

from colorama import Fore, Style

print ('\n')
def res():
    print(Style.RESET_ALL)
    
while True:
    os.system('clear')
     print(Fore.RED+['меню установщика'])
     print("
╔══╦═╗─╔╦═══╦════╦═══╦╗──╔╗──╔═══╦═══╗
╚╣╠╣║╚╗║║╔═╗║╔╗╔╗║╔═╗║║──║║──║╔══╣╔═╗║
─║║║╔╗╚╝║╚══╬╝║║╚╣║─║║║──║║──║╚══╣╚═╝║
─║║║║╚╗║╠══╗║─║║─║╚═╝║║─╔╣║─╔╣╔══╣╔╗╔╝
╔╣╠╣║─║║║╚═╝║─║║─║╔═╗║╚═╝║╚═╝║╚══╣║║╚╗
╚══╩╝─╚═╩═══╝─╚╝─╚╝─╚╩═══╩═══╩═══╩╝╚═╝")
     print("telegram: [@HORROR SOFT]")
     res()
     print (Fore.YELLOW+"    [1] ddos ")
     print (Fore.YELLOW+"    [2] bomber ")
     print (Fore.YELLOW+"    [00] exit  ")
     inp = input ('  Выбери пункт>>> ')
     os.system('clear')
     
     if inp == '1':
        os.system('clear')
        os.system('python3 ddos.py')
           
     if inp == '2'
        os.system('clear')
        os.system('python3 bomber.py')
           
     if inp == '00':
        os.system('clear')
        print('Спасибо за использование [installer]')
        break
