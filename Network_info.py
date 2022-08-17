#!/usr/bin/python3
#import sys
#import platform
import os
import subprocess as sp
from datetime import datetime

red = '\033[1;31m'
yellow = '\033[0;33m'
noclr = '\033[0m'

# 경로 설정
dir =f"{os.environ['HOME']}/K-Shield_D6/net"

<<<<<<< HEAD
=======
def make_dir(dir): 
    try:
        if os.path.isdir(dir) == False: # /usr 존재하지 않을때 mkdir 실행시켜 디렉토리 생성
            sp.run([f"mkdir",  dir])  # 수집된 정보들 저장할 디렉토리 생성
            print("Making directory to store evidence: " + dir)

    except Exception as err:
        print("Error creating directory: ",f"{red}{err}{noclr}")
        return False
>>>>>>> a9aee20 (commit)


def addtxt(filename):
    f = open(dir+"/"+filename, 'a')
    f.write("----------------------------------------\n")
    f.close()


#def timestamp(time):
#    sys.stdout  = open(dir+'/timestamp.txt','w') 
#    print(time+": ", now)
<<<<<<< HEAD

if os.path.isdir(dir) == False:
    sp.run ([f"mkdir","-p",  dir])
=======
>>>>>>> a9aee20 (commit)

#sudo apt-get install net-tools
def networkinfo(): #인터페이스 설정 정보
    try:
        now = datetime.now()
        print("-------------- Getting Network Info ... --------------\n Start time : ", f"{yellow}{now}{noclr}")
        
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

        now = datetime.now()
        print(" End time :  ", f"{yellow}{now}{noclr}") 
       # addEndTime("networkinfo")     
               
    except Exception as e:
        print("Failed to collect network information", f"{red}{e}{noclr}")


def arpinfo(): # arp 명령어를 사용한 네트워크 정보 수집
    try:
        now = datetime.now()
        print("-------------- Getting ARP Info ... --------------\n Start time : ", f"{yellow}{now}{noclr}") 
        
        sp.run ('arp -v >>' + dir + '/arpinfo.txt', shell=True) # arp상태 출력
        addtxt("arpinfo.txt")
        sp.run ('arp -a >> ' + dir + '/arpinfo.txt', shell=True) # 모든 arp 테이블 확인
        addtxt("arpinfo.txt")
        sp.run ('arp -an >> ' + dir + '/arpinfo.txt', shell=True) # 캐시 테이블 확인
        addtxt("arpinfo.txt")
        sp.run ('arp -v >> ' + dir + '/arpinfo.txt', shell=True) # 자세한 모드로 결과 출력
        addtxt("arpinfo.txt")
        sp.run ('arp -vn >> ' + dir + '/arpinfo.txt', shell=True) # n: Resolving 하지 않은 IP 주소로 출력
        addtxt("arpinfo.txt")
        
        now = datetime.now()
        print(" End time :  ", f"{yellow}{now}{noclr}")    

    except Exception as e:
        print("Failed to collect network information", f"{red}{e}{noclr}")


