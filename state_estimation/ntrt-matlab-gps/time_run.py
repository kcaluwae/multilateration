#Normal python imports
import numpy as np
import scipy.spatial as ss
import scipy.io

# ROS imports
import roslib; roslib.load_manifest('gps_agent_pkg')
import rospy
from gps_agent_pkg.msg import SUPERballState, SUPERballStateArray
from std_msgs.msg import Float32MultiArray, Float32, UInt16

# ROS node
rospy.init_node("manual_motor")

# Global variables
motor_pos = [0.0, #1
             0.0, #2
             0.0, #3
             0.0, #4
             0.0, #5
             0.0, #6
             0.0, #7
             0.0, #8
             0.0, #9
             0.0, #10
             0.0, #11
             0.0] #12

# Setup ROS publishers for motor positions
motor_pubs = []
for i in range(12):
    if i % 2 == 0:
        bbb, board_id, sub_index = i + 2, 0x71, 0x2
    else:
        bbb, board_id, sub_index = i + 1, 0x1, 0x1
    motor_pubs.append(rospy.Publisher('/bbb%d/0x%x_0x2040_0x%x' % (bbb, board_id, sub_index), \
                           Float32, queue_size=1))

time_pub = rospy.Publisher('/superball/timestep', UInt16, queue_size=1)

# Testing single motor movements
motor_move = [8,12,4,2,5,9] 
move_amount = 60 
count = 1
index = 2
lastIndex = 5
rate = 100 #in ms
move = 0
out = 0
motor_power = 0.7 #Percentage of avaliable motor power

# Set program rate and main loop
r = rospy.Rate(1000/rate)
while(not rospy.is_shutdown()):
    time_pub.publish(rate)
    r.sleep()
