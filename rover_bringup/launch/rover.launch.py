from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():
    ld = LaunchDescription()
    publish_data = Node(
        package = 'rover_status',
        executable = 'publish_data',
    )
    update_health = Node(
        package= 'rover_status',
        executable = 'publish_health'
    )
    display = Node(
        package= 'rover_status',
        executable = 'display'
    )
    ld.add_action(publish_data)
    ld.add_action(update_health)
    ld.add_action(display)
    return ld
