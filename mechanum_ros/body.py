import bge
from collections import OrderedDict

# System
import threading
import sys

# ROS
from mechanum_interface.srv import SetWheelVelo
import rclpy
from rclpy.node import Node
from time import sleep


class MinimalService(Node):

    def __init__(self, parent):
        super().__init__('minimal_service')
        self.srv = self.create_service(SetWheelVelo, 'set_wheel_velo', self.set_wheel_velo_callback)
        self.parent = parent

    def set_wheel_velo_callback(self, request, response):
        #response.sum = 42
        self.parent.fl = request.fl
        self.parent.fr = request.fr
        self.parent.bl = request.bl
        self.parent.br = request.br
        self.parent.request = True
        self.get_logger().info('Incoming request\nfl: %f fr: %f bl: %f br: %f' % (request.fl, request.fr, request.bl, request.br))

        return response

def runRos(parent):
    print("thread started")
    minimal_service = MinimalService(parent)

    rclpy.spin(minimal_service)
    

class RosInterface(bge.types.KX_PythonComponent):
    # Put your arguments here of the format ("key", default_value).
    # These values are exposed to the UI.
    args = OrderedDict([
    ])

    def __del__(self):
        rclpy.shutdown()
        print("shutdown")
    
    def start(self, args):
        # Put your initialization code here, args stores the values from the UI.
        # self.object is the owner object of this component.
        # self.object.scene is the main scene.

        self.fl = 0
        self.fr = 0
        self.bl = 0
        self.br = 0
        self.request = False

        # Create and run thread object with the given function
        print("ROS interface thread startup")
        rclpy.init()
        self.rosThread = threading.Thread(target=runRos, args=(self,))
        self.rosThread.setDaemon(True)
        self.rosThread.start()        

    def update(self):
        # Put your code executed every logic step here.
        # self.object is the owner object of this component.
        # self.object.scene is the main scene.

        # Sleep to allow interface a little bit of CPU
        sleep(0.002)

        if self.request:
            obj = self.object.scene.objects["Cylinder"]
            obj.components["Controller"].setSpeed( self.fl )

            obj = self.object.scene.objects["Cylinder.001"]
            obj.components["Controller"].setSpeed( self.fr )

            obj = self.object.scene.objects["Cylinder.002"]
            obj.components["Controller"].setSpeed( self.bl )

            obj = self.object.scene.objects["Cylinder.003"]
            obj.components["Controller"].setSpeed( self.br )
            self.request = False
            sleep(0.002)
            