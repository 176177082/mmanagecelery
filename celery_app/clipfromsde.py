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
from celery_app import app

reload(sys)
sys.setdefaultencoding('utf8')


@app.task
def clipfromsde(mapnumlist,MEDIA):
    taskpath=MEDIA
    SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
    pgsde = u"pgarcgis.sde"

    arcpy.env.workspace = os.path.join(SCRIPT_DIR, pgsde)

    tempath = os.path.join(SCRIPT_DIR, u"tasktemlate")
    shutil.copytree(tempath, taskpath)
    jtbpath = os.path.join(taskpath, u"Source", u"接图表.gdb", u"DLG_50000", u"GBmaprange")

    SQList = []
    for mapnum in mapnumlist.split(u","):
        SQL = u"new_jbmapn = '%s'" % mapnum
        SQList.append(SQL)
    SQLstr = u" or ".join(SQList)

    for ds in arcpy.ListDatasets(feature_type='feature') + ['']:
        if ds == u"dbgg.sde.mapinde":
            for fc in arcpy.ListFeatureClasses(feature_dataset=ds):
                fcpath = os.path.join(arcpy.env.workspace, ds, fc)
                arcpy.Select_analysis(fcpath, jtbpath, SQLstr)

    for ds in arcpy.ListDatasets(feature_type='feature') + ['']:
        if ds == u"dbgg.sde.DLG_K050":
            for fc in arcpy.ListFeatureClasses(feature_dataset=ds):
                fcpath = os.path.join(arcpy.env.workspace, ds, fc)
                taskgbpath = os.path.join(taskpath, u"Source", u"GBRGS.gdb", u"DLG_K050", fc.split(".")[2][0:9])
                arcpy.Clip_analysis(fcpath, jtbpath, taskgbpath)

    for ds in arcpy.ListDatasets(feature_type='feature') + ['']:
        if ds == u"dbggg.sde.DLG_K050_jb":
            for fc in arcpy.ListFeatureClasses(feature_type=ds):
                fcpath = os.path.join(arcpy.env.workspace, ds, fc)
                taskjbpath = os.path.join(taskpath, u"Source", u"JBRGS.gdb", u"DLG_K050", fc.split(".")[2][0:9])
                arcpy.Clip_analysis(fcpath, jtbpath, taskjbpath)

    return True


if __name__ == "__main__":
    clipfromsde()
