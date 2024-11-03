#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
from std_msgs.msg import Float32MultiArray
from std_msgs.msg import String

class Displayer(Node):
    def __init__(self):
        super().__init__('battery_and_temperature_publisher')
        self.bat_temp_sub_ = self.create_subscription(Float32MultiArray, '/rover_status', self.receiveBatTemp, 10)
        self.health_sub_ = self.create_subscription(String, '/rover_health', self.receiveHealth,10)

    def receiveBatTemp(self, dat: Float32MultiArray):
        self.battery_level = dat[0]
        self.temperature = dat[1]
    
    def receiveHealth(self, dat: String):
        self.battery_health = dat
        print('Battery level:', self.battery_level)
        print('Battery health:', self.battery_health)
        print('Temperature:', self.temperature)
        

        

def main(args = None):
    rclpy.init(args=args)
    new_node = Displayer()
    rclpy.spin(new_node)
    rclpy.shutdown()