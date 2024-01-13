
#!/bin/bash

RemoteServerName=meowserver

#setting HostName 
hostnamectl set-hostname meowclient
bash

#yum update -y
yum install -y httpd
systemctl start httpd.service
systemctl enable httpd.service
echo “Hello World from $(hostname)” > /var/www/html/index.html


#-----------------------------------------------------

#DNS cache
echo "Input TargetServerIP:"
read ServerIP
echo "$ServerIP meowserver" >> /etc/hosts

#-------------------------------------------

#Automaticlly
yum install expect -y
#----------------------------------------------------
#Task 3 NFS client 

cd /home/user/Desktop/LinuxScript
chmod +x *.exp

yum install -y nfs-utils 
systemctl start rpcbind && systemctl start nfs

echo "check Remote NFS folder"
read remoteNfs
showmount -e $remoteNfs

mkdir /home/user/nfsmount
mount -t nfs $remoteNfs:/home/user/nfsServer /home/user/nfsmount

#-----------------------
#echo server(client)
nc $RemoteServerName 9000 

#----------------
#FTP client 　(Download File！)

sudo yum install -y ftp
ftp $RemoteServerName -u user 

FTP_SERVER=$RemoteServerName
FTP_USER="user"
FTP_PASSWORD="user"

ftp -n $FTP_SERVER <<END_SCRIPT
quote USER $FTP_USER
quote PASS $FTP_PASSWORD
cd ./ftpserver/
bin
prompt
mget *.txt
bye
END_SCRIPT

# client upload

cd $initialdirectory
mkdir "$initialdirectory/ftpClient" && cd ./ftpClient
touch {1..4}.txt

ftp -n $FTP_SERVER <<END_SCRIPT
quote USER $FTP_USER
quote PASS $FTP_PASSWORD
cd ./ftpClient/
bin
prompt
mput *.txt
END_SCRIPT
#done

#-----------------------------------------------------------

#Telnet client 
telnetUser="user"
TelnetPassword="user"


yum install -y telnet
yum install -y xinetd
systemctl start telnet.socket
systemctl start xinetd

expect -f telnetAutoLogin.exp

#localIP=$(ip addr show ens33 | grep 'inet ' | awk '{print $2}' | cut -d'/' -f1)