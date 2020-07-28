import os, datetime, pyminizip, paramiko 
now = datetime.datetime.now()
date=now.strftime("%Y%m%d")
password=now.strftime("P@ssw0rd%Y%m%dpleaseEnter") #Пароль со своей фразой
os.chdir('d:\TMP')
compression_level = 5
pyminizip.compress("d:\TMP\file.xxx", "", "TMP"+ date +".zip", password, compression_level)
zipfile="TMP"+ date +".zip"
ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh.connect('ip', username="user", password="pass")
sftp = ssh.open_sftp()
localpath = "TMP"+ date +".zip"
remotepath= '/remdir/' +zipfile+''
sftp.put(zipfile, remotepath)
sftp.close()
ssh.close()
os.remove(zipfile)