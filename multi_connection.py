import threading

def multiple_connection(SSH, ip_list, credentials, config):
    thread = []
    for ip in ip_list:
        th = threading.Thread(target=SSH, args=(ip, credentials, config))
        th.start()
        thread.append(th)

    for th in thread:
        th.join()
