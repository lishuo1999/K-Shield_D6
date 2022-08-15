#!/usr/bin/python3
#import sys
#import platform
import os
import subprocess as sp
from datetime import datetime

now = datetime.now()

# 경로 설정
dir =f"{os.environ['HOME']}/K-Shield_D6/net"

def make_dir(dir): 
    try:
        if os.path.isdir(dir) == False: # /usr 존재하지 않을때 mkdir 실행시켜 디렉토리 생성
            sp.run([f"mkdir",  dir])  # 수집된 정보들 저장할 디렉토리 생성
            print("Making directory to store evidence: " + dir)

    except Exception as err:
        print("Error creating directory: {err}")
        return False


def addtxt(filename):
    f = open(dir+"/"+filename, 'a')
    f.write("----------------------------------------\n")
    f.close()


#def timestamp(time):
#    sys.stdout  = open(dir+'/timestamp.txt','w') 
#    print(time+": ", now)
    


#sudo apt-get install net-tools
def networkinfo(): #인터페이스 설정 정보
    try:
        print("-------------- Getting Network Info ... --------------\n Start time : ", now)
        
        sp.run ('ifconfig >>' + dir + '/networkinfo.txt', shell=True) # interface configuration
        addtxt("networkinfo.txt")        
        #sp.run ('iwconfig >>' + dir + '/networkinfo.txt', shell=True) # 무선랜 네트워크 환경 출력
        #addtxt("networkinfo.txt")
        sp.run ('ifconfig -a >>' + dir + '/networkinfo.txt', shell=True) # 모든 네트워크 인터페이스 구성 확인하기
        addtxt("networkinfo.txt")
        sp.run('cat /etc/resolv.conf >> ' + dir + '/networkinfo.txt', shell=True) # 네임서버 지정 파일 확인
        addtxt("networkinfo.txt")
        sp.run('ip link show >> ' + dir + '/networkinfo.txt', shell=True)
        addtxt("networkinfo.txt")
        
        print(" End time :  ", now) 
       # addEndTime("networkinfo")     
               
    except Exception as e:
        print("Failed to collect network information",e)


def arpinfo(): # arp 명령어를 사용한 네트워크 정보 수집
    try:
        print("-------------- Getting ARP Info ... --------------\n Start time : ", now) 
        
        sp.run ('arp -v >>' + dir + '/arpinfo.txt', shell=True) # arp상태 출력
        addtxt("arpinfo.txt")
        sp.run ('arp -a >> ' + dir + '/arpinfo.txt', shell=True) # 모든 arp 테이블 확인
        addtxt("arpinfo.txt")
        sp.run ('arp -vn >> ' + dir + '/arpinfo.txt', shell=True) #
        addtxt("arpinfo.txt")
          
        print(" End time :  ", now)    

    except Exception as e:
        print("Failed to collect network information",e)


def netstatinfo(): #네트워크 연결상태, 라우팅테이블, 인터페이스 상태 등
    try:
        print("-------------- Getting Netstat Info ... --------------\n Start time : ", now) 
        
        sp.run ('netstat -na >>' + dir + '/netstat.txt', shell=True) # 네트워크에 대기중인 상태 확인
        addtxt("netstat.txt")
        sp.run ('netstat -na -s >>' + dir + '/netstat.txt', shell=True) # 각각의 프로토콜에서 전송된 패킷 양 확인
        addtxt("netstat.txt")
        sp.run ('netstat -r >>' + dir + '/netstat.txt', shell=True) # 라우팅 테이블 출력
        addtxt("netstat.txt")
        sp.run ('netstat -i >>' + dir + '/netstat.txt', shell=True) #인터페이스 별 send/receive 통계 모니터링
        addtxt("netstat.txt")
        sp.run ('netstat -rn >>' + dir + '/netstat.txt', shell=True)
        addtxt("netstat.txt")
        sp.run ('netstat -es >> ' + dir + '/netstat.txt', shell=True)
        addtxt("netstat.txt")
        sp.run ('netstat -s >> ' + dir + '/netstat.txt', shell=True) # IP, ICMP, UDP 프로토콜별의 상태확인
        addtxt("netstat.txt")
        sp.run ('sudo netstat -nap|grep LISTEN >> ' + dir + '/netstat.txt', shell=True) #Listen 상태인 포트만 출력하기
        addtxt("netstat.txt")
        #sp.run ('netstat -v >> ' + dir + '/netstat.txt', shell=True) # 버전출력
        #addtxt("netstat.txt")
        sp.run ('netstat -at >> ' + dir + '/netstat.txt', shell=True) # TCP만 확인
        addtxt("netstat.txt")
        sp.run ('netstat -au >> ' + dir + '/netstat.txt', shell=True) # UDP만 확인
        addtxt("netstat.txt")
        sp.run ('netstat -g >> ' + dir + '/netstat.txt', shell=True) # 멀티캐스트에 대한 정보 출력
        addtxt("netstat.txt")
        #sp.run ('netstat -M >> ' + dir + '/netstat.txt', shell=True) # 마스커레이딩 정보 출력
        #addtxt("netstat.txt")
        sp.run ('netstat -w >> ' + dir + '/netstat.txt', shell=True) # raw 프로토콜만 출력
        addtxt("netstat.txt")
        sp.run ('netstat -l >> ' + dir + '/netstat.txt', shell=True) # 대기중인 네트워크
        addtxt("netstat.txt")
        sp.run ('sudo netstat -lptu >>' + dir + '/netstat.txt', shell=True) # l : listening, -p : program, t : tcp, u : udp
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
        sp.run ('nmcli device >>' + dir + '/netmanage.txt', shell=True) #디바이스 상세정보
        addtxt("netmanage.txt")
        print(" End time :  ", now)

    except Exception as e:
        print("Failed to collect network information",e)

#sudo apt-get install traceroute
def troute(): #네트워크 테스트, 측정 및 관리
    try:
        print("-------------- Getting Extra Network Info ... --------------\n Start time : ", now) 
        
        #sp.run ('traceroute -V >>' + dir + '/extrainfo.txt', shell=True) # 네트워크 설정-이름,장치명,UUID등 출력
        #addtxt("extrainfo.txt")
        sp.run ('sudo nmap -n -PN -sT -sU -p- localhost >>' + dir + '/extrainfo.txt', shell=True) #nmap으로 port 스캔
        addtxt("extrainfo.txt")
        sp.run ('sudo lsof -i >>' + dir + '/extrainfo.txt', shell=True) #모든 네트워크 파일보기
        addtxt("extrainfo.txt")
        print(" End time :  ", now)

    except Exception as e:
        print("Failed to collect network information",e)





make_dir(dir)

networkinfo()
arpinfo()
netstatinfo()
ssinfo()

netmanagerinfo()
troute()
