import subprocess
from turtle import color

def get_netpass():
    list_pass = []
    data = subprocess.check_output(['netsh', 'wlan', 'show', 'profiles']).decode('utf-8').split('\n')
    profiles = [i.split(":")[1][1:-1] for i in data if "All User Profile" in i]
    for i in profiles:
        results = subprocess.check_output(['netsh', 'wlan', 'show', 'profile', i, 'key=clear']).decode('utf-8').split('\n')
        results = [b.split(":")[1][1:-1] for b in results if "Key Content" in b]
        try:
            list_pass.append("{:<20}: {:<}".format(i, results[0]))
        except IndexError:
            list_pass.append("{:<20}: {:<}".format(i, ""))

    return list_pass

network_keys = get_netpass()

if network_keys:
    for i in network_keys:
        print(i[:21] + '\33[32m' + i[21:] + '\33[32m' + '\33[37m')

else:
    print('\33[31m' + 'NETWORKS NOT AVAILABLE' + '\33[31m')

