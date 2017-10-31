#!/user/bin/env python
# -*- coding:utf-8 -*-
from random import Random

import cv2
import multiprocessing
import numpy
import os
import threading
videos_src_path = 'E:\LOG\image\\videos\\videos'
videos_save_path = 'E:\LOG\image\\frame'

videos = os.listdir(videos_src_path)
videos = filter(lambda x: x.endswith('mp4'), videos)

def group():
    allvideo=[]
    for each_video in videos:
        print each_video
        allvideo.append(each_video)
    #print allvideo
    res = []
    _length_array = len(allvideo)

    z= 0
    for i in range(0,_length_array):
        print i
        b=allvideo[z:z+10]
        z += 10
        res.append(b)
        while z >= _length_array-10:
            break
    print res
    return res


def aaa():
    for each_video in videos:
        print each_video
        each_video_name, _ = each_video.split('.')
        os.mkdir(videos_save_path + '\\' + each_video_name)
        each_video_save_full_path = os.path.join(videos_save_path, each_video_name) + '/'

        # get the full path of each video, which will open the video tp extract frames
        each_video_full_path = os.path.join(videos_src_path, each_video)

        cap = cv2.VideoCapture(each_video_full_path)
        frame_count = 1
        success = True
        while (success):
            success, frame = cap.read()
            print 'Read a new frame: ', success

            params = []
            params.append(cv2.IMWRITE_PXM_BINARY)
            cv2.imwrite(each_video_save_full_path + each_video_name + "_%d.jpg" % frame_count, frame, params)

            frame_count = frame_count + 1

        cap.release()

def get_media_each_frame(each_video_name,each_video):
    each_video_save_full_path = 'E:\LOG\image\\frame\\all\\'
    #each_video_save_full_path = os.path.join(videos_save_path, each_video_name) + '/'

    # get the full path of each video, which will open the video tp extract frames
    each_video_full_path = os.path.join(videos_src_path, each_video)


    cap = cv2.VideoCapture(each_video_full_path)
    frame_count = 1
    success = True
    while (success):
        success, frame = cap.read()

        print "Read the file is %s : and the frame count is : %s" % (each_video_name,frame_count)
        #print 'Read a new frame: ', success

        params = []
        params.append(cv2.IMWRITE_PXM_BINARY)
        #params.append(cv2.IMWRITE_PNG_COMPRESSION)
        if frame_count ==1:
            cv2.imwrite(each_video_save_full_path + each_video_name + "_%d.jpg" % frame_count, frame, params)

        elif frame_count==1182:
            cv2.imwrite(each_video_save_full_path + each_video_name + "_%d.jpg" % frame_count, frame, params)
        frame_count = frame_count + 1

    print "the last image file number is " % frame_count

    cap.release()


def main(list1):
    #threads=[]
    allvideoss=list1
    pool = multiprocessing.Pool(processes=4)
    for each_video1 in allvideoss:
        #print each_video1
        each_video_name1, _ = each_video1.split('.')
        #os.mkdir(videos_save_path + '\\' + each_video_name1)
        #get_media_each_frame(each_video_name=each_video_name1,each_video=each_video1)
        pool.apply_async(get_media_each_frame,args=(each_video_name1,each_video1,))
        #t=threading.Thread(target=get_media_each_frame,args=(each_video_name1,each_video1))
        #threads.append(t)
    pool.close()
    pool.join()
    #for i in threads:
        #threads[i].start()
    #t.join()

if __name__ == '__main__':

    aaa=group()

    each_ten_get_two = []
    for i in aaa:
        length_ten_arry=len(i)
        #print length_ten_arry
        rd =Random()
        if length_ten_arry>=2:
            zzz=rd.randint(0,length_ten_arry-1)
            #print i
            each_ten_get_two.append(i[zzz])
            each_ten_get_two.append(i[zzz-1])
    print each_ten_get_two
    main(list1=each_ten_get_two)