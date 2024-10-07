import os
from glob import glob
from setuptools import find_packages, setup

package_name = 'robot_description'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
        (os.path.join('share', package_name, 'config'), glob(os.path.join('config', '*'))),
        (os.path.join('share', package_name, 'meshes'), glob(os.path.join('meshes', '*'))),
        (os.path.join('share', package_name, 'gazebo'), glob(os.path.join('gazebo', '*'))),
        (os.path.join('share', package_name, 'robots'), glob(os.path.join('robots', '*'))),
        (os.path.join('share', package_name, 'ros2_control'), glob(os.path.join('ros2_control', '*'))),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='scott-pena',
    maintainer_email='scott-pena@todo.todo',
    description='TODO: Package description',
    license='Apache-2.0',
    # tests_require=['pytest'],
    entry_points={
        'console_scripts': [
        ],
    },
)
