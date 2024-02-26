
## 1. Criando um workspace
O workspace é o local onde as aplicações do ROS são desenvolvidas.

* mkdir -p <workspace_name>/src

* cd <workspace_name>

* colcon build --symlink-install

* source install/setup.bash


## 2. Criando um pacote:
Os pacotes do ROS são uma forma de organizar o código.

* cd <workspace_name>/src

* ros2 pkg create --build-type ament_python --license Apache-2.0 <package_name>


## links:
* [ROS2](https://docs.ros.org/en/humble/index.html)
* [ROS2 Tutorials](https://docs.ros.org/en/humble/Tutorials.html)
* [ROS2 Messages](https://wiki.ros.org/common_msgs?distro=humble)

## Exemplos de mensagens:

* std_msgs/String
```python
from std_msgs.msg import String

msg = String()
msg.data = "Hello, World!"
```

* geometry_msgs/Twist
```python
from geometry_msgs.msg import Twist

msg = Twist()
msg.linear.x = 0.1
msg.angular.z = 0.3
```
