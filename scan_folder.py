import os
from time import time, sleep
from datastructures import circularBuffer
from file_send import Send

class Scan:
    """
    Scans a folder for newly added files, moves them to a new local folder\n
    There is a possibility to immediately copy the new file to an alternate \n 
    folder that can be emptied during file transfer
    
    --------
    # Functions:
    - set_origin: sets the folder to be scanned to path
    - set_destination: sets the folder where the files are transferred to path
    - print_origin:
    - print_destination:
    - scan_folder:
    - send_file:
    - transferable_files: 


    """
    def __init__(self, buffer: circularBuffer) -> None:
        self.origin = None
        self.destination  = None
        self.some_delay = 0.2
        self.buffer = buffer

    def set_origin(self, path: str) -> None:
        """
        Sets the folder to be scanned to path
        """
        if (path is not None):
            self.origin = path
        else:
            raise NameError('You did not specify a pathname :(')

    def set_destination(self, path: str) -> None:
        """
        Sets the folder where the files are transferred to path
        """
        if (path is not None):
            self.destination = path
        else:
            raise NameError('You did not specify a pathname :(')

    def print_origin(self) -> None:
        if (self.origin is not None):
            print(f"Origin folder is {self.origin}")
        else:
            raise NameError('Oops, you did not yet set a folder to be scanned!')

    def print_destination(self) -> None:
        if (self.destination is not None):
            print(self.destination)
        else:
            raise NameError('Oops, you did not yet set a destination folder!')

    def scan_folder(self) -> None:
        """"""
        print(os.listdir(self.origin))
        while True:
            for file in os.listdir(self.origin):                                                 # Check if this function does what it seems to do
                if file not in self.buffer.queue:
                    if file != '.DS_Store':                 # MacOS specific thingy
                        self.buffer.enqueue(file)
                        print(self.buffer.queue)       
                sleep(self.some_delay)
            # raise NotImplementedError('This function has not been fully implemented yet, dumbass')


    def transferable_files(self) -> list:                                                   #probably not needed
        # self.buffer.display()
        return self.buffer.queue
        # raise NotImplementedError('This function has not been implemented yet, dumbass')

        