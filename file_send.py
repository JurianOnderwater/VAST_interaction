import os
from datastructures import circularBuffer
from connect_to_server import connect
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
        self.username = None
        self.password = None
        self.destination = None
        self.ssh = connect(hostname=self.host, username=self.username, password=self.password)

    def set_destination(self, path: str):
        """
        Sets the path to where the files are transferred.
        """
        if (path is not None):
            self.destination = path
        else:
            raise NameError('You did not specify a pathname :(')

    def transfer_file(self, buffer) -> None:
        # check buffer for file to transfer at index = head
        if (self.remote is not None):
            file = buffer.dequeue()
            self.ftp_client= self.ssh.open_sftp()
            self.ftp_client.put(localpath=file,remotefilepath=self.destination)
            self.ftp_client.close() 
            os.remove(file)                                     
        # delete file from folder when it is transferred
        # dequeue file
        # raise NotImplementedError('This function has not been implemented yet, dumbass')