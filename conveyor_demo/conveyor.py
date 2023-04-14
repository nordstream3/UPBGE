import bge
from collections import OrderedDict
from math import fabs


class Controller(bge.types.KX_PythonComponent):
    # Put your arguments here of the format ("key", default_value).
    # These values are exposed to the UI.
    args = OrderedDict([ ("speed", 2.), ("acc", 2.), ("texture_obj", "Conveyor_origo")
    ])

    def setMove(self, val):
        if val:
            self.step_step = fabs(self.step_step)
        else:
            self.step_step = -fabs(self.step_step)
            
        self.step += self.step_step
        self.is_moving = val



    def start(self, args):
        # Put your initialization code here, args stores the values from the UI.
        # self.object is the owner object of this component.
        # self.object.scene is the main scene.
        
        self.is_moving = False
        self.max_step = args["speed"]/60.  #0.06
        self.step_step = args["acc"] / (60.*60.)
        self.step = 0. #self.step_step
        self.pulseframes =12
        self.i = 3
        self.fric = self.object.friction
        self.belt_core = self.object.scene.objects["BeltCore"]

        self.belt = self.object.scene.objects[ args["texture_obj"] ]


    def update(self):
        # Put your code executed every logic step here.
        # self.object is the owner object of this component.
        # self.object.scene is the main scene.
        if not self.is_moving and self.i > 2 and self.step < 0.000001:
            #self.step = self.step_step
            return

        step_x = self.step
        if self.i == 0:
            self.object.friction = 0.
        elif self.i == 1:
            step_x = self.belt_core.localPosition[0] - self.object.localPosition[0]
            #step_x = -self.step*(self.pulseframes-1)
        elif self.i == 2:
            self.object.friction = self.fric

        self.object.applyMovement((step_x,0.,0.))
        
        self.belt.applyMovement((self.step,0.,0.))

        self.i = (self.i+1) % self.pulseframes
        
        # Acceleration
        if self.step < self.max_step:
            self.step += self.step_step
            if self.step > self.max_step:
                self.step = self.max_step
        