#!/usr/bin/python
# -*- coding: utf-8 -*-

import sys, os, re
# Imports the monkeyrunner modules used by this program
from com.android.monkeyrunner import MonkeyRunner, MonkeyDevice

# argc = len(sys.argv)
# if argc < 3:
#     print('usage: %android_sdk%tools\monkeyrunner dumpMemory.py [package] [activity] [extras]')
#     sys.exit(1)
#
# Connects to the current device, returning a MonkeyDevice object
device = MonkeyRunner.waitForConnection()
#
package = sys.argv[1]  # 'com.starcor.hljiptv.app'
# activity = sys.argv[2]  # 'com.starcor.hljiptv.app.CommonActivity'
# # extras = dict(sys.argv[3])  # {'pageId':'videoListPage'}
# extras = {'xul_page_id': 'page_video_list',
#           'xul_layout_file': 'xul_layouts/pages/xul_video_list_page.xml',
#           'xul_page_behavior': 'VideoListBehavior',
#           'xul_behavior_params': {'categoryId': "{'A': '10002', 'C': '', 'T': 'vod'}",
#                                   'media_asset_id': 10002,
#                                   'category_id': 1000001,
#                                   'category_type': 0}
#           }
#
#
# # sets the name of the component to start
# runComponent = package + '/' + activity
#
# # Runs the component
# device.startActivity(component=runComponent, extras=extras)


def causeGC():
    gcCmd = '"for p in /proc/[0-9]*; do [[ $(<$p/cmdline) = ' + package + ' ]] && su -c kill -10 ${p##*/}; done"'
    device.shell(gcCmd)
    MonkeyRunner.sleep(5)


def enterPage():
    device.touch(1025, 409, MonkeyDevice.DOWN_AND_UP)  # 改成点击的坐标
    MonkeyRunner.sleep(10)


def exitPage():
    device.press('KEYCODE_BACK', MonkeyDevice.DOWN_AND_UP)


def getMemory():
    cmd = 'adb shell dumpsys meminfo ' + package
    data = os.popen(cmd).readlines()
    data = filter(lambda x: 'Dalvik Heap' in x, data)
    data = re.split('\s+', data[0])
    print(data[4])
    return data[4]

causeGC()
for i in range(10):
    enterPage()
    exitPage()

    causeGC()
    getMemory()
    MonkeyRunner.sleep(5)

