import os
import yaml
from launch import LaunchDescription
from launch.actions import DeclareLaunchArgument
from launch.substitutions import LaunchConfiguration, PathJoinSubstitution
from launch_ros.actions import Node
from launch_ros.substitutions import FindPackageShare

def generate_launch_description():
    # 获取包路径
    pkg_share = FindPackageShare("zxc_cartographer").find("zxc_cartographer")
    
    # 读取YAML参数文件到字典对象
    params_path = os.path.join(pkg_share, "config", "zxc_backpack_3d_params.yaml")
    with open(params_path, 'r') as f:
        params_dict = yaml.safe_load(f)

    # 简单参数声明
    use_sim_time_arg = DeclareLaunchArgument(
        "use_sim_time", 
        default_value="true",
        description="Use simulation clock"
    )
    use_sim_time = LaunchConfiguration("use_sim_time")
    
    # Cartographer节点
    cartographer_node = Node(
        package="cartographer_ros",
        executable="cartographer_node",
        parameters=[{"use_sim_time": use_sim_time}],
        arguments=[
            "-configuration_directory", PathJoinSubstitution([pkg_share, "config"]),
            "-configuration_basename", params_dict['cartographer']['configuration_basename']
        ],
        remappings=[tuple(rule) for rule in params_dict['cartographer']['remappings']],
        output="screen"
    )

    # 栅格地图节点
    occupancy_grid_node = Node(
        package="cartographer_ros",
        executable="cartographer_occupancy_grid_node",
        parameters=[
            {"use_sim_time": use_sim_time},
            {"resolution": params_dict['occupancy_grid']['resolution']}
        ]
    )

    ld = LaunchDescription()
    ld.add_action(use_sim_time_arg)
    ld.add_action(cartographer_node)
    ld.add_action(occupancy_grid_node)

    return ld