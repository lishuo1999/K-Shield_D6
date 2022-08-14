#!/bin/python3

from __future__ import print_function
from collections import OrderedDict
import subprocess
import os,sys,time
import pprint

dir=f"{os.environ['HOME']}/K-Shiled_D6/pro"
def make_dir(dir): 
    try:
        if os.path.isdir(dir) == False: # /usr 존재하지 않을때 mkdir 실행시켜 디렉토리 생성
            subprocess.run([f"mkdir",  dir])  # 수집된 정보들 저장할 디렉토리 생성
            print("Making directory to store evidence: " + dir)

    except Exception as err:
        print("Error creating directory: {err}")
        return False
make_dir(dir)

#시스템에 동작중인 모든 프로세스 소유자 정보 출력
def ps_aux():
    subprocess.call('ps aux', shell=True)
    subprocess.call('ps aux > ps_aux_result.txt', shell=True) #명령어 실행 결과 ps_aux_result.txt 파일로 저장
ps_aux()

#부모 프로세스와 자식 프로세스 확인
def ps_ef():
    subprocess.call('ps -ef', shell=True)
    subprocess.call('ps -ef > ps_ef_result.txt', shell=True) #명령어 실행 결과 ps_ef_result.txt 파일로 저장
ps_ef()

#실행되는 task 유동적 관찰, 실시간 os 상태 줄력
def top():
    process = os.popen('top -n 1')
    preprocessed = process.read()
    process.close()
     #명령어 실행 결과 top_result.txt 파일로 저장
    output = 'top_result.txt'
    fout = open(output,'w')
    fout.write(preprocessed)
    fout.close()
    print(preprocessed)
top()

#Filename:CPU1.py
#Filename:meminfo.py

#프로세서 정보 출력, cpu에 관련된 다양한 정보 출력
def CPUinfo():

    CPUinfo=OrderedDict()
    procinfo=OrderedDict()
    nprocs = 0
    with open('/proc/cpuinfo') as f:
        for line in f:
            if not line.strip():
                #end of one processor
                CPUinfo['proc%s' % nprocs]=procinfo
                nprocs = nprocs+1
                #Reset
                procinfo=OrderedDict()
            else:
                if len(line.split(':')) == 2:
                    procinfo[line.split(':')[0].strip()] = line.split(':')[1].strip()
                else:
                    procinfo[line.split(':')[0].strip()] = ''
    return CPUinfo

if __name__ == '__main__':
    CPUinfo = CPUinfo()
    for processor in CPUinfo.keys():
        print('CPUinfo[{0}]={1}'.format(processor,CPUinfo[processor]['model name']))
         #명령어 실행 결과 CPUinfo_result.txt 파일로 저장
        f = open('CPUinfo_result.txt', 'w')
        f.write('CPUinfo[{0}]={1}'.format(processor,CPUinfo[processor]['model name']))
        f.close()

#메모리에 관한 상세 정보 출력
def meminfo():

    meminfo = OrderedDict()
    with open('/proc/meminfo') as f:
        for line in f:
            meminfo[line.split(':')[0]] = line.split(':')[1].strip()
    return meminfo

if __name__ == '__main__':
    meminfo = meminfo()
    print("Total memory:{0}".format(meminfo['MemTotal']))
    print("Free memory:{0}".format(meminfo['MemFree']))
     #명령어 실행 결과 meminfo_result.txt 파일로 저장
    f = open('meminfo_result.txt', 'w')
    f.write("Free memory:{0}".format(meminfo['MemFree']))
    f.write("Free memory:{0}".format(meminfo['MemFree']))
    f.close()

#시스템 부팅 메세지 
def dmesg():
    subprocess.call('sudo dmesg', shell=True)
    subprocess.call('sudo dmesg > dmesg_result.txt', shell=True)  #명령어 실행 결과 dmesg_result.txt 파일로 저장
dmesg()
