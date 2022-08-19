import argparse
from argparse import ArgumentParser
import os
import subprocess as sp
from datetime import datetime

white = "\033[1;37m"
green = '\033[1;32m'
red = '\033[1;31m'
blue = '\033[1;34m'
cyan = '\033[0;36m'
yellow = '\033[0;33m'
noclr = '\033[0m'  
        
def main():
    os.nice(19) #우선순위 설정
   
    dir_main = f"{os.environ['HOME']}/K-Shield_D6"
    if os.path.isdir(dir_main) == False: 
            sp.run([f"mkdir",  dir_main])

    parser = argparse.ArgumentParser(description="Automatically collect Linux artifacts script")
    parser.add_argument('-p', '--process', dest = 'process', action = 'store_true', help = 'Collecting data about process')
    parser.add_argument('-n', '--network', dest = 'network', action = 'store_true', help = 'Collecting data about network')
    parser.add_argument('-s', '--system', dest = 'system', action = 'store_true', help = 'Collecting data about system')
    parser.add_argument('-f', '--file', dest = 'file', action = 'store_true', help = 'Collecting data about file')
    parser.add_argument('-u', '--user', dest = 'user', action = 'store_true', help = 'Collecting data about user')
    parser.add_argument('-a', '--all', dest = 'all', action = 'store_true', help = 'Collecting all data')

    parser.add_argument('--group', dest = 'group', type=str)
    parser.add_argument('--name', dest = 'name', type=str)
    parser.add_argument('--comment', dest = 'comment', type=str) #required=True

    parser.add_argument('-d', '--directory', dest = 'directory', type=str) #선택사항

    args = parser.parse_args() # 입력받은 인자값을 args에 저장

    if args.directory:
        storage_dir = args.directory
    else:
        storage_dir = f"{os.environ['HOME']}/K-Shield_D6/result" 
        
    try:
        if os.path.isdir(storage_dir) == False: # /usr 존재하지 않을때 mkdir 실행시켜 디렉토리 생성
            sp.run([f"mkdir",  storage_dir])  # 수집된 정보들 저장할 디렉토리 생성
            print("Making directory to store investigator's personal information: " + storage_dir)

    except Exception as err:
        print("Error creating directory: ", f"{red}{err}{noclr}")
        return False

    time = datetime.now()
    file = open(storage_dir + '/personal_data.txt', 'a', encoding = 'utf-8')
    name = ''' _______   _     _          _             __   ___  
|__   __| (_)   | |         | |           /_ | / _ \ 
   | |_ __ _ ___| |__  _   _| |________   _| || | | |
   | | '__| / __| '_ \| | | | |______\ \ / / || | | |
   | | |  | \__ \ | | | |_| | |       \ V /| || |_| |
   |_|_|  |_|___/_| |_|\__,_|_|        \_/ |_(_)___/ 
   '''
#이름 수정
    print(f'''\n{white}{name}{noclr}
    Group: {cyan}{args.group}{noclr}
    Name: {cyan}{args.name}{noclr}
    date: {cyan}{time}{noclr}
    Comment: {cyan}{args.comment}{noclr}
    {white}description~~~~~~~~~~~~~{noclr}\n''')

    file.write(f'''Group: {cyan}{args.group}{noclr}
Name: {cyan}{args.name}{noclr}
date: {cyan}{time}{noclr}
Comment: {cyan}{args.comment}{noclr}
{white}description~~~~~~~~~~~~~{noclr}\n''')

    file.close()

    try:
        if args.process:
            sp.call('python3 Process_info.py', shell=True)
        if args.network:
            sp.call('python3 Network_info.py', shell=True)
        if args.system:
            sp.call('python3 System_info.py', shell=True)
        if args.file:
            sp.call('python3 File_info.py', shell=True)
        if args.user:
            sp.call('python3 User_info.py', shell=True)
        if args.all:
            sp.call('python3 Process_info.py', shell=True)
            sp.call('python3 Network_info.py', shell=True)
            sp.call('python3 System_info.py', shell=True)
            sp.call('python3 File_info.py', shell=True)
            sp.call('python3 User_info.py', shell=True)

    except Exception as err:
        print("Error: ", f"{red}{err}{noclr}")
        return False
    
if __name__ == '__main__':
    main()