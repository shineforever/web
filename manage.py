#!/usr/bin/env python
#coding:utf-8
import os
import sys
import socket

if __name__ == "__main__":
    """
    配置两种环境中setting文件，自动匹配;
    """
    if socket.gethostname() == 'guolt-pythoner':
        os.environ.setdefault("DJANGO_SETTINGS_MODULE", "web.settings_pythoner")

        from django.core.management import execute_from_command_line

        execute_from_command_line(sys.argv)
    else:
        os.environ.setdefault("DJANGO_SETTINGS_MODULE", "web.settings")

        from django.core.management import execute_from_command_line

        execute_from_command_line(sys.argv)
        
