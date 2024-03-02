import os
from launch import LaunchDescription
from launch_ros.actions import Node
from ament_index_python.packages import get_package_share_directory

def generate_launch_description():

    package_name = 'goal_bot'
    return LaunchDescription([

        Node(
            package='rplidar_ros',
            executable='rplidar_composition',
            output='screen',
            parameters=[
               get_package_share_directory(package_name) + '/config/rplidar_node.yaml'
            ]
        )
    ])

#Change serial port 
