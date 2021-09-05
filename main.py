#!/usr/bin/env python3
import boto3
import sys
from tabulate import tabulate
from os import system, name

def clear():
    if name == 'nt':
        _ = system('cls')
    else:
        _ = system('clear')

clear()

print("------------------------------------------------------------------------------")
print("-This script get info about EC2 instances and present them in a table format.-")
print("------------------------------------------------------------------------------")
print('\n')
profile  = input('Please provide aws profile: ')
print('\n')
try:
    aws_mag_con=boto3.session.Session(profile_name=profile)
    ec2_con_cli=aws_mag_con.client(service_name="ec2")
except:
    print("Invalid profile. Please check your profile before execute again.")
    sys.exit()

while True:
    print("""

		1. Press one to enter instance(s)
		2. Exit

""")
    opt=int(input('Enter your option: '))
    if opt==1:
        instance_id=input('Enter your EC2 Instance Id (* for all): ')
        if instance_id == '*' :
            response = ec2_con_cli.describe_instances()                
            for reservation in response['Reservations']:
                 list_a = []
                 total_v = 0
                 for instance in reservation['Instances']:
                      volumes = ec2_con_cli.describe_volumes(
                             Filters=[
                                         {'Name':'attachment.instance-id',
                                        'Values':[instance['InstanceId']],
                                            }
                                          ]
                                    )
                      sum_ds = 0
                      for disk in volumes['Volumes']:
                         sum_ds = sum_ds + disk['Size']
                         #table.add.row(instance['InstanceId'], instance['InstanceType'],instance['State']['Name'],instance['PrivateIpAddress'],instance['PublicIpAddress'],sum_ds) 
                      list_a.append([instance['InstanceId'], instance['InstanceType'],instance['State']['Name'],instance['PrivateIpAddress'],instance['PublicIpAddress'],sum_ds])
                      total_v = total_v + sum_ds
                      #list_a.sort(reverse=True, key=lambda x: x[5])
                 clear()
                 print(tabulate(list_a, headers=["Instance Id", "Instance Type", "State", "Private IP", "Public IP","Disk(s) Size (GB)"]))
                 print('\n')
                 print('Total instances disk size (GB): '+ str(total_v))

        else:
            try:
               response = ec2_con_cli.describe_instances(InstanceIds=[instance_id])                
               for reservation in response['Reservations']:
                 list_a = []
                 total_v = 0
                 for instance in reservation['Instances']:
                            volumes = ec2_con_cli.describe_volumes(
                                Filters=[
                                            {'Name':'attachment.instance-id',
                                            'Values':[instance['InstanceId']],
                                                }
                                            ]
                                        )
                 sum_ds = 0
                 for disk in volumes['Volumes']:
                   sum_ds = sum_ds + disk['Size']

                   list_a.append([instance['InstanceId'], instance['InstanceType'],instance['State']['Name'],instance['PrivateIpAddress'],instance['PublicIpAddress'],sum_ds])
                   total_v = total_v + sum_ds
                 list_a.sort(reverse=True, key=lambda x: x[5])
               clear()
               print(tabulate(list_a, headers=["Instance Id", "Instance Type", "State", "Private IP", "Public IP","Disk(s) Size (GB)"]))
               print('\n')
               print('Total instances disk size (GB): '+ str(total_v))
            except:
                print('Instance not found. Thank you for using this script')
                sys.exit()

    elif opt==2:
            print("Thank you for using this script")
            sys.exit()
    else:
        print("Your option is invalid. Please try once again")


