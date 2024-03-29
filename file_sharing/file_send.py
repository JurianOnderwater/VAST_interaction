import os
from file_sharing.datastructures import *
from file_sharing.connect_to_server import connect, set_credentials, delete_credentials
from time import sleep
# from typing import Type # might need for typing with subclasses.

class Send:
    """
    Transfers files to remote server.\n
    Connects to remote server using SSH using the paramiko module for python.\n
    When initialising you need to pass a circularBuffer object as argument.

    --------
    ### Arguments:
    - `buffer (circularBuffer)` - This is a bufferobject used for dequeueing the files and send them
    --------
    ### Functions:
    - `set_destination(path: str)`: Sets the path to where the files are transferred.
    - `print_destination()`: Prints the filepath to the destination folder on the server
    - `transfer_file()`:
    """

    
    def __init__(self, buffer, LLSC: bool) -> None: # check if buffer here also works for classes that inherint from buffer
        self.buffer = buffer
        # self.host = None
        # self.port = None
        self.destination = None
        if LLSC:
            self.ssh = connect(hostname='change_to_actual_hostname', username='change_to_actual_username', password='change_to_actual_password')
        else:
            self.hostname, self.username,self.password = set_credentials()                                         # Take user input as username and password
            self.ssh = connect(hostname=self.hostname, username=self.username, password=self.password)
            delete_credentials(self.hostname, self.username, self.password)                                        # Prevents user credentials from being saved


    def set_destination(self, path: str) -> None:
        """
        Sets the destination folder filepath

        --------
        Arguments:
            `path (str)` - filepath to the origin folder

        --------
        Raises:
            `TypeError` - When no path is provided
        """
        self.destination = path

    def print_destination(self):
        """
        Prints the destination folder filepath.

        --------
        Raises:
            `NameError` - When path is not set yet
        """
        if (self.destination is None):
            raise NameError('Oops, you did not yet set a destination folder!')            
        else:
            print(self.destination)

    def transfer_files(self) -> None:
        """
        Transfers queued files to the remote server destination folder.\n
        The file transfer protocol is opened, the file transferred, and the\n
        transfer protocol closed again.\n 
        The file is deleted from the origin folder.

        --------
        Raises:
            `NameError` - When path is not set yet
        """
        print('TRANSFER FILES IS CALLED')
        sleep(0.2)
        if (self.destination is None):
            raise NameError('The destination folder has not yet been set!')
        else:
            self.ftp_client = self.ssh.open_sftp()
            while self.buffer.size >= 1:
                file = self.buffer.dequeue()
                remotepath = self.destination + '/' + file

                file = "C:/test/" + file
                try:
                    self.ftp_client.put(localpath=file,remotepath=remotepath, confirm=True)
                    print(f'Transferred {file} to {self.destination}')
                    os.remove(file)  
                except FileNotFoundError:
                    pass
            self.ftp_client.close()
            self.buffer.__init__()     

    # def transfer_files_2(self, file) -> None:
    #     """
    #     Transfers queued files to the remote server destination folder.\n
    #     The file transfer protocol is opened, the file transferred, and the\n
    #     transfer protocol closed again.\n 
    #     The file is deleted from the origin folder.

    #     --------
    #     Raises:
    #         `NameError` - When path is not set yet
    #     """
    #     print('TRANSFER FILE IS CALLED')
    #     sleep(0.2)
    #     if (self.destination is None):
    #         raise NameError('The destination folder has not yet been set!')
    #     else:
    #         self.ftp_client = self.ssh.open_sftp()
            
            # remotepath = self.destination + '/' + file
            # # file = 'test/' + file
            # try:
            #     self.ftp_client.put(localpath=file,remotepath=remotepath, confirm=True)
            #     os.remove(file)
            # except FileNotFoundError:
            #     pass
            # print(f'Transferred {file} to {self.destination}')  
            # self.ftp_client.close()                           