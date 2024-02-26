import rclpy
from rclpy.node import Node

from std_msgs.msg import String


class Assinante(Node):
    def __init__(self):
        super().__init__('Assinante')
        self.get_logger().info('Escutando topico')
        self._assinatura = self.create_subscription(String, "mensagem_do_publicador",self.callback, 10)
        self._assinatura2 = self.create_subscription(String, "topico2",self.callback2, 10)
       
    
    def callback(self, msg):
        mensagem = msg.data
        self.get_logger().info(mensagem)
    
    def callback2(self,msg):
        mensagem = msg.data
        self.get_logger().info(mensagem)
        




def main(args=None):
    rclpy.init(args=args)
    assinante =  Assinante()
    rclpy.spin(assinante)
    rclpy.shutdown()
    
    
    
if __name__ == '__main__':
    main()