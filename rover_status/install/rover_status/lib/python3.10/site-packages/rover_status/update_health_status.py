#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
from std_msgs.msg import Float32MultiArray
from std_msgs.msg import String

class Health_Status(Node):
    def __init__(self):
        super().__init__('battery_and_temperature_publisher')
        self.bat_temp_sub_ = self.create_subscription(Float32MultiArray, '/rover_status', self.batTempCallback, 10)
        self.health_pub_ = self.create_publisher(String, '/rover_health', 10)

    def batTempCallback(self, dat: Float32MultiArray):
        battery_level = dat[0]
        cmd = String()
        if battery_level > 50:
            cmd = 'Healthy'
        elif battery_level >20:
            cmd = 'Critical'
        else:
            cmd = 'Warning'
        self.health_pub_.publish(cmd)

        

def main(args = None):
    rclpy.init(args=args)
    new_node = Health_Status()
    rclpy.spin(new_node)
    rclpy.shutdown()