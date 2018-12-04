#!C:/Python27/ArcGIS10.2/python.exe
#-*- coding:utf-8 -*-
"""
#============================================
#
# Project: mycelery
# Name: The file name is celeryconfig
# Purpose: 
# Auther: Administrator
# Tel: 17372796660
#
#============================================
#
"""

BORKER_URL='amqp://admin:Lantucx2018@localhost:15672/admin-vhost'

BACKEND_URL='amqp'

CELERY_TIMEZONE='Asiz/Shanghai'

CELERY_IMPORTS=(
    'celery_app.clipfromsde',
)