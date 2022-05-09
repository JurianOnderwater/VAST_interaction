import os
from datastructures import circularBuffer
from connect_to_server import connect, set_credentials, delete_credentials
import paramiko

class Send:
    """
    Transfers files to remote server.\n
    Connects to remote server using SSH with the paramiko module for python.\n
    When initialising you need to pass a circularBuffer object as argument.
    
    --------
    # Functions:
    - set_destination: Sets the path to where the files are transferred.
    - print_destination:
    - transfer_file:
    """
    def __init__(self, buffer: circularBuffer) -> None:
        self.buffer = buffer
        self.host = None
        self.port = None
        self.destination = None
        self.username,self.password = set_credentials()                                         # Take user input as username and password
        self.ssh = connect(hostname=self.host, username=self.username, password=self.password)
        delete_credentials(self.username, self.password)                                        # Prevents user credentials from being saved

    def set_destination(self, path: str) -> None:
        """
        Sets the path to where the files are transferred.
        """
        if (path is not None):
            self.destination = path
        else:
            raise NameError('You did not specify a pathname :(')

    def print_destination(self):
        if (self.destination is not None):
            print(self.destination)
        else:
            raise NameError('Oops, you did not yet set a destination folder!')

    def transfer_file(self, buffer: circularBuffer) -> None:
        if (self.remote is not None):
            file = buffer.dequeue()
            self.ftp_client= self.ssh.open_sftp()
            self.ftp_client.put(localpath=file,remotefilepath=self.destination)
            print(f'Transferred {file} to {self.destination}')
            self.ftp_client.close() 
            os.remove(file)                                     