def netstatinfo(): #네트워크 연결상태, 라우팅테이블, 인터페이스 상태 등
    try:
        now = datetime.now()
        print("-------------- Getting Netstat Info ... --------------\n Start time : ", f"{yellow}{now}{noclr}") 
        
        sp.run ('netstat -na >>' + dir + '/netstat.txt', shell=True) # 네트워크에 대기중인 상태 확인
        addtxt("netstat.txt")
        sp.run ('netstat -na -s >>' + dir + '/netstat.txt', shell=True) # 각각의 프로토콜에서 전송된 패킷 양 확인
        addtxt("netstat.txt")
        sp.run ('netstat -r >>' + dir + '/netstat.txt', shell=True) # 라우팅 테이블 출력
        addtxt("netstat.txt")
        sp.run ('netstat -i >>' + dir + '/netstat.txt', shell=True) #인터페이스 별 send/receive 통계 모니터링
        addtxt("netstat.txt")
        sp.run ('netstat -rn >>' + dir + '/netstat.txt', shell=True) # routing 정보 보기
        addtxt("netstat.txt")
        sp.run ('netstat -es >> ' + dir + '/netstat.txt', shell=True)
        addtxt("netstat.txt")
        sp.run ('netstat -s >> ' + dir + '/netstat.txt', shell=True) # IP, ICMP, UDP 프로토콜별의 상태확인
        addtxt("netstat.txt")
        sp.run ('sudo netstat -nap|grep LISTEN >> ' + dir + '/netstat.txt', shell=True) #Listen 상태인 포트만 출력하기
        addtxt("netstat.txt")
        #sp.run ('netstat -v >> ' + dir + '/netstat.txt', shell=True) # 버전출력
        #addtxt("netstat.txt")
        sp.run ('sudo netstat -t >> ' + dir + '/netstat.txt', shell=True) # listening 중인 TCP소켓
        addtxt("netstat.txt")
        sp.run ('sudo netstat -antup >> ' + dir + '/netstat.txt', shell=True) # listening 소켓 정보 상세
        addtxt("netstat.txt")
        sp.run ('netstat -at >> ' + dir + '/netstat.txt', shell=True) # TCP만 확인 (수신 대기 연결과 설정된 연결로만 범위 제한)
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
        
        now = datetime.now()
        print(" End time :  ", f"{yellow}{now}{noclr}")

    except Exception as e:
        print("Failed to collect network information",f"{red}{e}{noclr}")


def ssinfo():
    try:
        now = datetime.now()
        print("-------------- Getting Socket Info ... --------------\n Start time : ", f"{yellow}{now}{noclr}") 
      
        sp.run ('ss -t >>' + dir + '/socket.txt', shell=True) # listening socket 제외 현재 연결된 소켓 표시
        addtxt("socket.txt")
        sp.run ('ss -t >>' + dir + '/socket.txt', shell=True) # TCP socket 표시
        addtxt("socket.txt")
        sp.run ('ss -u >>' + dir + '/socket.txt', shell=True) # UDP socket 표시
        addtxt("socket.txt")
        sp.run ('ss -a >> ' + dir + '/socket.txt', shell=True) # listening socket 포함 모든 소켓 표시
        addtxt("socket.txt")
        sp.run ('ss -lt src :80 >>' + dir + '/socket.txt', shell=True) # TCP 80 port listening 소켓 표시
        addtxt("socket.txt")
        sp.run ('ss -t src :443 >>' + dir + '/socket.txt', shell=True) # https에 연결한 외부 IP
        addtxt("socket.txt")
        sp.run ('ss -t dst :443 >>' + dir + '/socket.txt', shell=True) # https에 연결한 외부 IP
        addtxt("socket.txt")
        sp.run ('ss -pt dst :443 >>' + dir + '/socket.txt', shell=True) # 외부 https에 연결한 프로세스 목록
        addtxt("socket.txt")
        
        now = datetime.now()
        print(" End time :  ", f"{yellow}{now}{noclr}")

    except Exception as e:
        print("Failed to collect network information",f"{red}{e}{noclr}")


def netmanagerinfo():
    try:
        now = datetime.now()
        print("-------------- Getting Network Manger Info ... --------------\n Start time : ", f"{yellow}{now}{noclr}") 
        
        sp.run ('nmcli con show >>' + dir + '/netmanage.txt', shell=True) # 네트워크 설정-이름,장치명,UUID등 출력
        addtxt("netmanage.txt")
        sp.run ('nmcli gen >>' + dir + '/netmanage.txt', shell=True) # 전체적인 네트워크 상태확인
        addtxt("netmanage.txt")
        sp.run ('nmcli net >>' + dir + '/netmanage.txt', shell=True) # 네트워크 활성화 상태 출력
        addtxt("netmanage.txt")
        sp.run ('nmcli device >>' + dir + '/netmanage.txt', shell=True) #디바이스 상세정보
        addtxt("netmanage.txt")

        now = datetime.now()
        print(" End time :  ", f"{yellow}{now}{noclr}")

    except Exception as e:
        print("Failed to collect network information",f"{red}{e}{noclr}")

#sudo apt-get install traceroute
def troute(): #네트워크 테스트, 측정 및 관리
    try:
