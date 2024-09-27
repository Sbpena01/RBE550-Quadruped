import sys
if sys.prefix == '/home/sbpena01/.local/share/pipx/venvs/colcon-common-extensions':
    sys.real_prefix = sys.prefix
    sys.prefix = sys.exec_prefix = '/home/sbpena01/GitHub/RBE550-Quadruped/install/leg_controls'
