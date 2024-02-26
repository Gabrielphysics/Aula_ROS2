import rclpy
from rclpy.node import Node

from std_msgs.msg import String


class Publicador(Node):
    def __init__(self):
        super().__init__('publicador')
        self.get_logger().info('Publicador iniciado')
        
        self._publicador = self.create_publisher(String, "mensagem_do_publicador", 10)
        self._publicador2 = self.create_publisher(String, "topico2", 10)
        
        self.timer = self.create_timer(0.5, self.callback)
        self.timer2 = self.create_timer(0.5, self.callback2)
    
    
    def callback(self):
        msg = String()
        msg.data = "mensagem do publicador"
        self._publicador.publish(msg)
        
        
    def callback2(self):
        msg = String()
        msg.data = "mensagem do publicador2"
        self._publicador.publish(msg)
        




def main(args=None):
    rclpy.init(args=args)
    publicador =  Publicador()
    rclpy.spin(publicador)
    rclpy.shutdown()
    
    
    
if __name__ == '__main__':
    main()