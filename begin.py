#!C:/Python27/ArcGIS10.2/python.exe
#-*- coding:utf-8 -*-
"""
#============================================
#
# Project: mmanagecelery
# Name: The file name is begin
# Purpose: 
# Auther: Administrator
# Tel: 17372796660
#
#============================================
#
"""

import sys
from celery_app import clipfromsde




reload(sys)
sys.setdefaultencoding('utf8')


def begin():
    clipfromsde.clipfromsde.delay(6, 9)
    clipfromsde.clipfromsde.delay(6, 9)
    return True


if __name__ == "__main__":
    begin()