#!/usr/bin/env python3
import sys
import subprocess
from tabulate import tabulate
import json
import os
from os import system, name, remove

def clear():
    if name == 'nt':
        _ = system('cls')
    else:
        _ = system('clear')

clear()

print('\n')
instance_id=input('Enter your EC2 Instance Id (* for all): ')
print('\n')
    
cmd="aws lambda invoke --cli-binary-format raw-in-base64-out --function-name ec2_Function --payload \'{ \"Instance\":\"" + instance_id + "\"}\' response.json"
subprocess.call(cmd, shell=True)
file =  open('response.json',)
dict = json.load(file)
last_element = dict.pop()
if last_element =="Invalid or Inexistent Instance Id":
  print('\n')
  print(last_element)
  print('\n')
else:  
  print('\n')
  print(tabulate(dict, headers=["Instance Id", "Instance Type", "State", "Private IP", "Public IP","Disk(s) Size (GB)"]))
  print('\n')
  print('Total disk size (GB): ' + str(last_element))
  print('\n')
file.close()
os.remove("response.json")
