#!usr/bin/env python
# -*- coding:utf-8 -*-
import os

import imageio
from moviepy.editor import *
#from skvideo.io import VideoCapture
imageio.plugins.ffmpeg.download()
os.chdir("E:\LOG\image")
aaa=VideoFileClip("E:\LOG\image\\20171030144718.mp4")
#aaa.
