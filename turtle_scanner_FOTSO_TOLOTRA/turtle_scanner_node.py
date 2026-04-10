#!/usr/bin/env python3

import rclpy
from rclpy.node import Node
from turtlesim.msg import Pose


class TurtleScanner(Node):
     
    def __init__(self):
        super().__init__('turtle_scanner_node')

        self.pose_target = None

        self.sub_target = self.create_subscription(
            Pose,
            '/turtle_target/pose',
            self.callback_target,
            10
        )

    def callback_target(self, msg):
        self.pose_target = msg
    def __init__(self):  # ✅ DOUBLE UNDERSCORE
        super().__init__('turtle_scanner_node')  # ✅ CORRECT

        # Attributs pour stocker les positions
        self.pose_scanner = None
        self.pose_target = None

        # Subscriber turtle1 (scanner)
        self.sub_scanner = self.create_subscription(
            Pose,
            '/turtle1/pose',
            self.callback_scanner,
            10
        )

        # Subscriber turtle_target
        self.sub_target = self.create_subscription(
            Pose,
            '/turtle_target/pose',
            self.callback_target,
            10
        )

        self.get_logger().info("TurtleScanner node démarré")

    def callback_scanner(self, msg):
        self.pose_scanner = msg
        self.get_logger().info(
            f"[SCANNER] x={msg.x:.2f}, y={msg.y:.2f}"
        )

    def callback_target(self, msg):
        self.pose_target = msg
        self.get_logger().info(
            f"[TARGET] x={msg.x:.2f}, y={msg.y:.2f}"
        )


def main(args=None):
    rclpy.init(args=args)

    node = TurtleScanner()

    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        pass

    node.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()
    
    self.pose_target = None
)
