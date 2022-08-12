import argparse
from argparse import ArgumentParser
import os
import subprocess as sp
import User_info

#VOLATILITY = args.volpath #dest
#source_image = args.filename
#profile = args.profile

parser = argparse.ArgumentParser(description="Automatically collect Linux artifacts script")
#parser.add_argument('-p', '--process', dest = 'process', action = 'store_true', required = True, help = 'Collecting data about process')
#parser.add_argument('-n', '--network', dest = 'network', action = 'store_true', required = True, help = 'Collecting data about network')
#parser.add_argument('-s', '--system', dest = 'system', action = 'store_true', required = True, help = 'Collecting data about system')
#parser.add_argument('-f', '--file', dest = 'file', action = 'store_true', required = True, help = 'Collecting data about file')
parser.add_argument('-u', '--user', dest = 'user', action = 'store_true', help = 'Collecting data about user')

args = parser.parse_args() # 입력받은 인자값을 args에 저장
sp.run('python3 User_info.py', shell=True)
