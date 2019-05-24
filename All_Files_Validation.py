"""This program checks the validity of the ip file provided by the user"""

import os.path
import sys
import time

count = 0

def loading_feature():
    for i in range(3):
        print(".", end=' ', flush=True)
        time.sleep(0.5)
    print("")

def terminate():
    global count
    count += 1
    if count == 3:
        print("Invalid entry exhausted")
        time.sleep(0.5)
        print("Exiting the program")
        sys.exit()
    else:
        return print("You have {} retry(s) left\n".format(3-count))

def file_validity():
    global count
    files_mapping = {'IP': '', 'Credentials': '', 'Command': ''}

    loading_feature()

    for item in files_mapping:
        def user_input():
            file = input("\nPlease enter a file that contains {}\n"
                            "(Enter the full path) : ".format(item))

            if os.path.isfile(file) == True:
                print("{} file found and validated".format(item), flush=True)
                loading_feature()

                # Open validated file
                read_file = open(file, 'r')

                # Start at the beginning
                read_file.seek(0)

                # Reading lines
                output = read_file.readlines()

                # Closing the file
                read_file.close()

                files_mapping[item] = output

            else:
                print("File not found ", flush=True)
                loading_feature()
                terminate()
                return user_input()

        user_input()
    return files_mapping
