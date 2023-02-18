#!/usr/bin/env bash

sed -i "s/cn.archive.ubuntu.com/mirrors.tuna.tsinghua.edu.cn/g" /etc/apt/sources.list
apt update -y
apt upgrade -y
apt install nginx -y
apt install etcd -y
apt install rabbitmq-server

wget https://fastdl.mongodb.org/linux/mongodb-linux-x86_64-ubuntu2204-6.0.4.tgz
wget https://downloads.mongodb.com/compass/mongodb-mongosh_1.6.2_amd64.deb
wget https://fastdl.mongodb.org/tools/db/mongodb-database-tools-ubuntu2204-x86_64-100.6.1.deb

apt install ./mongodb-mongosh_1.6.2_amd64.deb
apt install ./mongodb-database-tools-ubuntu2204-x86_64-100.6.1.deb
rm -rf ./mongodb-database-tools-ubuntu2204-x86_64-100.6.1.deb ./mongodb-mongosh_1.6.2_amd64.deb

tar -xvf mongodb-linux-x86_64-ubuntu2204-6.0.4.tgz
mkdir -p /opt/mongodb
mv mongodb-linux-x86_64-ubuntu2204-6.0.4 /opt/mongodb

echo "
processManagement:
   fork: true
net:
   bindIp: 0.0.0.0
   port: 27017

systemLog:
   destination: file
   path: "/var/log/mongodb/mongod.log"
   logAppend: true

storage:
   dbPath: /var/lib/mongodb
   journal:
      enabled: true" > /etc/mongod.conf

mkdir -p /var/lib/mongo
mkdir -p /var/lib/mongodb

echo "
[Unit]
Description=Mongodb Server
After=network.target

[Service]
ExecStart=/opt/mongodb/bin/mongod -f /etc/mongodb.conf
ExecStop=/opt/mongodb/bin/mongod -f /etc/mongodb.conf --shutdown
Type=forking

[Install]
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
