#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
@说明: 创建正运动学服务端节点fk_server
"""

import rclpy                                         # ROS2 Python接口库
from rclpy.node   import Node                        # ROS2 节点类
#from learning_interface.srv import Inverse          # 自定义的服务接口
from my_interface.srv import Inverses                # 自定义的服务接口
import numpy as np

class adderServer(Node):
    def __init__(self, name):
        super().__init__(name)                                                                 # ROS2节点父类初始化
        self.srv = self.create_service(Inverses, 'forward_kinematics', self.adder_callback)    # 创建服务器对象（接口类型、服务名、服务器回调函数）

    def adder_callback(self, request, response):                                               # 创建回调函数，执行收到请求后对数据的处理
        m=request.a
        n=request.b
        
        response.theta1=m
        response.theta2=n
        response.summary=m+n
        #正运动学模型
        self.get_logger().info('Incoming request\na: %d b: %d' % (request.a, request.b))       # 输出日志信息，提示已经完成加法求和计算
        return response                                                                        # 反馈应答信息

def main(args=None):                                 # ROS2节点主入口main函数
    rclpy.init(args=args)                            # ROS2 Python接口初始化
    node = adderServer("fk_server")                  # 创建ROS2节点对象并进行初始化
    rclpy.spin(node)                                 # 循环等待ROS2退出
    node.destroy_node()                              # 销毁节点对象
    rclpy.shutdown()                                 # 关闭ROS2 Python接口
    
    
