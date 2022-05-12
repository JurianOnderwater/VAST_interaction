import os
from time import sleep
from datastructures import circularBuffer

class Scan:
    """
    This class scans a folder for new files and queues them in a provided buffer object.

    --------
    ### Arguments:
    - buffer: circularBuffer - This is a bufferobject used for queueing the files
    - scanning_interval: float - This is the time interval on which the scanner scans the folder \b new files
    
    --------
    ### Functions:
    - set_origin(path: str): sets the folder to be scanned to path
    - set_destination(path: str): sets the folder where the files are transferred to path
    - print_origin(): prints the filepath to the origin folder
    - print_destination(): prints the filepath to the destination folder
    - scan_folder(): scans the origin folder and queues unqueued files for transfer.
    """
    def __init__(self, buffer: circularBuffer, scanning_interval: float = 0.1) -> None:
        self.origin = None
        self.destination  = None
        self.scanning_interval = scanning_interval
        self.buffer = buffer


    def set_origin(self, path: str) -> None:
        """
        Sets the origin folder filepath

        --------
        Arguments:
            path: str - filepath to the origin folder

        --------
        Raises:
            TypeError - When no path is provided
        """
        if (path is None):
            raise TypeError('You did not specify a pathname :(')
        else:
            self.origin = path

    def set_destination(self, path: str) -> None:
        """
        Sets the destination folder filepath

        --------
        Arguments:
            path: str - filepath to the origin folder

        --------
        Raises:
            TypeError - When no path is provided
        """
        if (path is None):
            raise TypeError('You did not specify a pathname :(')
        else:
            self.destination = path

    def print_origin(self) -> None:
        """
        Prints the origin folder filepath.

        --------
        Raises:
            NameError - When path is not set yet
        """
        if (self.origin is None):
            raise NameError('Oops, you did not yet set a folder to be scanned!')
        else:
            print(f"Origin folder is {self.origin}")            


    def print_destination(self) -> None:
        """
        Prints the destination folder filepath.

        --------
        Raises:
            NameError - When path is not set yet
        """
        if (self.destination is None):
            raise NameError('Oops, you did not yet set a destination folder!')
        else:
            print(self.destination)


    def scan_folder(self) -> None:
        """
        Scans the origin folder and queues unqueued files for transfer.

        --------
        Raises:
            NameError - When path is not set yet
        """
        if (self.origin is None):
            raise NameError("You didn't specify an origin folder!")
        else:
            print(os.listdir(self.origin))
            while True:
                for file in os.listdir(self.origin):            # Check if this function does what it seems to do
                    if file not in self.buffer.queue:
                        if file != '.DS_Store':                 # MacOS specific thingy
                            self.buffer.enqueue(file)
                            print(self.buffer.queue)       
                    sleep(self.scanning_interval)

        