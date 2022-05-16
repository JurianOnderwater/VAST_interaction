from scan_folder import Scan
from file_send import Send
from connect_to_server import *
from datastructures import circularBuffer
import threading
from threading import Thread, enumerate


if __name__ == '__main__':
    buffer = circularBuffer()

    scanner = Scan(buffer=buffer)
    sender = Send(buffer=buffer)
    scanner.set_origin('test')
    sender.set_destination()
    Thread(target = scanner.scan_folder()).start()
    Thread(target = sender.transfer_files()).start()
    for thread in threading.enumerate(): 
        print(thread.name)
