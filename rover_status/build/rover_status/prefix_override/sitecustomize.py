import sys
if sys.prefix == '/usr':
    sys.real_prefix = sys.prefix
    sys.prefix = sys.exec_prefix = '/home/aryaanb17/ros2_ws/src/rover_status/install/rover_status'
