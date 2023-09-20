# buaa_rescue_robot
The warehouse uses ros2 to complete the control system code of the rescue robot.

## 逆运动学：
### (1)ros2 run inverse_kinematics fk_server (启动正运动学服务端)
### (2)ros2 run inverse_kinematics ik_server (启动逆运动学服务端和正运动学客户端)
### (2)ros2 run inverse_kinematics ik_client x y  (启动逆运动学客户端，x和y为具体参数)
