from setuptools import find_packages, setup
import os
from glob import glob
from setuptools import setup
from setuptools import find_packages

package_name = 'leg_controls'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
        (os.path.join('lib', package_name, 'leg_controls'), glob(os.path.join('leg_controls', '*'))),
        (os.path.join('share', package_name, 'launch'), glob(os.path.join('launch', '*'))),
        (os.path.join('share', package_name), glob('gazebo/*')),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='sbpena01',
    maintainer_email='sbpena01@gmail.com',
    description='TODO: Package description',
    license='Apache-2.0',
    # tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'FrontLeftLeg = leg_controls.FrontLeftLeg:main',
            'FrontRightLeg = leg_controls.FrontRightLeg:main',
            'RearLeftLeg = leg_controls.RearLeftLeg:main',
            'RearRightLeg = leg_controls.RearRightLeg:main',
            # 'state_publisher = leg_controls.state_publisher:main'
        ],
    },
)
