from genericpath import isfile
import platform
import os
import subprocess
from datetime import date, datetime

pwd = os.getcwd()
savedir = f"{pwd}/sys"

def osmkdir():
    if os.path.isdir(f"{pwd}/sys") == False:
        subprocess.run(['mkdir', f"{pwd}/sys"])

        
def status(name): #실행시 시간정보 출력

    nowtime = datetime.now()

    if os.path.isfile(f"{pwd}/status.txt") == True:
        f = open(pwd + '/status.txt', "a")
        f.write("{} : {}\n".format(name, nowtime.time()))

    elif os.path.isfile(f"{pwd}/status.txt") == False:
        f = open(pwd + '/status.txt', "w")
        f.write("today : {}\n".format(nowtime.date()))
        f.write("---------------------------------------\n")
        f.write("{} : {}\n.".format(name, nowtime.time()))
    
    
    print("-------------------time : {}-------------------\n".format(nowtime.time()))
    print("-----------------------{}------------------\n".format(name))
    
    f.close()
  
  

def file_save(path, filename, savename):
    

    if os.path.isfile(savedir + savename) == True:

        f = open(path + filename, "r")
        s = open(savedir + savename, "a")
        data = f.read()
        s.write("----------------------{}--------------------------------\n".format(filename))
        s.write(data)
        s.write("-----------------------------------------------------\n")
        s.close()    
        f.close
    elif os.path.isfile(savedir + savename) == False:
        f = open(path + filename, "r")
        s = open(savedir + savename, "w")
        data = f.read()
        s.write("----------------------{}--------------------------------\n".format(filename))
        s.write(data)
        s.write("-----------------------------------------------------\n")
        s.close()    
        f.close











def sys_info():
    status("system_info")
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


    status("fstab")
    #etc/fstab 부팅시 마운트 정보
    file_save("/etc/","fstab","/system_info.txt")
    
    
    
    
    status("mtab")
    # /etc/mtab 현재 마운트 상태에 대한 정보
    file_save("/etc/","mtab","/system_info.txt")
    


    status("issue")
    i = open(savedir + '/issue.txt', "w") #로그인전 로컬접속시도 message
    i.write("----------------/etc/issue------------------\n")
    issue = open("/etc/issue", "r")
    issue_data = issue.read()
    i.write(issue_data)
    i.write("------------------------------------------------\n")
    i.close()
    issue.close()

    status("issue.net")
    i = open(savedir + '/issue.txt', "a")# 로그인전 원격접속시도시 message
    i.write("----------------/etc/issue.net------------------\n")
    issue = open("/etc/issue.net", "r")
    issue_data = issue.read()
    i.write(issue_data)
    i.write("------------------------------------------------\n")
    i.close()
    issue.close()


    
sys_info()

    
#ubuntu 20 /etc/inittab이 없음..?
