#!/usr/bin/env python
# -*- coding: utf-8 -*-
import rospy
from geometry_msgs.msg import Twist
from sensor_msgs.msg import Joy
from agv_trans_comm.msg import ButtonPress
from agv_trans_comm.msg import Command
from agv_trans_comm.msg import State


# Author: Marcus Lindvärn
'''
def __init__ (self)
    last_command_recieved = ""
    last_product_recieved = ""
    last_run_recieved = False
    current_cmd = ""
    current_state = "init"
    agv_state.message = ""
    agv_state.cmd = ""
    agv_state.state = ""
'''
def callback_commandcenter(data):
    # update current and lastrecieved product to the recieved data - kanske kan skita i det helt och hållat då jag isnt svarar med ngt sådant
    #agv_state = State()
    #last_product_recieved = data.product_name
    #agv_state.product_name = last_product_recieved
    last_run_recieved = data.run

    #if a new command is recieved, update current command and refresh the view
    if (last_command_recieved != data.command):
        print ("last_command_recieved: " + last_command_recieved + '\n')
        print ("data.command: " + data.command + '\n')
        last_command_recieved = data.command
        current_cmd = data.command
        agv_state.cmd = current_cmd
        refresh_view(self)
    
    if (last_run_recieved == False and current_state == "finished")
        current_state = "init"
        agv_state.state = current_state
    #publisha alltid på mottaget meddelande med current status.
    ccpub.publish(agv_state)


def callback_button_state(data):
    #agv_state = State()
    # om X är nedtryckt, sät status till executing och publisha
    print ("xpressed: " + data.xpressed + '\n')
    print ("bpressed: " + data.bpressed + '\n')
    if (data.xpressed = True):
        current_state = "executing"
        current_cmd = last_command_recieved
        agv_state.state = current_state
        agv_state.cmd = current_cmd
    
    #om B är nedtrykt så sätt till finished, tömm cmd
    if (data.bpressed = True):
        current_state = "finished"
        agv_state.state = current_state
        current_cmd = ""
        agv_state.cmd = current_cmd
    #publicera med de nya ändringarna
    ccpub.publish(agv_state)

def refresh_view(self)
    print('Last command: ' + last_command_recieved)

# Intializes everything
def start():    
    agv_state = State()
    __init__(self)
    global last_command_recieved
    global last_run_recieved
    global last_product_recieved
    global current_state
    global current_cmd
    global ccpub
    last_command_recieved = ""
    last_product_recieved = ""
    last_run_recieved = False
    current_cmd = ""
    current_state = "init"
    agv_state.message = ""
    agv_state.cmd = ""
    agv_state.state = ""
    ccpub = rospy.Publisher('/AGV_state', State)
    #subscribing to the comandcenter topic as well as the buttionstates from the teleop.
    rospy.Subscriber("/commandcenter", command, callback_commandcenter)
    rospy.Subscriber("/button_state", ButtonPress, callback_button_state)
    # starts the node
    rospy.init_node('AGVComms_node')
    rospy.spin()

if __name__ == '__main__':
    start()

