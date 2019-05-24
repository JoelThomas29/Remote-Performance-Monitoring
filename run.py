""" Run this program to start the application """

from All_Files_Validation import file_validity
from ip_address_validity import ip_address_validity
from ip_address_reachability import ip_address_reachability
from multi_connection import multiple_connection
from SSH_connection import SSH
import time

try:
    # Requesting all files
    all_files = file_validity()

    # IP address validation
    ip_address_validity(all_files['IP'])

    # IP address reachability
    ip_address_reachability(all_files['IP'])

    while True:
        # Calling all routers for reading/writing configurations
        multiple_connection(SSH, all_files['IP'], all_files['Credentials'], all_files['Command'])

        # Hold timer for the next poll
        time.sleep(5)
    # fin
except KeyboardInterrupt:
    print("Interrupted by user\nExiting program")
