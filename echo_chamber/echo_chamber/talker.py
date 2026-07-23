import rclpy
from rclpy.node import Node
from std_msgs.msg import Float32
import random

class TalkerNode(Node):
    def __init__(self):
        super().__init__('talker')
        # Create a publisher on topic '/random_number' using Float32
        self.publisher_ = self.create_publisher(Float32, '/random_number', 10)
        # Timer to run every 1 second (1.0 Hz)
        self.timer = self.create_timer(1.0, self.timer_callback)

    def timer_callback(self):
        msg = Float32()
        msg.data = random.uniform(0.0, 100.0)  # Random float between 0.0 and 100.0
        self.publisher_.publish(msg)
        self.get_logger().info(f'Published: {msg.data:.2f}')

def main(args=None):
    rclpy.init(args=args)
    node = TalkerNode()
    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        pass
    finally:
        node.destroy_node()
        rclpy.shutdown()

if __name__ == '__main__':
    main()