#!/usr/bin/python3
import sys
#import platform
import os
import subprocess as sp
from datetime import datetime

now = datetime.now()

dir =f"{os.environ['HOME']}/Desktop"

def addtxt(filename):
    f = open(dir+"/"+filename, 'a')
    f.write("----------------------------------------\n")
    f.close()


def timestamp(time):
    sys.stdout  = open(dir+'/timestamp.txt','w') 
    print(time+": ", now)
    


#def addStartTime():
#    f = open(dir+"/time stamp.txt",'a')
#    f.wirte("Start time : ")
#    f.close()



#def addEndTime():
#    f = open(dir+"/time stamp.txt",'a')
#    f.wirte("End time : ", now)
#    f.close()

#sudo apt-get install net-tools
def networkinfo(): #인터페이스 설정 정보
    try:
        print("-------------- Getting Network Info ... --------------\n Start time : ", now)
        #timestamp("start time")
        #sp.run ('date >>' + dir + '/timestamp.txt', shell=True)
        sp.run ('ifconfig >>' + dir + '/networkinfo.txt', shell=True)
        addtxt("networkinfo.txt")        
        #sp.run ('iwconfig >>' + dir + '/networkinfo.txt', shell=True) #무선랜 네트워크 환경 출력
        #addtxt("networkinfo.txt")
        sp.run ('ifconfig -a >>' + dir + '/networkinfo.txt', shell=True)
        addtxt("networkinfo.txt")
        sp.run('cat /etc/resolv.conf >> ' + dir + '/networkinfo.txt', shell=True)
        addtxt("networkinfo.txt")
        
        print(" End time :  ", now) 
       # addEndTime("networkinfo")             
    except Exception as e:
        print("Failed to collect network information",e)


def arpinfo(): 
    try:
        print("-------------- Getting ARP Info ... --------------\n Start time : ", now) 
        
        sp.run ('arp -v >>' + dir + '/arpinfo.txt', shell=True)
        addtxt("arpinfo.txt")
        sp.run ('arp -a >> ' + dir + '/arpinfo.txt', shell=True)
        addtxt("arpinfo.txt")
        sp.run ('arp -vn >> ' + dir + '/arpinfo.txt', shell=True)
        addtxt("arpinfo.txt")
          
        print(" End time :  ", now)    
    except Exception as e:
        print("Failed to collect network information",e)


def netstatinfo():
    try:
        print("-------------- Getting Netstat Info ... --------------\n Start time : ", now) 
        
        sp.run ('netstat -na >>' + dir + '/netstat.txt', shell=True)
        addtxt("netstat.txt")
        sp.run ('netstat -rn >>' + dir + '/netstat.txt', shell=True)
        addtxt("netstat.txt")
        sp.run ('netstat -es >> ' + dir + '/netstat.txt', shell=True)
        addtxt("netstat.txt")
        sp.run ('netstat -lptu >>' + dir + '/netstat.txt', shell=True) # l : listening, -p : program, t : tcp, u : udp
        addtxt("netstat.txt")
        
        print(" End time :  ", now)
    except Exception as e:
        print("Failed to collect network information",e)


def ssinfo():
    try:
        print("-------------- Getting Socket Info ... --------------\n Start time : ", now) 
      
        sp.run ('ss -t >>' + dir + '/socket.txt', shell=True) # TCP socket 표시
        addtxt("socket.txt")
        sp.run ('ss -u >>' + dir + '/socket.txt', shell=True) # UDP socket 표시
        addtxt("socket.txt")
        sp.run ('ss -a >> ' + dir + '/socket.txt', shell=True)
        
        print(" End time :  ", now)
    except Exception as e:
        print("Failed to collect network information",e)


def netmanagerinfo():
    try:
        print("-------------- Getting Network Manger Info ... --------------\n Start time : ", now) 
        
        sp.run ('nmcli con show >>' + dir + '/netmanage.txt', shell=True) # 네트워크 설정-이름,장치명,UUID등 출력
        addtxt("netmanage.txt")
        sp.run ('nmcli gen >>' + dir + '/netmanage.txt', shell=True) # 전체적인 네트워크 상태확인
        addtxt("netmanage.txt")
        sp.run ('nmcli net >>' + dir + '/netmanage.txt', shell=True) # 네트워크 활성화 상태 출력
        addtxt("netmanage.txt")
        sp.run ('nmcli device >>' + dir + '/netmanage.txt', shell=True) 
        addtxt("netmanage.txt")
        print(" End time :  ", now)
    except Exception as e:
        print("Failed to collect network information",e)


networkinfo()
arpinfo()
netstatinfo()
ssinfo()
netmanagerinfo()