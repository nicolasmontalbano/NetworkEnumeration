#!/usr/bin/python3
import os

def Main():
    Menu()

def EnumHosts():
    ip = input("IP: ")
    ipArray = str(ip).split('.')
    ipArray[3] = 0
    newIP = ''
    for oct in range(3):
        newIP += str(ipArray[oct]) + '.'
    newIP += str(ipArray[3]) +'/24'

    while(True):
        fileName = input("Enter the file name: ")
        if(not os.path.exists(fileName)):
            os.system(f"nmap -sN {newIP} -oG {fileName}.txt")
            break
        else:
            print("The file name already exists, please choose another")

def EnumAllPorts(ip):
    os.system(f"echo '{ip}' > target_{ip}.txt")
    os.system(f"nmap -p- -iL target_{ip}.txt")

def EnumServices(ip):
    os.system(f"nmap -p- -sV -iL target_{ip}.txt")

def Menu():
    print("1) Hosts Enumeration")
    print("2) Ports and Services Enumeration")
    print("0) Exit")

    option = int(input("Enter your option: "))

    while(option != 0):
        if(option == 1):
            print("\n\n\n--------------------------------HOSTS--------------------------------\n\n\n")
            EnumHosts()
            option = 0
        elif(option == 2):
            ip = input("Enter target IP: ")
            print("\n\n\n--------------------------------ALL PORTS--------------------------------\n\n\n")
            EnumAllPorts(ip)
            print("\n\n\n--------------------------------SERVICES--------------------------------\n\n\n")
            EnumServices(ip)
            option = 0
        else:
            print("Invalid option")
        Menu()

    
    
Main()