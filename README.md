## 1 cartographer安装

### 1.1 apt安装依赖

```bash
sudo apt update
sudo apt install -y \
  ros-humble-cartographer \
  ros-humble-cartographer-ros \
  ros-humble-cartographer-ros-msgs \
  ros-humble-cartographer-rviz
```

查看 Cartographer ROS 2 节点是否存在

```bash
ros2 pkg list | grep cartographer 
# 我的输出
# (zxc) zufezzq@Thinkbook:~/cartographer_ros_custom$ ros2 pkg list | grep cartographer 
# cartographer_ros
# cartographer_ros_msgs
# cartographer_rviz
# (zxc) zufezzq@Thinkbook:~/cartographer_ros_custom$ 

```

### 1.2 源码编译

#### 依赖下载
```bash
sudo apt update
sudo apt install -y \
	clang \
    cmake \
    g++ \
    git \
    google-mock \
    libceres-dev \
    liblua5.3-dev \
    libboost-all-dev \
    libprotobuf-dev \
    protobuf-compiler \
    libeigen3-dev \
    libgflags-dev \
    libgoogle-glog-dev \
    libcairo2-dev \
    libpcl-dev \
    libsuitesparse-dev \
    python3-sphinx \
    lsb-release \
    ninja-build \
    stow
```

#### 源码安装

```bash
git clone https://github.com/ros2/cartographer.git
git clone https://github.com/ros2/cartographer_ros.git
```

编译代码自行找资料，这里不再赘述。
如果发生重复宏定义错误则可以建议拉取中的cartographer子模块，并重新编译。

```bash
git clone --recursive https://github.com/fishros/fishbot.git -b humble
```

注意每次编译编译cartograher时候注意需要
```bash
# 编译自己的cartographer
source install/setup.bash
```

## 2 cartographer测试


### tips
如果是使用apt安装的，可以直接运行demo
源码需要
```bash
# 编译自己的cartographer_ros
source install/setup.bash
```

### 第一个终端：

注意 ROS2 不能直接运行官方的.bag文件，需要转换为.db3文件
参考
![如何ROS和ROS2 bag转换数据](https://blog.csdn.net/weixin_51612528/article/details/146243805)

```bash
# ros2 bag安装
# pip install rosbags
rosbags-convert --src ros1.bag --dst ros2bag/
------------------------------------------
# --src <输入路径>：源文件是 ros1格式.bag 或 ros2的bag目录。
# --dst <输出文件>：目标转换文件的路径。
```

```bash
# 文件已经放在Nas上了，直接下载
ros2 bag play ros2_bag.db3 
```

### 第二个终端：

```bash
ros2 launch cartographer_ros backpack_3d.launch.py
```

### 第三个终端：

```bash
rviz2
```

添加map，即可查看


### 3 构建自己的实例

