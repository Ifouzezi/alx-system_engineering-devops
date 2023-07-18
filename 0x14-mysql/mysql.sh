#!/usr/bin/env bash

sudo apt update
sudo apt install mysql-server-5.7
sudo systemctl start mysql
sudo systemctl enable mysql
sudo mysql_secure_installation
