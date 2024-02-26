import rclpy
from rclpy.node import Node, Parameter

class Parametros(Node):
    def __init__(self):
        super().__init__('Parametros')
        self.get_logger().info('Parametros iniciado')
        # self.declare_parameter("parametro_inteiro", rclpy.Parameter.Type.INTEGER)
        # self.declare_parameter("parametro_string", rclpy.Parameter.Type.INTEGER)
        
        self.declare_parameters(
            namespace='',
            parameters=[
                ('parametro_inteiro', Parameter.Type.INTEGER),
                ('parametro_string', Parameter.Type.STRING),
                ('parametro_booleano', Parameter.Type.BOOL),
            ]
        )
        
        self.parametro_inteiro = self.get_parameter("parametro_inteiro").get_parameter_value().integer_value
        self.parametro_string = self.get_parameter("parametro_string").get_parameter_value().string_value
        self.parametro_booleano = self.get_parameter("parametro_booleano").get_parameter_value().bool_value
        # # self.lista = self.get_parameter("lista").get_parameter_value().string_array_value
        
        
        self.get_logger().info(f'parametro_inteiro: {self.parametro_inteiro}')
        self.get_logger().info(f'parametro_string: {self.parametro_string}')
        self.get_logger().info(f'parametro_booleano: {self.parametro_booleano}')
        # self.get_logger().info(f'lista: {self.lista}')
        

def main(args=None):
    rclpy.init(args=args)
    parametros =  Parametros()
    rclpy.spin(parametros)
    rclpy.shutdown()
    
    
    
if __name__ == '__main__':
    main()
    