# buaa_rescue_robot
The warehouse uses ros2 to complete the control system code of the rescue robot.

## 1.正运动学：
### （1）启动服务端节点ros2 run forward_kinematics fw_server
### （2）启动客户端节点ros2 run forward_kinematics fw_client theta1 theta2(theta1和theta2为具体参数)

## 2.逆运动学：
### (1)ros2 run inverse_kinematics fk_server
### (2)ros2 run inverse_kinematics ik_server 
### (2)ros2 run inverse_kinematics ik_client x y  (x和y为具体参数)
