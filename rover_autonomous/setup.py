from setuptools import find_packages, setup

package_name = 'rover_autonomous'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='aryaanb17',
    maintainer_email='aryaanb17@todo.todo',
    description='TODO: Package description',
    license='TODO: License declaration',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'publish_coords = rover_autonomous.obstacle:main',
            'navigate = rover_autonomous.navigation:main'
        ],
    },
)
