#!/usr/bin/env python3
import rclpy
import math
from rclpy.node import Node
from mars_msgs.msg import RoverOdometry

class Displayer(Node):
    def __init__(self):
        super().__init__('displayer')
        self.count = 1
        self.odo_sub_ = self.create_subscription(RoverOdometry, 'rover_status/rover_odometry', self.receiveOdo, 10)

    def receiveOdo(self, dat: RoverOdometry):
        self.linear_vel_x = dat.linear_velocity.linear.x
        self.linear_vel_y = dat.linear_velocity.linear.y
        self.angular_vel = dat.angular_velocity
        if self.count == 1:
            self.x = 0
            self.y = 0
            self.orientation = 0
        self.x+= self.linear_vel_x
        self.y+= self.linear_vel_y
        self.orientation+= self.angular_vel
        while self.orientation > 2* math.pi:
            self.orientation -= 2* math.pi

        self.get_logger().info('x coordinate: ' + str(self.x))
        self.get_logger().info('y coordinate: ' + str(self.y))
        self.get_logger().info('Orientation: ' + str(self.orientation))

        self.linear_vel = math.sqrt((self.linear_vel_x)**2 + (self.linear_vel_y)**2)
        if self.linear_vel > 3:
            self.get_logger().info('Warning! Speed exceeds 3')
        
        self.count+=1

        
        
def main(args = None):
    rclpy.init(args=args)
    new_node = Displayer()
    rclpy.spin(new_node)
    rclpy.shutdown()

if __name__ == '__main__':
    main()