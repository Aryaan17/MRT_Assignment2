#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
from std_msgs.msg import Float32MultiArray
from std_msgs.msg import String

class Health_Status(Node):
    def __init__(self):
        super().__init__('rover_navigation')
        self.steps = [[0,0]]
        self.obs_sub_ = self.create_subscription(Float32MultiArray, '/obstacle_coordinates', self.roverNav, 10)
        self.status_pub_ = self.create_publisher(String, '/navigation/status', 10)

    def roverNav(self, dat: Float32MultiArray):
        self.coords = self.steps[-1]
        self.obs_coords = []
        for coord in dat.data:
            x = (round(coord/100)* 100)//100
            y = int(coord - 100*x)
            self.obs_coords.append([x,y])
        obs_surr = []
        for coord in self.obs_coords:
            if 1 in coord:
                obs_surr.append(coord)
        self.get_logger().info(self.obs_coords)

def main(args = None):
    rclpy.init(args=args)
    new_node = Health_Status()
    rclpy.spin(new_node)
    rclpy.shutdown()

if __name__ == '__main__':
    main()