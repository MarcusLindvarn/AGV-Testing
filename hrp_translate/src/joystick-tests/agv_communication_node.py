#!/usr/bin/env python
import rospy
from geometry_msgs.msg import Twist
from sensor_msgs.msg import Joy
from hrp_translate.msg import ButtonPress
from hrp_translate.msg import Command
from hrp_translate.msg import State


# Author: Marcus Lindvärn

def callback_commandcenter(data):
    if last_command
def callback_button_state(data):
    if (data.xpressed = true):
        
    if (data.bpressed = true):

def refresh_view()
    print('Last command: ' + last_command_recieved)
# Intializes everything
def start():    
    global last_command_recieved
    global last_state_recieved
    global pub
    pub = rospy.Publisher('/AGV_state', Twist)
    global buttonpub
    buttonpub = rospy.Publisher('/state_button', Twist)
    # subscribed to joystick inputs on topic "joy"
    rospy.Subscriber("/commandcenter", command, callback_commandcenter)
    rospy.Subscriber("/button_state", ButtonPress, callback_button_state)
    # starts the node
    rospy.init_node('AGVComms_node')
    rospy.spin()

if __name__ == '__main__':
    start()

