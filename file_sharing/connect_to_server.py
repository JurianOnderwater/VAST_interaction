import paramiko

def set_credentials():
    hostname = str(input("Hostname:"))
    username = str(input("Username:"))
    password = str(input("Password:"))
    return [hostname,username, password]

def delete_credentials(hostname: str, username: str, password: str):
    '''
        Deletes credentials that are saved in the program.

        --------
        ### Arguments:
        - `hostname (str)` - The hostname of the server you are connecting to.
        - `username (str)` - The username you are using to log into the server.
        - `password (str)` - The password you are using to log into the server
        '''
    hostname, username, password = None, None, None

def connect(hostname: str, username: str, password: str):
    """
    Connects to a remote server using paramiko.

    --------
    ### Arguments:
    - `hostname (str)` - The hostname of the server you are connecting to.
    - `username (str)` - The username you are using to log into the server.
    - `password (str)` - The password you are using to log into the server

    --------
    #### Returns:
    - A paramiko `.SSHClient` object that has been connected to.
    """
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh.connect(hostname=hostname, username=username, password=password)
    return ssh
