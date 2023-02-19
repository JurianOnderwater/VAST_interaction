from file_sharing.scan_folder import Scan
from file_sharing.file_send import Send
from file_sharing.connect_to_server import *
from file_sharing.datastructures import *
from threading import Thread
# from multiprocessing import Process


class Transfer:
    def __init__(self) -> None:
        ######################################################################
        # Scanpath and sendpath should always end with the same folder name! #
        # Otherwise shit breaks cause Paramiko is dumb                       #
        ######################################################################
        self.scanpath = r"\test"                                # Windows
        self.sendpath = "/webhome/s2649438/public_html/test"    # Linux

        self.buffer = fifoBuffer(max_size=5)
        self.scanner = Scan(buffer=self.buffer)
        self.sender = Send(buffer=self.buffer, testing=True)
        print('Transfer initiated')

    def transfer(self):
        '''
        Starts up a `Send` and `Scan` thread
        
        '''
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

        
