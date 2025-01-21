import os
import paramiko 
# pip install paramiko
# py -m pip install --upgrade pip
# py -m pip install paramiko


import datetime


def main():
    date = datetime.datetime.now().strftime("%Y-%m-%d")

    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh.connect(hostname='10.2.1.193', username="nvidia", password="nvidia")
    sftp = ssh.open_sftp()
    localpath = 'test.txt'
    Download_local_path = 'test_download.txt'
    remotepath = '/home/nvidia/Desktop/test.txt'
    #/home/nvidia/Desktop#

    #UpLoadFile( ssh, localpath, remotepath )
    DownLoadFile( ssh, Download_local_path, remotepath )
    
    ssh.close()


def UpLoadFile( ssh, localpath, remotepath ) :
    sftp = ssh.open_sftp()
    sftp.put(localpath, remotepath) # UpLoad File to remotePath
    sftp.close()


def DownLoadFile( ssh, localpath, remotepath ) :
    sftp = ssh.open_sftp()
    sftp.get(remotepath,localpath) # Download File to local
    sftp.close()    

if __name__ == '__main__':
    main()
