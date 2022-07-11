from scan_folder import Scan
from file_send import Send
from connect_to_server import *
from datastructures import *
from threading import Thread


if __name__ == '__main__':
    buffer = timedBuffer()

    scanner = Scan(buffer=buffer)
    sender = Send(buffer=buffer, testing=True)
    scanner.set_origin(path='test')
    sender.set_destination(path='/webhome/s2649438/public_html/test')
    scanning_thread = Thread(target = scanner.scan_folder)
    sending_thread  = Thread(target = sender.transfer_files)
    scanning_thread.start()
    sending_thread.start()
