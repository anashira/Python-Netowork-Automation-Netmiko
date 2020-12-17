# -*- coding: utf-8 -*-
"""
Created on Sat Dec 12 18:04:30 2020

@author: ahiraman
"""


from netmiko import ConnectHandler
from os import path
    
def  ConnectDevice(host,username,passoword):
    device = ConnectHandler(device_type='cisco_ios', ip=host, username=username, password=passoword)
    return device

def sendCommands(device,command, hostname):
    for commandStack in command:
        output = device.send_command(commandStack)
        writefile(output, hostname)
        


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
        
def commands():
    if not path.exists("commands.txt"):
        commandsFile = open("commands.txt",'w')
        commandsFile.close()
    else:
        commandsFile = open("commands.txt",'r')
        commandline = commandsFile.read()
        print(commandline)
        commandlineList = commandline.split('\n')
        print(commandlineList)
        
        return commandlineList
    
def hostdetailsFetch():
    if not path.exists("devicedetails.txt"):
        deviceDetailsFile = open('devicedetails.txt','w')
        deviceDetailsFile.write("IP Address/hostname, Username, Password")
        deviceDetailsFile.close()
    else:
        print("devicedetails.txt file already exists in the directory.\nMake sure you have the device details written in the file.")
        deviceDetailsFile = open('devicedetails.txt', 'r') 
        Lines = deviceDetailsFile.read()
        linelist = Lines.split('\n')

        
        for line in linelist:
            line = line.replace(" ", "")
            x = line.split(",")
           
            IpAddress = x[0]
            UserName = x[1]
            Password = x[2]
            
            print(IpAddress)
            print(UserName)
            print(Password)
            
            device = ConnectDevice(IpAddress, UserName, Password)
            CommandList = commands()
            sendCommands(device, CommandList, IpAddress)
            device.disconnect()
        print("program executed successfully!!!!!!!!!!!")


hostdetailsFetch();


