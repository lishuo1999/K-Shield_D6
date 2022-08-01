import platform
import os
import subprocess
from datetime import date, datetime

pwd = os.getcwd()
savedir = f"{pwd}/sys"

def osmkdir():
    if os.path.isdir(f"{pwd}/sys") == False:
        subprocess.run(['mkdir', f"{pwd}/sys"])

def sys_info():
    print("----progressing systeminfo-----")
    s = open(savedir + '/system_info.txt', "w")
    s.write("----------------sysytem_info------------------\n")
    s.write("Architecture : " + platform.architecture()[0] + "\n") #architecture
    s.write("Machine : " + platform.machine() + "\n") #machine
    s.write("Node : " + platform.node() + "\n")    #node
    s.write("System : " + platform.system() + "\n") #os
    now = str(datetime.now()) # 현재시간
    s.write("local time : " + now + "\n")
    s.write("-------------------------------------------------\n")
    s.close()


    print("------progressing fstab-----")
    #etc/fstab 부팅시 마운트 정보
    f = open("/etc/fstab", "r")
    s = open(savedir + '/system_info.txt', "a")
    data = f.read()
    s.write("---------------fstab--------------------------------\n")
    s.write(data)
    s.write("-----------------------------------------------------\n")
    s.close()    
    f.close

    print("---------progressing mtab---------------")
    # /etc/mtab 현재 마운트 상태에 대한 정보
    mtab= open("/etc/mtab", "r")
    s2 = open(savedir + '/system_info.txt', "a")
    data2=mtab.read()
    s2.write("--------------------mtab-------------------------------\n")
    s2.write(data2)
    s2.write("-------------------------------------------------\n")
    f.close()
    s2.close()


    
    
    
    
#ubuntu 20 /etc/inittab이 없음..?
