from scan_folder import Scan
from file_send import Send
from connect_to_server import *
from datastructures import *
from threading import Thread


class Transfer:
    def __init__(self) -> None:
        self.scanpath = r"\test" # Windows
        self.sendpath = "/webhome/s2649438/public_html/test" # Linux

        self.buffer = timedBuffer(max_size=20)
        self.scanner = Scan(buffer=self.buffer)
        self.sender = Send(buffer=self.buffer, testing=True)

    def transfer(self):
        self.scanner.set_origin(path=self.scanpath)
        self.scanner.print_origin()
        self.sender.set_destination(path=self.sendpath)
        scanning_thread    = Thread(target = self.scanner.scan_folder())
        sending_thread     = Thread(target = self.sender.transfer_files())
        scanning_thread.start()
        sending_thread.start()
