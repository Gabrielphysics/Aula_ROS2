from launch import LaunchDescription
from launch_ros.actions import Node
from launch.substitutions import LaunchConfiguration
import os
from ament_index_python.packages import get_package_share_directory


def generate_launch_description():
    
    config = os.path.join(
        get_package_share_directory('meu_pacote'),
        'config',
        'param.yaml'
        )

    
    return LaunchDescription([
        
        # Node(
        #     package="meu_pacote",
        #     executable="publicador",
        #     name="publicador",
        # ), 
        # Node(
        #     package="meu_pacote",
        #     executable="assinante",
        #     name="assinante",
        # ),
        # Node(
        #     package="meu_pacote",
        #     executable="frame_fixo",
        #     name="frame_fixo",
        # ),
        Node(
            package="meu_pacote",
            executable="parametros",
            name="parametros",
            parameters=[
                {"parametro_inteiro":104},
                {'parametro_string': 'parametro_string'},
                {'parametro_booleano': True}
            ]
        ),
        Node(
            package="meu_pacote",
            executable="parametros",
            name="parametros",
            parameters=[config]
        ),
        
        
    ])