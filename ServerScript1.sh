#!/bin/bash

#using to locate Executing postions of script
initialdirectory=$(pwd)
ClientHostname=meowclient

#setting HostName 
hostnamectl set-hostname meowserver
bash

#yum update -y
yum install -y httpd
systemctl start httpd.service
systemctl enable httpd.service
echo “Hello World from $(hostname)” > /var/www/html/index.html

#---------------------

#DNS cache
echo "Input TargetClientIP:"

read ClientIP

echo "$ClientIP meowclient" >> /etc/hosts

#-----------------

#Automaticlly
yum install expect -y

#-------------------------------------------

cd /home/user/Desktop/LinuxScript
chmod +x *.exp

#SSH 
systemctl start sshd && systemctl enable sshd

#generate SSHkey !
expect -f keyGenAndSendkey.exp && echo "Auto login Finish!!"


#---------------------------------------------------------
#task 2  LAMP PHP

yum install -y mariadb-server mariadb && systemctl start mariadb
yum install -y php php-mysql php-fpm && systemctl restart httpd


expect -f mysqlSecureSetting.exp

#create database and insert Data
php dbSetting.php

# backend-php
mv ./meowdb.php /var/www/html


#----------------------------------------------------------------------
#Task 3 
#NFS server


yum install -y nfs-utils
systemctl start rpcbind
systemctl start nfs

mkdir -p /home/user/nfsServer
chmod 755 /home/user/nfsServer
sameLanIP=$(ip addr show ens33 | grep 'inet ' | awk '{split($2, a, "."); print a[1]"."a[2]"."a[3]".0"}')
echo "/home/user/nfsServer/ $sameLanIP/24(rw,sync,no_root_squash,no_all_squash)" >> /etc/exports
systemctl restart nfs && showmount -e localhost


#--------------------------------------------------------------
# Task 4 SAMBA

yum install samba samba-client samba-common -y
mkdir /home/user/sambaServer/
chown nobody /home/user/sambaServer/
sudo chmod 777 /home/user/sambaServer/


# SMB.conf
echo "[MeowHecker]" >> /etc/samba/smb.conf
echo -e "\tcomment = for MeowHecker" >> /etc/samba/smb.conf
echo -e "\tpath = /home/user/sambaServer/" >> /etc/samba/smb.conf
echo -e "\tread only = no" >> /etc/samba/smb.conf
echo -e "\tguest ok = yes" >> /etc/samba/smb.conf
echo -e "\tbrowseable = yes" >> /etc/samba/smb.conf
#Testing  restart SMB
echo -e '\r' | testparm && systemctl start smb
        
# Setting SMB user password (user:user)
expect -f smbpass.exp
#Windows \\192.168.87.134
        
#
#localIP=$(ip addr show ens33 | grep 'inet ' | awk '{print $2}' | cut -d'/' -f1)


#--------------------------


#httpd Access controll !

## White list (IP)

cd /var/www/html/ 
mkdir iplimit
cd /var/www/html/iplimit && echo "ipAccessControll" >> iplimit.html

# AllowOveride None -> All
allowOverrideLine=$(grep -n "AllowOverride None" /etc/httpd/conf/httpd.conf | sed -n '2s/:.*//p')
sed -i "${allowOverrideLine}s/AllowOverride None/AllowOverride All/" /etc/httpd/conf/httpd.conf

echo "Ip Allow White list(192.xxx.xxx.xxx):"
read ipAllow

echo "<Directory /var/www/html/iplimit>" >> /etc/httpd/conf/httpd.conf
echo -e "\tOrder deny,allow" >> /etc/httpd/conf/httpd.conf
echo -e "\tDeny from all" >> /etc/httpd/conf/httpd.conf
echo -e "\tAllow from $ipAllow" >> /etc/httpd/conf/httpd.conf
echo "</Directory>" >> /etc/httpd/conf/httpd.conf
systemctl reload httpd #Access Limit done 

##Directory Authentication 

cd /var/www/html/
mkdir authDir && cd ./authDir/
touch {a..d}.txt 

#Genearte (meowhecker:meowhecker)

expect -f httpdauthConf.exp
echo "AuthType Basic" >> /var/www/html/authDir/.htaccess
echo "AuthName 'Restricted Files'" >> /var/www/html/authDir/.htaccess
echo "AuthBasicProvider file" >> /var/www/html/authDir/.htaccess
echo "AuthUserFile /var/www/html/authDir/.htpasswd" >> /var/www/html/authDir/.htaccess
echo "Require user meowhecker" >> /var/www/html/authDir/.htaccess
systemctl reload httpd

#-------------------------------------------------------
# Running Echo server via systemctl 

yum install python3 -y

sudo chmod +x "$initialdirectory/echoserver.py"

#configure systemctl Configuration 
cd /etc/systemd/system

echo "[Unit]" >> /etc/systemd/system/echoserver.service
echo -e "Description=Echo Server\n" >> /etc/systemd/system/echoserver.service
echo "[Service]" >> /etc/systemd/system/echoserver.service
echo "Type=simple" >> /etc/systemd/system/echoserver.service
echo "ExecStart=$initialdirectory/echoserver.py" >> /etc/systemd/system/echoserver.service
echo -e "Restart=always\n" >> /etc/systemd/system/echoserver.service
echo "[Install]" >> /etc/systemd/system/echoserver.service
echo "WantedBy=multi-user.target" >> /etc/systemd/system/echoserver.service


chmod 644 /etc/systemd/system/echoserver.service

sudo systemctl daemon-reload
sudo systemctl start echoserver.service
sudo systemctl status echoserver.service

#--------------------------------------------------

yum install vsftpd -y 
systemctl start vsftpd

#Limit user cd other dirctory 
sed -i 's/^#chroot_local_user=YES/chroot_local_user=YES/' /etc/vsftpd/vsftpd.conf
sed -i '/^chroot_local_user=YES/a allow_writeable_chroot=YES' /etc/vsftpd/vsftpd.conf
systemctl restart vsftpd

mkdir "$initialdirectory/ftpserver" && cd "$initialdirectory/ftpserver"
touch {a..d}.txt



#-------------------------------
#Telnet

yum install -y telnet-server
yum install -y telnet
yum install -y xinetd
systemctl start telnet.socket
systemctl start xinetd


#------------------------------

#Network Manager -> Network 

networkConfigure="/etc/sysconfig/network-scripts/ifcfg-ens33"

systemctl stop NetworkManager
chkconfig network on
systemctl start network
ifconfig ens33 0
cd /etc/sysconfig/network-scripts/
rm ifcfg-* -f


cat << EOF > $networkConfigure
TYPE=Ethernet
DEVICE=ens33
ONBOOT=yes
BOOTPROTO=static
IPADDR=192.168.87.129
NETMASK=255.255.255.0
GATEWAY=192.168.87.2
EOF

systemctl restart network