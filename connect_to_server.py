import paramiko

def set_credentials():
    username = input("Username:")
    password = input("Password:")
    return [username, password]

def delete_credentials(username, password):
    username, password = None, None

def connect(hostname: str, username: str, password: str):
    """
    Connects to a remote server using paramiko.
    """
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh.connect(hostname=hostname, username=username, password=password)
    return ssh
