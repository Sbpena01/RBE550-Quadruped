import sys
if sys.prefix == '/usr':
    sys.real_prefix = sys.prefix
    sys.prefix = sys.exec_prefix = '/home/scott-pena/GitHub/RBE550-Quadruped/install/robot_description'
