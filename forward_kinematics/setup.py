from setuptools import setup

package_name = 'forward_kinematics'

setup(
    name=package_name,
    version='0.0.0',
    packages=[package_name],
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='czj',
    maintainer_email='czj@todo.todo',
    description='TODO: Package description',
    license='TODO: License declaration',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
         'fw_client  = forward_kinematics.fw_client:main',
         'fw_server  = forward_kinematics.fw_server:main',
        
        ],
    },
)
