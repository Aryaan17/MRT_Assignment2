#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
from std_msgs.msg import Float32MultiArray
from std_msgs.msg import String

class Displayer(Node):
    def __init__(self):
        super().__init__('displayer')
        self.bat_temp_sub_ = self.create_subscription(Float32MultiArray, 'rover_status/rover_stats', self.receiveBatTemp, 10)
        self.health_sub_ = self.create_subscription(String, 'rover_status/rover_health', self.receiveHealth,10)

    def receiveBatTemp(self, dat: Float32MultiArray):
        self.battery_level = dat.data[0]
        self.temperature = dat.data[1]
    
    def receiveHealth(self, dat: String):
        self.battery_health = dat.data
        self.get_logger().info('Battery level: ' + str(self.battery_level))
        self.get_logger().info('Battery health: ' + str(self.battery_health))
        self.get_logger().info('Temperature: '+ str(self.temperature))
        
def main(args = None):
    rclpy.init(args=args)
    new_node = Displayer()
    rclpy.spin(new_node)
    rclpy.shutdown()

if __name__ == '__main__':
    main()