#!/usr/bin/env python3
import random
import rclpy
from rclpy.node import Node
from std_msgs.msg import Float32MultiArray

class Battery_Temperature(Node):
    def __init__(self):
        super().__init__('battery_and_temperature_publisher')
        self.bat_temp_pub_ = self.create_publisher(Float32MultiArray, '/rover_stats', 10)
        self.timer_ = self.create_timer(2.0, self.timerCallback)

    def timerCallback(self):
        battery_level = random.random() * 100
        temperature = (random.random() * 100) -20
        cmd = Float32MultiArray
        cmd.data = [battery_level, temperature]
        self.bat_temp_pub_.publish(cmd)
        self.get_logger().info('Published message')
        

def main(args = None):
    rclpy.init(args=args)
    new_node = Battery_Temperature()
    rclpy.spin(new_node)
    rclpy.shutdown()