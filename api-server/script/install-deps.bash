#!/usr/bin/env bash

sed -i "s/cn.archive.ubuntu.com/mirrors.tuna.tsinghua.edu.cn/g" /etc/apt/sources.list

apt update
apt upgrade -y

wget https://fastdl.mongodb.org/linux/mongodb-linux-x86_64-ubuntu2204-6.0.4.tgz
wget https://downloads.mongodb.com/compass/mongodb-mongosh_1.6.2_amd64.deb
wget https://fastdl.mongodb.org/tools/db/mongodb-database-tools-ubuntu2204-x86_64-100.6.1.deb

apt install ./mongodb-mongosh_1.6.2_amd64.deb
apt install ./mongodb-database-tools-ubuntu2204-x86_64-100.6.1.deb
rm -rf ./mongodb-mongosh_1.6.2_amd64.deb ./mongodb-database-tools-ubuntu2204-x86_64-100.6.1.deb

tar -xvf mongodb-linux-x86_64-ubuntu2204-6.0.4.tgz
mv mongodb-linux-x86_64-ubuntu2204-6.0.4 /opt/mongodb

echo "
processManagement:
   fork: true
net:
   bindIp: 0.0.0.0
   port: 27017
storage:
   dbPath: /var/lib/mongo
systemLog:
   destination: file
   path: "/var/log/mongodb/mongod.log"
   logAppend: true
storage:
   journal:
      enabled: true" > /etc/mongod.conf

mkdir -p /var/lib/mongo
mkdir -p /var/log/mongodb

echo "
[Unit]
Description=MongoDB Server
After=network.target

[Service]
ExecStart=/opt/mongodb/bin/mongod -f /etc/mongodb.conf
ExecStop=/opt/mongodb/bin/mongod -f /etc/mongodb.conf --shutdown
Type=forking

[Install]
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
