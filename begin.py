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
    MEDIA=u"F:/data"
    taskname=u"task2018"
    user_id=u"1"
    clipfromsde.clipfromsde(u"I49E019021,I49E019022,I49E019023", MEDIA,taskname,user_id)

    #clipfromsde.clipfromsde.delay(u"I49E019021,I49E019022,I49E019023", MEDIA,taskname)
    # clipfromsde.clipfromsde.delay(6, 9)
    return True


if __name__ == "__main__":
    begin()