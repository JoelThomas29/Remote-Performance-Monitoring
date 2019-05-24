"""This program handles the connection to a remote device and reads/writes configurations"""

import time
import paramiko
import re
from All_Files_Validation import loading_feature as load

def SSH(ip,credentials,config):

    try:
        # Extracting user credentials
        username = credentials[0].rstrip('\n')
        password = credentials[1].rstrip('\n')

        # Creating an SSH session
        session = paramiko.SSHClient()
        session.set_missing_host_key_policy(paramiko.AutoAddPolicy())

        # Authenticating with the credentials to the IP address provided
        session.connect(ip.rstrip('\n'), username= username, password= password)

        # Invoking shell on the router
        connection = session.invoke_shell()

        # Disable pagination
        connection.send('enable\n')
        connection.send('terminal length 0\n')
        time.sleep(1)

        # Interacting with the command file and the invoked shell
        for line in config:
            connection.send(line)
            time.sleep(1)

        # Reading the shell output
        output = connection.recv(65535)

        # Finding the required info using regex in the output
        cpu = re.search(b"CPU utilization for five seconds: (\d+)", output)

        # Writing filtered output to a file
        with open('config_output.txt', 'a') as write_file:
            write_file.write(cpu.group(1).decode('utf-8'))
            write_file.write("\n")
            write_file.close()

        # Checking for Syntax errors
        if re.search(b"% Invalid input", output):
            print("\nThere was some syntax error on {}".format(ip))
        else:
            print("Completed for {}".format(ip))

        # Closing the session
        session.close()

    except paramiko.AuthenticationException:
        print("Authentication problem - ", flush=True)
        time.sleep(0.5)
        print("Check username and password\n")
        print("Exiting the program", flush=True)
        load()
