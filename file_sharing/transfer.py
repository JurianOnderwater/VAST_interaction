from file_sharing.scan_folder import Scan
from file_sharing.file_send import Send
from file_sharing.connect_to_server import *
from file_sharing.datastructures import *
from threading import Thread
from multiprocessing import Process


class Transfer:
    def __init__(self) -> None:
        self.scanpath = r"\test"                                # Windows
        self.sendpath = "/webhome/s2649438/public_html/test"    # Linux

        self.buffer = randomBuffer(max_size=4)
        self.scanner = Scan(buffer=self.buffer)
        self.sender = Send(buffer=self.buffer, testing=True)
        print('Transfer initiated')

    def transfer(self):
        print('transferer called')
        self.scanner.set_origin(path=self.scanpath)
        self.scanner.print_origin()
        self.sender.set_destination(path=self.sendpath)
        scanning_thread = Thread(target = self.scanner.scan_folder())
        scanning_thread.start()
        sending_thread  = Thread(target = self.sender.transfer_files())
        sending_thread.start()
        scanning_thread.join()
        sending_thread.join()

    # def func1(self):
    #     self.scanner.set_origin(path=self.scanpath)
    #     self.scanner.scan_folder()
    #     sleep(0.1)

    # def func2(self):
    #     self.sender.set_destination(path=self.sendpath)
    #     self.sender.transfer_files()
    #     sleep(0.1)


    # def main(self):
    #     print(" script started")
    #     print(1)
    #     p1 = Process(target=self.func1())
    #     print(2)
    #     p1.start()
    #     print(3)
    #     p2 = Process(target=self.func2)
    #     print(4)
    #     p2.start()
    #     print(5)
    #     p1.join()
    #     p2.join()
    #     print (" over")
        
