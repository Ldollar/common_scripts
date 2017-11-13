#!/user/bin/env python
# -*- coding:utf-8 -*-
from random import Random

import cv2
import multiprocessing
import numpy
import os
import threading
videos_src_path = 'E:\LOG\image\\videos'
videos_save_path = 'E:\LOG\image\\frame'

videos = os.listdir(videos_src_path)
videos = filter(lambda x: x.endswith('mp4'), videos)

def sample_group():   #每十个视频取一对相邻的视频组
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
    print "get the all videos are : ",res,len(res)
    return res


def get_all_frame_image():
    '''获取每一帧信息，并以jpg格式保存图片'''
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
            print 'Read a new %s frame:  '%frame_count, success
            params = []
            params.append(cv2.IMWRITE_PXM_BINARY)
            cv2.imwrite(each_video_save_full_path + each_video_name + "_%d.jpg" % frame_count, frame, params)
            # if success == False:
            #     print frame_count
            #     print 'dalsdjljkjlkjljljljjljldsa'
            #     print gggg[-2]
            #
            #     ff = frame_count - 1
            #     cv2.imwrite(each_video_save_full_path + each_video_name + "_%d.jpg" % ff, gggg[-2], params)

            frame_count = frame_count + 1

        cap.release()
def get_first_last_frame_each_video():
    '''获取一个视频的第一帧和最后一帧信息，并以jpg格式保存图片'''
    for each_video in videos:
        print each_video
        each_video_name, _ = each_video.split('.')
        #os.mkdir(videos_save_path + '\\' + each_video_name)
        #each_video_save_full_path = os.path.join(videos_save_path, each_video_name) + '/'
        each_video_save_full_path = 'E:\LOG\image\\frame\\all1\\'
        # get the full path of each video, which will open the video tp extract frames
        each_video_full_path = os.path.join(videos_src_path, each_video)

        cap = cv2.VideoCapture(each_video_full_path)

        frame_count = 1
        success = True
        put_one_franme = []
        while (success):
            success, frame = cap.read()

            print "Read the file is %s : and the frame count is : %s" % (each_video_name, frame_count)
            # print 'Read a new frame: ', success
            put_one_franme.append(frame)
            params = []
            params.append(cv2.IMWRITE_PXM_BINARY)
            # params.append(cv2.IMWRITE_PNG_COMPRESSION)
            if frame_count == 1:
                # print "-------------1 frame------------"
                cv2.imwrite(each_video_save_full_path + each_video_name + "_%d.jpg" % frame_count, frame, params)

            elif success == True:
                out_one_frame = put_one_franme.pop()

            elif success == False:
                try:
                    last_true_frame_number = frame_count - 1
                    cv2.imwrite(each_video_save_full_path + each_video_name + "_%d.jpg" % last_true_frame_number, out_one_frame, params)
                except Exception, e:
                    print e

            frame_count = frame_count + 1
        print "the last image file number is %s " % frame_count

        cap.release()

def get_media_each_frame(each_video_name,each_video):
    '''
    获取视频每一帧信息，并保存第一帧和最后一帧
    :param each_video_name: 视频文件名称，不带后缀
    :param each_video: 带后缀的视频文件
    :return:
    '''
    each_video_save_full_path = 'E:\LOG\image\\frame\\all4\\'
    #each_video_save_full_path = os.path.join(videos_save_path, each_video_name) + '/'

    # get the full path of each video, which will open the video tp extract frames
    each_video_full_path = os.path.join(videos_src_path, each_video)


    cap = cv2.VideoCapture(each_video_full_path)
    frame_count = 1
    success = True
    put_one_franme = []
    while (success):
        success, frame = cap.read()

        print "Read the file is %s : and the frame count is : %s" % (each_video_name,frame_count)
        #print 'Read a new frame: ', success
        put_one_franme.append(frame)
        params = []
        params.append(cv2.IMWRITE_PXM_BINARY)
        #params.append(cv2.IMWRITE_PNG_COMPRESSION)
        if frame_count ==1:
            #print "-------------1 frame------------"
            cv2.imwrite(each_video_save_full_path + each_video_name + "_%d.jpg" % frame_count, frame, params)

        elif success ==True:
            out_one_frame=put_one_franme.pop()

        elif success == False:
            try:
                last_true_frame_number = frame_count - 1
                cv2.imwrite(each_video_save_full_path + each_video_name + "_%d.jpg" % last_true_frame_number, out_one_frame, params)
            except Exception,e:
                print e

        frame_count = frame_count + 1
    print "the last image file number is " % frame_count

    cap.release()

# def test_timer():
#     print '---------- i am test 123 --------'
#     global timer
#     timer = threading.Timer(20,test_timer)
#     timer.start()


def main(list1):
    #threads=[]
    allvideoss=list1
    pool = multiprocessing.Pool(processes=2)
    for each_video1 in allvideoss:
        print each_video1
        each_video_name1, _ = each_video1.split('.')
        pool.apply_async(get_media_each_frame,args=(each_video_name1,each_video1,))
    # timer = threading.Timer(1,test_timer)
    # timer.start()
    pool.close()
    pool.join()
    #for i in threads:
        #threads[i].start()
    #t.join()

if __name__ == '__main__':
    #get_all_frame_image()
    get_first_last_frame_each_video()
    #get_all_frame_image=sample_group()

    # each_ten_get_two = []
    # for i in get_all_frame_image:
    #     length_ten_arry=len(i)
    #     #print length_ten_arry
    #     rd =Random()
    #     if length_ten_arry>=2:
    #         zzz=rd.randint(0,length_ten_arry-1)
    #         #print i
    #         each_ten_get_two.append(i[zzz])
    #         each_ten_get_two.append(i[zzz-1])
    # print each_ten_get_two
    # main(list1=each_ten_get_two)

