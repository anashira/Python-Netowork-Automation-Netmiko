# -*- coding: utf-8 -*-
"""
Created on Sat Dec 12 18:04:30 2020

@author: ahiraman
"""


from netmiko import ConnectHandler
from os import path

def hostFiles():
    
    if not path.exists("devicedetails.txt"):
        deviceDetailsFile = open('devicedetails.txt','w')
        input("devicedetails.txt file has been created in working directort.\nInput the device details by reading readme file and Press Enter")
        deviceDetailsFile.close()
    else:
        print("devicedetails.txt file already exists in the directory.\nMake sure you have the device details written in the file.\n\n")
        deviceDetailsFile = open('devicedetails.txt', 'r') 
        Lines = deviceDetailsFile.read()
        hostlist = Lines.split('\n')
        return hostlist


def  connectDevice(host,username,passoword):
    device = ConnectHandler(device_type='cisco_ios', ip=host, username=username, password=passoword)
    return device


def commands():
    if not path.exists("commands.txt"):
        commandsFile = open("commands.txt",'w')
        commandsFile.close()
        input("Enter the commands as explained in readme text file and press Enter")
    else:
        commandsFile = open("commands.txt",'r')
        commandline = commandsFile.read()
        print("\n\nCommands to excecute > \n" + commandline + "\n\n")
        commandlineList = commandline.split('\n')
               
        return commandlineList


def sendCommands(device,command, hostname):
    for commandStack in command:
        output = device.send_command(commandStack)
        return output
        #writefile(output, hostname)
        
def writefile(string, filename):
    if not path.exists(filename):
        file= open(filename,'w')
        file.write("\n##############----Start----##############\n")
        file.write(string)
        file.write("\n##############----End----##############\n")
        file.close()
    else:
        file= open(filename,'a+')
        file.write("\n##############----Start----##############\n")
        file.write(string)
        file.write("\n##############----End----##############\n")
        file.close()


def controller():
    
    print("Welcome")
    hostlist = hostFiles()
    
    for host in hostlist:
        host = host.replace(" ", "")
        x = host.split(",")
           
        IpAddress = x[0]
        UserName = x[1]
        Password = x[2]
            
        print("connecting to : " + IpAddress + " with Username : " + UserName)
        
        deviceInstance = connectDevice(IpAddress, UserName, Password)
        commandInstance = commands()
        output = sendCommands(deviceInstance, commandInstance, IpAddress)
        writefile(output, IpAddress)
        deviceInstance.disconnect()
        print("Commands Excecuted!!!\n\nDisconnecting from device: " + IpAddress + "\n\n")
    print("program executed successfully!!!!!!!!!!!")
        
    
controller() 

