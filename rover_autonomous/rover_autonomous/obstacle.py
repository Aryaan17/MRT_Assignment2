#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
from std_msgs.msg import Float32MultiArray

class Obstacle_Coords(Node):
    def __init__(self):
        super().__init__('obstacle_avoidance')
        self.obs_pub_ = self.create_publisher(Float32MultiArray, '/obstacle_coordinates', 10)
        self.obs = [[1,0,0,0,0,1,0,1,0,0], [0,1,0,0,1,0,0,0,1,0], [0,0,1,0,0,0,1,0,0,1], [1,0,0,1,0,0,0,1,0,0], [0,1,0,0,1,0,0,0,0,1], [0,0,1,0,0,0,1,0,0,0], [0,1,0,0,0,1,0,0,0,1], [1,0,0,0,1,0,0,0,1,0], [0,0,1,0,0,0,1,0,0,0]]
        self.publishInitial()

    def publishInitial(self):
        cmd = Float32MultiArray()
        for y in range(len(self.obs)):
            for x in range(len(self.obs[y])):
                if self.obs[y][x] == 1:
                    cmd.data.append(100*x + y)
        self.obs_pub_.publish(cmd)
        self.get_logger().info('Published')
        self.get_logger().info(cmd)
        

def main(args = None):
    rclpy.init(args=args)
    new_node = Obstacle_Coords()
    rclpy.spin(new_node)
    rclpy.shutdown()

if __name__ == '__main__':
    main()    