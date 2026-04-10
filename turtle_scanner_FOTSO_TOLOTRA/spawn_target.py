import rclpy
from rclpy.node import Node
from turtlesim.srv import Spawn
import random


class SpawnTarget(Node):

    def __init__(self):
        super().__init__('spawn_target')

        # Création du client pour le service /spawn
        self.client = self.create_client(Spawn, '/spawn')

        # Attendre que le service soit disponible
        while not self.client.wait_for_service(timeout_sec=1.0):
            self.get_logger().info('Service /spawn non disponible, attente...')

        # Création de la requête
        self.request = Spawn.Request()

        # Coordonnées aléatoires
        self.request.x = random.uniform(1.0, 10.0)
        self.request.y = random.uniform(1.0, 10.0)
        self.request.theta = 0.0
        self.request.name = 'turtle_target'

        # Appel du service
        self.future = self.client.call_async(self.request)
        self.future.add_done_callback(self.callback_response)

    def callback_response(self, future):
        try:
            response = future.result()

            self.get_logger().info(
                f"Tortue spawnée ! Nom: {response.name} | "
                f"x: {self.request.x:.2f}, y: {self.request.y:.2f}"
            )

        except Exception as e:
            self.get_logger().error(f"Erreur lors du spawn: {e}")


def main(args=None):
    rclpy.init(args=args)

    node = SpawnTarget()

    rclpy.spin(node)

    node.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()
