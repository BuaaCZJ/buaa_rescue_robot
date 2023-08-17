import rclpy
from rclpy.node import Node
from std_msgs.msg import String
import serial

class SerialNode(Node):
    def __init__(self):
        super().__init__('serial_node')
        # 初始化串口
        self.ser = serial.Serial('/dev/ttyUSB0', 115200, timeout=1)
        # 创建发布器和订阅器
        self.publisher_ = self.create_publisher(String, 'serial_data', 10)
        self.subscription = self.create_subscription(
            String,
            'serial_data',
            self.serial_callback,
            10)

    def serial_callback(self, msg):
        # 接收到订阅的消息时，将数据发送到串口
        self.get_logger().info('Sending serial data: %s' % msg.data)
        self.ser.write(msg.data.encode())

    def main(self):
        while rclpy.ok():
            # 循环读取串口数据
            data = self.ser.readline().decode()
            if data:
                # 收到串口数据时，发布消息
                self.get_logger().info('Received serial data: %s' % data)
                msg = String()
                msg.data = data
                self.publisher_.publish(msg)

def main(args=None):
    rclpy.init(args=args)
    node = SerialNode(serial_node)
    node.main()
    node.destroy_node()
    rclpy.shutdown()

 #if  == '__main__':
   main()
