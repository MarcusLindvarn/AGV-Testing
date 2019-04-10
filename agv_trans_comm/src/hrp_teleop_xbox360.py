#!/usr/bin/env python
import rospy
from geometry_msgs.msg import Twist
from sensor_msgs.msg import Joy
from agv_trans_comm.msg import ButtonPress

# Author: Marcus Lindvärn
# This ROS Node converts Joystick inputs from the joy node
# into commands for HRP
# Small changes has been made from the original file to make 
# it usable for this purpose

# Receives joystick messages (subscribed to Joy topic)
# then converts the joysick inputs into Twist commands
# axis 1 aka left stick vertical controls linear speed
# axis 0 aka left stick horizonal controls angular speed
def callback(data):
    twist = Twist()
    buttonpress = ButtonPress()
    # vertical left stick axis = linear rate
    twist.linear.x = 0.4*data.axes[1]
    # horizontal left stick axis = turn rate
    twist.angular.z = 0.7*data.axes[0]
    buttonpress.xpress = True
    buttonpress.bpress = False
    if (data.buttons[9]== 1):
        twist.linear.x = 0*data.axes[1]
        twist.angular.z = 0*data.axes[0]
    if (data.buttons[2]== 1):
        buttonpress.xpress = True
        buttonpub.publish(buttonpress)  
    if (data.buttons[1]== 1):
        buttonpress.bpress = True
        buttonpub.publish(buttonpress)
    
    pub.publish(twist)

# Intializes everything
def start():
    # publishing to "/cmd_vel" to control AGV
    global pub
    pub = rospy.Publisher('/cmd_vel', Twist)
    global buttonpub
    buttonpub = rospy.Publisher('/button_state', Twist)
    # subscribed to joystick inputs on topic "joy"
    rospy.Subscriber("joy", Joy, callback)
    # starts the node
    rospy.init_node('Joy2HRP')
    rospy.spin()

if __name__ == '__main__':
    start()
