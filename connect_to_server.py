import paramiko

def set_credentials():
    username = input("Username:")
    password = input("Password:")
    return [username, password]

def delete_credentials(username, password):
    username, password = None, None
    pass

def connect(hostname: str, username: str, password: str):
    """
    Connects to a remote server using paramiko.

    --------
    ### Arguments:
    - `hostname: str` - The hostname of the server you are connecting to.
    - `username: str` - The username you are using to log into the server.
    - `password: str` - The password you are using to log into the server

    --------
    #### Returns:
    - A paramiko `SSHClient` object that has been connected to.
    """
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh.connect(hostname=hostname, username=username, password=password)
    return ssh
