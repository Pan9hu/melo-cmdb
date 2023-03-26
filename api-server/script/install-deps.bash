#!/usr/bin/env bash

sed -i "s/cn.archive.ubuntu.com/mirrors.tuna.tsinghua.edu.cn/g" /etc/apt/sources.list
<<<<<<< HEAD

apt update
apt upgrade -y
=======
apt update -y
apt upgrade -y
apt install nginx -y
apt install etcd -y
apt install rabbitmq-server
>>>>>>> 73ae8ef755d9614cf9f8337c6ba2a01e013f8f3b

wget https://fastdl.mongodb.org/linux/mongodb-linux-x86_64-ubuntu2204-6.0.4.tgz
wget https://downloads.mongodb.com/compass/mongodb-mongosh_1.6.2_amd64.deb
wget https://fastdl.mongodb.org/tools/db/mongodb-database-tools-ubuntu2204-x86_64-100.6.1.deb

apt install ./mongodb-mongosh_1.6.2_amd64.deb
apt install ./mongodb-database-tools-ubuntu2204-x86_64-100.6.1.deb
<<<<<<< HEAD
rm -rf ./mongodb-mongosh_1.6.2_amd64.deb ./mongodb-database-tools-ubuntu2204-x86_64-100.6.1.deb

tar -xvf mongodb-linux-x86_64-ubuntu2204-6.0.4.tgz
=======
rm -rf ./mongodb-database-tools-ubuntu2204-x86_64-100.6.1.deb ./mongodb-mongosh_1.6.2_amd64.deb

tar -xvf mongodb-linux-x86_64-ubuntu2204-6.0.4.tgz
mkdir -p /opt/mongodb
>>>>>>> 73ae8ef755d9614cf9f8337c6ba2a01e013f8f3b
mv mongodb-linux-x86_64-ubuntu2204-6.0.4 /opt/mongodb

echo "
processManagement:
   fork: true
net:
   bindIp: 0.0.0.0
   port: 27017
<<<<<<< HEAD
storage:
   dbPath: /var/lib/mongo
=======

>>>>>>> 73ae8ef755d9614cf9f8337c6ba2a01e013f8f3b
systemLog:
   destination: file
   path: "/var/log/mongodb/mongod.log"
   logAppend: true
<<<<<<< HEAD
storage:
=======

storage:
   dbPath: /var/lib/mongodb
>>>>>>> 73ae8ef755d9614cf9f8337c6ba2a01e013f8f3b
   journal:
      enabled: true" > /etc/mongod.conf

mkdir -p /var/lib/mongo
<<<<<<< HEAD
mkdir -p /var/log/mongodb

echo "
[Unit]
Description=MongoDB Server
=======
mkdir -p /var/lib/mongodb

echo "
[Unit]
Description=Mongodb Server
>>>>>>> 73ae8ef755d9614cf9f8337c6ba2a01e013f8f3b
After=network.target

[Service]
ExecStart=/opt/mongodb/bin/mongod -f /etc/mongodb.conf
ExecStop=/opt/mongodb/bin/mongod -f /etc/mongodb.conf --shutdown
Type=forking

[Install]
<<<<<<< HEAD
WantedBy=multi-user.target" > /lib/systemd/system/mongod.service

systemctl daemon-reload
systemctl enable mongod
systemctl start mongod

apt install git -y
apt install nginx -y
apt install etcd -y
apt install rabbitmq-server -y
apt install gitlab-ce

systemctl enable nginx
systemctl enable etcd
systemctl enable rabbitmq-server

systemctl start nginx
systemctl start etcd
systemctl start rabbitmq-server

rabbitmq-plugins enable rabbitmq_management
=======
WantedBy=multi-usr.target" > /lib/systemd/system/mongod.service

systemctl daemon-reload
systemctl enabled --now mongod


rabbitmq-plugins enable  rabbitmq_management
rabbitmqctl add_user admin admin
rabbitmqctl set_user_tags admin
rabbitmqctl set_user_tags admin administrator
#rabbitmqctl set_permissions -p "/" admin ".*" ".*" ".*"

systemctl daemon-reload
systemctl enabled --now mongod
systemctl enable --now nginx
systemctl enable --now  rabbitmq-server
systemctl enable --now etcd
>>>>>>> 73ae8ef755d9614cf9f8337c6ba2a01e013f8f3b
