# /usr/bin/Python
# -*- coding = utf-8 -*-
# config.py

# 调试config模块功能

import configparser

cf = configparser.ConfigParser()  # 这里大小写要注意,否则通不过
cf.read("C:\\Work\\Joseph\\deploy\\config.ini")

host = cf.get("server", "host")
port = int(cf.get("server", "port"))
user = cf.get("server", "user")
passwd = cf.get("server", "passwd")
local_path = cf.get("path", "local_path")
project_path = cf.get("path", "project_path")
server_path = cf.get("path", "server_path")


print(host, port, user, passwd, local_path, project_path, server_path)
