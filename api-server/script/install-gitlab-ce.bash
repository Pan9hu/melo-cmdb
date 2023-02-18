#!/usr/bin/env bash


sed -i "s/cn.archive.ubuntu.com/mirrors.tuna.tsinghua.edu.cn/g" /etc/apt/sources.list
curl https://packages.gitlab.com/gpg.key 2> /dev/null | sudo apt-key add - &>/dev/null
echo "deb https://mirrors.tuna.tsinghua.edu.cn/gitlab-ce/ubuntu jammy main" > /etc/apt/sources.list.d/gitlab-ce.list

apt update
sudo locale-gen en_US.UTF-8
localectl set-locale LANG=en_US.UTF-8
apt install gitlab-ce -y
gitlab-ctl reconfigure
