import rclpy
from rclpy.node import Node
from std_msgs.msg import Float32

class ListenerNode(Node):
    def __init__(self):
        super().__init__('listener')
        # Create subscriber to the '/random_number' topic
        self.subscription = self.create_subscription(
            Float32,
            '/random_number',
            self.listener_callback,
            10)

    def listener_callback(self, msg):
        received_val = msg.data
        multiplied_val = received_val * 2
        # Print message showing the math operation
        self.get_logger().info(f'Received: [{received_val:.2f}]. Multiplied value: [{multiplied_val:.2f}]')

def main(args=None):
    rclpy.init(args=args)
    node = ListenerNode()
    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        pass
    finally:
        node.destroy_node()
        rclpy.shutdown()

if __name__ == '__main__':
    main()