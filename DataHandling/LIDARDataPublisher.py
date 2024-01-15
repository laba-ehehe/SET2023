#import ros
import rospy

#import data
from sensor_msgs.msg import PointCloud, Point32

import math

def lidar_publisher():
    #Initialize ROS node
    rospy.init_node('lidar_publisher')


    #create Publisher
    lidar_pub=rospy.Publisher('/lidar_scan')

    #define publishing rate
    rate=rospy.Rate(10) #10 Hz


    #main loop
    while not rospy.is_shutdown():
        #calls method to get data
        lidar_data=get_parsed_lidar()

        #instantiates point cloud message to publish later
        lidar_msg=PointCloud()


        #fill headers of point cloud message
        lidar_msg.header.stamp=rospy.Time.now()
        lidar_msg.header.frame_id="placeholder" #replace with SET Robot base link

        #for points in lidar_data retrieved, convert to x y
        for point in lidar_data:
            x = point * math.cos(0) # replace 0 with angle given in parsed data
            y = point * math.sin(0) # replace 0 with angle given in parsed data
            z=0.0
            #populate point cloud message with points
            lidar_msg.points.append(Point32(x=x, y=y, z=z))

        #pulish
        lidar_pub.publish(lidar_msg)

        #sleep to match publishing rate
        rate.sleep()



#method to get parsed Lidar data
def get_parsed_lidar():
    pass