<<<<<<< HEAD
        print("-------------- Getting Extra Network Info ... --------------\n Start time : ", now) 
        sp.run ('ip addr show >>' + dir + '/extrainfo.txt', shell=True) 
        addtxt("extrainfo.txt")
        sp.run('cat /proc/net/dev >> ' + dir + '/extrainfo.txt', shell=True) #/proc 파일 시스템을 통해서 네트워크 정보 수집
        addtxt("extrainfo.txt")
        sp.run('cat /proc/net/dev_mcast >> ' + dir + '/extrainfo.txt', shell=True) 
        addtxt("extrainfo.txt")
        sp.run('cat /proc/net/connector >> ' + dir + '/extrainfo.txt', shell=True) 
        addtxt("extrainfo.txt")
        sp.run('cat /proc/net/fib_trie >> ' + dir + '/extrainfo.txt', shell=True) 
        addtxt("extrainfo.txt")
        sp.run('cat /proc/net/fib_triestat >> ' + dir + '/extrainfo.txt', shell=True) 
        addtxt("extrainfo.txt")
        sp.run('cat /proc/net/hci >> ' + dir + '/extrainfo.txt', shell=True) 
        addtxt("extrainfo.txt")
        sp.run('cat /proc/net/icmp >> ' + dir + '/extrainfo.txt', shell=True) 
        addtxt("extrainfo.txt")
        sp.run('cat /proc/net/icmp6 >> ' + dir + '/extrainfo.txt', shell=True) 
        addtxt("extrainfo.txt")
        sp.run('cat /proc/net/if_inet6 >> ' + dir + '/extrainfo.txt', shell=True) 
        addtxt("extrainfo.txt")
        sp.run('cat /proc/net/igmp >> ' + dir + '/extrainfo.txt', shell=True) 
        addtxt("extrainfo.txt")
        sp.run('cat /proc/net/igmp6 >> ' + dir + '/extrainfo.txt', shell=True) 
        addtxt("extrainfo.txt")
        sp.run('cat /proc/net/ip6_flowlabel >> ' + dir + '/extrainfo.txt', shell=True) 
        addtxt("extrainfo.txt")
        sp.run('cat /proc/net/ip6_mr_cache >> ' + dir + '/extrainfo.txt', shell=True) 
        addtxt("extrainfo.txt")
        sp.run('cat /proc/net/ip6_mr_vif >> ' + dir + '/extrainfo.txt', shell=True) 
        addtxt("extrainfo.txt")
        sp.run('cat /proc/net/ip_mr_cache >> ' + dir + '/extrainfo.txt', shell=True) 
        addtxt("extrainfo.txt")
        sp.run('cat /proc/net/ip_mr_vif >> ' + dir + '/extrainfo.txt', shell=True) 
        addtxt("extrainfo.txt")
        sp.run('sudo cat /proc/net/ip_tables_matches >> ' + dir + '/extrainfo.txt', shell=True) 
        addtxt("extrainfo.txt")
        sp.run('cat /proc/net/ipv6_route >> ' + dir + '/extrainfo.txt', shell=True) 
        addtxt("extrainfo.txt")
        sp.run('cat /proc/net/l2cap >> ' + dir + '/extrainfo.txt', shell=True) 
        addtxt("extrainfo.txt")
        sp.run('cat /proc/net/mcfilter >> ' + dir + '/extrainfo.txt', shell=True) 
        addtxt("extrainfo.txt")
        sp.run('cat /proc/net/mcfilter6 >> ' + dir + '/extrainfo.txt', shell=True) 
        addtxt("extrainfo.txt")
        sp.run('cat /proc/net/netlink >> ' + dir + '/extrainfo.txt', shell=True) 
        addtxt("extrainfo.txt")
        sp.run('cat /proc/net/netstat >> ' + dir + '/extrainfo.txt', shell=True) 
        addtxt("extrainfo.txt")
        sp.run('cat /proc/net/packet >> ' + dir + '/extrainfo.txt', shell=True) 
        addtxt("extrainfo.txt")
        sp.run('cat /proc/net/protocols >> ' + dir + '/extrainfo.txt', shell=True) 
        addtxt("extrainfo.txt")
        sp.run('cat /proc/net/psched >> ' + dir + '/extrainfo.txt', shell=True) 
        addtxt("extrainfo.txt")
        sp.run('cat /proc/net/ptype >> ' + dir + '/extrainfo.txt', shell=True) 
        addtxt("extrainfo.txt")
        sp.run('cat /proc/net/raw >> ' + dir + '/extrainfo.txt', shell=True) 
        addtxt("extrainfo.txt")
        sp.run('cat /proc/net/raw6 >> ' + dir + '/extrainfo.txt', shell=True) 
        addtxt("extrainfo.txt")
        sp.run('cat /proc/net/rfcomm >> ' + dir + '/extrainfo.txt', shell=True) 
        addtxt("extrainfo.txt")
        sp.run('cat /proc/net/route >> ' + dir + '/extrainfo.txt', shell=True) 
        addtxt("extrainfo.txt")
        sp.run('cat /proc/net/rt6_stats >> ' + dir + '/extrainfo.txt', shell=True) 
        addtxt("extrainfo.txt")
        sp.run('cat /proc/net/rt_cache >> ' + dir + '/extrainfo.txt', shell=True) 
        addtxt("extrainfo.txt")
        sp.run('cat /proc/net/sco >> ' + dir + '/extrainfo.txt', shell=True) 
        addtxt("extrainfo.txt")
        sp.run('cat /proc/net/snmp >> ' + dir + '/extrainfo.txt', shell=True) 
        addtxt("extrainfo.txt")
        sp.run('cat /proc/net/snmp6 >> ' + dir + '/extrainfo.txt', shell=True) 
        addtxt("extrainfo.txt")
        sp.run('cat /proc/net/sockstat >> ' + dir + '/extrainfo.txt', shell=True) 
        addtxt("extrainfo.txt")
        sp.run('cat /proc/net/sockstat6 >> ' + dir + '/extrainfo.txt', shell=True) 
        addtxt("extrainfo.txt")
        sp.run('cat /proc/net/softnet_stat >> ' + dir + '/extrainfo.txt', shell=True) 
        addtxt("extrainfo.txt")
        sp.run('cat /proc/net/tcp >> ' + dir + '/extrainfo.txt', shell=True) 
        addtxt("extrainfo.txt")
        sp.run('cat /proc/net/tcp6 >> ' + dir + '/extrainfo.txt', shell=True) 
        addtxt("extrainfo.txt")
        sp.run('cat /proc/net/udp >> ' + dir + '/extrainfo.txt', shell=True) 
        addtxt("extrainfo.txt")
        sp.run('cat /proc/net/udp6 >> ' + dir + '/extrainfo.txt', shell=True) 
        addtxt("extrainfo.txt")
        sp.run('cat /proc/net/udplite >> ' + dir + '/extrainfo.txt', shell=True) 
        addtxt("extrainfo.txt")
        sp.run('cat /proc/net/udplite6 >> ' + dir + '/extrainfo.txt', shell=True) 
        addtxt("extrainfo.txt")
        sp.run('cat /proc/net/unix >> ' + dir + '/extrainfo.txt', shell=True) 
        addtxt("extrainfo.txt")
        sp.run('cat /proc/net/xfrm_stat >> ' + dir + '/extrainfo.txt', shell=True) 
        addtxt("extrainfo.txt")

=======
        now = datetime.now()
        print("-------------- Getting Extra Network Info ... --------------\n Start time : ", f"{yellow}{now}{noclr}") 
>>>>>>> a9aee20 (commit)
        
        #sp.run ('traceroute -V >>' + dir + '/extrainfo.txt', shell=True) # 네트워크 설정-이름,장치명,UUID등 출력
        #addtxt("extrainfo.txt")
        sp.run ('sudo nmap -n -PN -sT -sU -p- localhost >>' + dir + '/extrainfo.txt', shell=True) #nmap으로 port 스캔
        addtxt("extrainfo.txt")
        sp.run ('sudo lsof -i >>' + dir + '/extrainfo.txt', shell=True) #모든 네트워크 파일보기
        addtxt("extrainfo.txt")

        now = datetime.now()
        print(" End time :  ", f"{yellow}{now}{noclr}")

    except Exception as e:
        print("Failed to collect network information",f"{red}{e}{noclr}")


networkinfo()
arpinfo()
netstatinfo()
ssinfo()

netmanagerinfo()
troute()