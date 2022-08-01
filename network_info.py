#!/usr/bin/python3
#import sys
#import platform
import os
import subprocess as sp

dir =f"{os.environ['HOME']}/Desktop"

#sudo apt-get install net-tools
def networkinfo(): #인터페이스 설정 정보
    try:
        sp.run ('ifconfig >>' + dir + '/networkinfo.txt', shell=True)
        sp.run ('arp -v >>' + dir + '/networkinfo.txt', shell=True)
        sp.run ('arp -a >> ' + dir + '/networkinfo.txt', shell=True)
        sp.run ('arp -vn >> ' + dir + '/networkinfo.txt', shell=True)
        print(" Getting Network Info ... ")
    except Exception as e:
        print("Failed to collect network information")

def netstatinfo():
    try:
        sp.run ('netstat -na >>' + dir + '/netstat.txt', shell=True)       
        sp.run ('netstat -rn >>' + dir + '/netstat.txt', shell=True)
        sp.run ('netstat -es >> ' + dir + '/netstat.txt', shell=True)
        print(" Getting Netstat Info ... ")
    except Exception as e:
        print("Failed to collect network information")

def ssinfo():
    try:
        sp.run ('ss -t >>' + dir + '/socket.txt', shell=True) # TCP socket 표시
        sp.run ('ss -u >>' + dir + '/socket.txt', shell=True) # UDP socket 표시
        sp.run ('ss -a >> ' + dir + '/socket.txt', shell=True)
        print(" Getting Socket Info ... ")
    except Exception as e:
        print("Failed to collect network information")

#networkinfo()
netstatinfo()
#ssinfo()