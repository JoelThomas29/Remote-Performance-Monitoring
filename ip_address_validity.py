""" This program check the validity of the ip address """

import sys

def ip_address_validity(ip_list):
    for ip in ip_list:
        ip = ip.rstrip("\n") # Removing next line character in every list index, obtained from readlines
        digits = ip.split(".") # splitting each address to verify is usability

        # Checking with the criteria if the address is of the right format
        if ( (len(digits) == 4) and (1 <= int(digits[0]) <= 223) and (int(digits[0]) != 127) and (int(digits[0]) != 169 or int(digits[1]) != 254) and (0 <= int(digits[1]) <= 255) and (0 <= int(digits[2]) <= 255) and (0 <= int(digits[3]) <= 255)):
            print("{} address validated\n".format(ip))
        else:
            print("Invalid IP address {} found in the file".format(ip))
            sys.exit()
