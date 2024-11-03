#!/usr/bin/env python3
import random
import rclpy
from rclpy.node import Node
from mars_msgs.msg import RoverOdometry

class Velocity(Node):
    def __init__(self):
        super().__init__('motion_publisher')
        self.vel_pub = self.create_publisher(RoverOdometry, 'rover_status/rover_odometry', 10)
        self.count = 1
        self.timer_ = self.create_timer(1.0, self.timerCallback)

    def timerCallback(self):
        cmd = RoverOdometry()
        linear_vel_x = random.random() * 3
        linear_vel_y = random.random() * 3
        angular_vel = random.random() * 2
        cmd.rover_id = 1
        cmd.angular_velocity = angular_vel
        cmd.linear_velocity.linear.x = linear_vel_x
        cmd.linear_velocity.linear.y = linear_vel_y
        self.vel_pub.publish(cmd)
        self.get_logger().info('Published message '+ str(self.count))
        self.count+=1

def main(args = None):
    rclpy.init(args=args)
    new_node = Velocity()
    rclpy.spin(new_node)
    rclpy.shutdown()

if __name__ == '__main__':
    main()    