import optparse
import argparse
from argparse import ArgumentParser
import os
import subprocess as sp

white = "\033[1;37m"
green = '\033[1;32m'
red = '\033[1;31m'
blue = '\033[1;34m'
cyan = '\033[0;36m'
yellow = '\033[0;33m'
noclr = '\033[0m'

class forensic_project:
    def __init__(self) -> None: #constructor
        self.storage_dir = f"{os.environ['HOME']}/usr_inf" # /home/leeseok/usr_inf 에 저장된 값 읽어옴
        if os.path.isdir(self.storage_dir) == False: # /usr_inf 존재하지 않을때 mkdir 실행  
                print(f"Making directory to store evidence: {self.storage_dir}")
                sp.run([f"mkdir",  self.storage_dir])  # 수집된 정보들 저장할 디렉토리 생성
            
    def find_user_inf(self):  # 로그인 정보 수집
        try:
            if os.path.isfile(self.storage_dir + '/login_fail.txt') == False:
                print("Collecting system login failure history via 'lastb' command ...")
                sp.run('sudo lastb >> ' + self.storage_dir + '/login_fail.txt', shell=True)
            
            if os.path.isfile(self.storage_dir + '/login_lastlog.txt') == False:
                print("Collecting system login history via 'lastlog' command ...")
                sp.run('sudo lastlog >> ' + self.storage_dir + '/login_lastlog.txt', shell=True)

            if os.path.isfile(self.storage_dir + '/login_user.txt') == False:
                print("Collecting Login User Information via 'who' command ...")
                sp.run('who >> ' + self.storage_dir + '/login_user.txt', shell=True)

            if os.path.isfile(self.storage_dir + '/login_user.txt') == False:
                print("Collecting Login User Information via 'w' command ...")
                sp.run('w >> ' + self.storage_dir + '/login_user.txt', shell=True)

            if os.path.isfile(self.storage_dir + '/login_logout_user.txt') == False:
                print("Collecting login and logout information via 'last' command ...")
                sp.run('last >> ' + self.storage_dir + '/login_logout_user.txt', shell=True)

        except Exception as err:
            print(f"Error creating directory: {err}")
            return False

    def main(self):
        return self.find_user_inf()
        

if __name__ == '__main__':
    forensic_project().main()


# parser = argparse.ArgumentParser()
# parser.add_argument('-a', '--application', type = str, required = True, help = 'application name')
# parser.add_argument('-t', '--datetime', type=str, help = 'format: YYYY-mm-ddTHH:MM:SS')
# parser.add_argument('-d', '--destination', type=str, help = 'alpha or real')
# args = parser.parse_args() # 입력받은 인자값을 args에 저장
# result = sp.getoutput(f"ps -ef")
# print(f"{result}")
