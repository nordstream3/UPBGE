import bge
from collections import OrderedDict
from mathutils import Matrix, Euler
from math import pi, fabs, copysign


class Controller(bge.types.KX_PythonComponent):
    # Put your arguments here of the format ("key", default_value).
    # These values are exposed to the UI.
    args = OrderedDict([("wheel", "wheel"), ("body", "body"), ("acc", 5.),
    ])


    def start(self, args):
        # Put your initialization code here, args stores the values from the UI.
        # self.object is the owner object of this component.
        # self.object.scene is the main scene.
        self.wheel = self.object.scene.objects[args["wheel"]]
        self.cube = self.object.scene.objects[args["body"]]
        self.angle = 0
        self.accum_angle = 0

        self.init = self.object.localOrientation.copy()

        self.pos = 0
        self.speed = 0
        
        self.max_a = args["acc"] / (60.*60.)
        self.max_v = 0

    def setSpeed(self, val):
        self.max_v = val /60.
        print(self.object, self.max_v)


    def updateMecanum(self, dA):

        self.wheel.localPosition = self.object.localPosition
        
        # Find the absolute angle of the mechanum wheel
        newA = self.accum_angle + dA/0.707 # cos(45 deg)
        if newA > 2*pi:
            newA -= 2*pi
        elif newA < 0:
            newA += 2*pi
        self.accum_angle = newA
        self.wheel.localOrientation = self.cube.localOrientation @ Matrix.Rotation(newA, 3, 'Y')

        
    def update(self):
        # Put your code executed every logic step here.
        # self.object is the owner object of this component.
        # self.object.scene is the main scene.

        world2wheelorigin = self.cube.localOrientation @ self.init

        # describe rotation relative to wheel origin
        rot = world2wheelorigin.inverted() @ self.object.localOrientation

        # Find the incremental angle step of the Friction Wheel (this)
        eul = rot.to_euler()
        v = eul[1] - self.angle
        if fabs(v) > pi:
            if v < 0:
                v += 2*pi
            else:
                v -= 2*pi
        self.angle = eul[1]

        #v = dS
        a = self.max_v - v
        a *= 100.
        #fabs_a = min(fabs(a),self.max_a)
        #a = copysign(fabs_a,a)
        
        #v += a

        self.updateMecanum(v)

        #if self.max_v > 0:
        #    print(self.angle,dS,a)
            
        #self.object.applyRotation((0.,v,0.), True)
        self.object.applyTorque((0.,a,0.), True)

