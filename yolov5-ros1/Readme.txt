###  1. 下载镜像Download image
	docker pull juanqinliu/bit-tii:v3
###  2. 显示图像界面，在本地宿主机器上安装X11界面工具Display the image interface and install the X11 interface tool on your local host machine

	sudo apt-get install x11-xserver-utils
	xhost + (每次电脑开机需要运行)
### 3. 创建并进入容器 Create and enter a container
	docker run -it --net=host --ipc=host --name bit-tii --gpus all -v /tmp/.X11-unix:/tmp/.X11-unix -e DISPLAY=unix$DISPLAY -e GDK_SCALE -e GDK_DPI_SCALE -v /home/ps/Share:/home/share juanqinliu/bit-tii:v3 bash

###
--gpus all :挂载GPU
-v /tmp/.X11-unix:/tmp/.X11-unix -e DISPLAY=unix$DISPLAY -e GDK_SCALE -e GDK_DPI_SCALE 显示图形
-v /home/ps/Share:/home/share：共享文件夹
### 

###4.测试GPU挂载是否成功Test whether the GPU is mounted successfully
	nvidia-smi
### 5. 环境变量设置：Environment variable setting
	export PATH=/root/anaconda3/bin:$PATH
	source ~/.bashrc
	source activate Pytorch

	cd home/share/yolo-ros
	source /opt/ros/melodic/setup.bash
	source ~/.bashrc

### 6.编译Compile:
	catkin_make
### 7. 运行ROS：Run ROS:
	source devel/setup.bash
	roslaunch yolov5_ros yolo_v5.launch
	
	sudo apt-get install python3-tk

