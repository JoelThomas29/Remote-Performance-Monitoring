"""This program pings the ip adrees to check if its reachable or not"""

import sys
import subprocess

def ip_address_reachability(list):
    for ip in list:
        ip = ip.rstrip('\n')

        # Pinging the ip to know if its reachable
        call = subprocess.call('ping %s -n 2' % (ip), stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        if call == 0:
            print("\n {} is reachable".format(ip))
        else:
            print("\n {} not reachable".format(ip))
            sys.exit()

