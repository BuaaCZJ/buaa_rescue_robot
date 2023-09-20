#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
@说明: 创建逆运动学服务端节点ik_server和正运动学客户端节点fk_client
"""

import rclpy                                                                               # ROS2 Python接口库
from rclpy.node   import Node                                                              # ROS2 节点类
from my_interface.srv import Inverses                                                      # 自定义的服务接口
import numpy as np

class adderClient(Node):
    def __init__(self):
        super().__init__('fk_client')                                                      # ROS2节点父类初始化
        self.client = self.create_client(Inverses, 'forward_kinematics')                   # 创建服务器对象（接口类型、服务名、服务器回调函数）
        while not self.client.wait_for_service(timeout_sec=1.0):                           # 循环等待服务器端成功启动
            self.get_logger().info('service not available, waiting again...') 
        self.request=Inverses.Request()                                                    # 创建服务请求的数据对象
        
        
    def send_request(self,m,n):                                                            # 创建一个发送服务请求的函数 
        self.request.a=m
        self.request.b=n
        self.future=self.client.call_async(self.request)                                   #异步方式发送请求
         
    
    
class adderServer(Node):
    def __init__(self, client):
        super().__init__('ik_server')                                                      # ROS2节点父类初始化
        self.srv = self.create_service(Inverses, 'inverse_kinematics', self.callback)      # 创建服务器对象（接口类型、服务名、服务器回调函数）
        self.client=client                                                                 # 在该类中接收传入的客户端节点
        self.request=Inverses.Request()                                                    # 创建服务请求的数据对象
        

    def callback(self, request, response):                                                 # 创建回调函数，执行收到请求后对数据的处理
        response.theta1=request.x
        response.theta1=request.y
        q=request.x
        w=request.y
        
        #逆运动学模型编写
        
        
        self.client.send_request(q,w)
        response=self.client.future.result()
        
        while rclpy.ok():                                                                  # ROS2系统正常运行
            rclpy.spin_once(self.client)                                                   # 循环执行一次节点

            if self.client.future.done():                                                  # 数据是否处理完成
                try:
                    response =self.client.future.result()                                  # 接收服务器端的反馈数据
                except Exception as e:
                    self.client.get_logger().info(
                    'Service call failed %r' % (e,))
                else:
                    print(response.summary)
                    self.client.get_logger().info(                                                   # 将收到的反馈信息打印输出
                    'Result of add_two_ints: for %d + %d = %d' % 
                    (q, w, response.summary))
            break
        print(response.summary)
        return response                                                                    # 反馈应答信息


    

def main(args=None):                                 # ROS2节点主入口main函数
    rclpy.init(args=args)                            # ROS2 Python接口初始化
                       
    client=adderClient()                             # 创建正运动学的客户端
    server=adderServer(client)                       # 创建逆运动学的服务端
    
    rclpy.spin(server)                               # 循环等待ROS2退出
    node.destroy_node()                              # 销毁节点对象
    rclpy.shutdown()                                 # 关闭ROS2 Python接口
