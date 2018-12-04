#!C:/Python27/ArcGIS10.2/python.exe
# -*- coding:utf-8 -*-
"""
#============================================
#
# Project: mycelery
# Name: The file name is clipfromsde
# Purpose: 
# Auther: Administrator
# Tel: 17372796660
#
#============================================
#
"""

import sys
import os
import arcpy
import shutil
import datetime
from celery_app import app

reload(sys)
sys.setdefaultencoding('utf8')


@app.task
def clipfromsde(mapnumlist,MEDIA,taskname,userid):
    taskdirname=u"user_{0}/{1}/{2}".format(userid, datetime.datetime.now().strftime("%Y-%m-%d-%H-%M-%S-%f"), taskname)

    SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
    rgsde = u"rgs20181204150827.sde"
    mapindexsde=u"mapindex20181204150827.sde"



    tempath = os.path.join(os.path.dirname(SCRIPT_DIR), u"tasktemplate")
    taskpath=os.path.join(MEDIA,taskdirname)
    shutil.copytree(tempath, taskpath)
    jtbpath = os.path.join(taskpath, u"Source", u"接图表.gdb", u"DLG_50000", u"GBmaprange")

    SQList = []
    for mapnum in mapnumlist.split(u","):
        SQL = u"new_jbmapn = '%s'" % mapnum
        SQList.append(SQL)
    SQLstr = u" or ".join(SQList)

    arcpy.env.workspace = os.path.join(SCRIPT_DIR, rgsde)

    for ds in arcpy.ListDatasets(feature_type='feature') + ['']:
        if ds == mapindexsde+u"DLG_50000":
            for fc in arcpy.ListFeatureClasses(feature_dataset=ds):
                if fc == mapindexsde+u"GBmaprange":
                    fcpath = os.path.join(arcpy.env.workspace, ds, fc)
                    arcpy.Select_analysis(fcpath, jtbpath, SQLstr)

    arcpy.env.workspace = os.path.join(SCRIPT_DIR, rgsde)
    for ds in arcpy.ListDatasets(feature_type='feature') + ['']:
        if ds == rgsde+u"DLG_K050":
            for fc in arcpy.ListFeatureClasses(feature_dataset=ds):
                fcpath = os.path.join(arcpy.env.workspace, ds, fc)
                taskgbpath = os.path.join(taskpath, u"Source", u"RGS.gdb", u"DLG_K050", fc.split(".")[2])
                arcpy.Clip_analysis(fcpath, jtbpath, taskgbpath)


    return True


if __name__ == "__main__":
    clipfromsde()
