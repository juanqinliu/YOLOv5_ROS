#!/usr/bin/env python
#coding:utf-8
 
import rospy
import sys
sys.path.append('.')
import cv2
import os
import numpy as np
from sensor_msgs.msg import Image
from std_msgs.msg import Header
# from cv_bridge import CvBridge, CvBridgeError
import ctypes
libgcc_s = ctypes.CDLL('libgcc_s.so.1')
 
def pubVideo():
    rospy.init_node('pubVideo',anonymous = True)
    pub = rospy.Publisher('/camera/color/image_raw', Image, queue_size = 10)
    rate = rospy.Rate(10)
    path = "/home/ljq/GL-YOMO-ros/videos/FW_loiter1_H20T_W.mp4"
    cap = cv2.VideoCapture(path)
    scaling_factor = 0.5
    # bridge = CvBridge()
    if not cap.isOpened():
        rospy.loginfo("vedio is not available!")
        return -1
    else:
        rospy.loginfo("Successful opened video file:{}".format(path))
    count = 0
    while not rospy.is_shutdown():
        ret, frame = cap.read()
        if ret:
            count = count + 1
        else:
            rospy.loginfo("Capturing image failed.")
        if count == 2:
            count = 0
            frame = cv2.resize(frame,None,fx=scaling_factor,fy=scaling_factor,interpolation=cv2.INTER_AREA)
            # msg = bridge.cv2_to_imgmsg(frame, encoding="bgr8")
            # Convert OpenCV image to ROS Image message without using cv_bridge 
            img_msg = Image() 
            img_msg.header = Header() 
            img_msg.header.stamp = rospy.Time.now() 
            img_msg.height, img_msg.width, channels = frame.shape 
            img_msg.encoding = "bgr8" 
            img_msg.step = img_msg.width * channels 
            img_msg.data = frame.tobytes()
            pub.publish(img_msg)
            # print('** publishing webcam_frame ***')	
        rate.sleep()
       
if __name__ == '__main__':
    try:
        pubVideo()
    except rospy.ROSInterruptException:
        pass
