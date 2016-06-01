#!/usr/bin/Python
# coding=utf-8
# sftp.py

# 测试SFTP上传功能, OK,
import paramiko
import os

t = paramiko.Transport("114.215.150.46", 22)
t.connect(username="root", password="0okmnji9Uzi")

sftp = paramiko.SFTPClient.from_transport(t)

remotepath = '/home/test/autopep8.zip'
localpath = 'c:\\users\\hdh\\autopep8.zip'
sftp.put(localpath, remotepath)
t.close()
