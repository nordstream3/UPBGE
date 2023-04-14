import bge
from collections import OrderedDict
from math import fabs
from mathutils import Vector

class Controller(bge.types.KX_PythonComponent):
    # Put your arguments here of the format ("key", default_value).
    # These values are exposed to the UI.
    args = OrderedDict([
    ])

    def set(self, dx, dy, dz):
        self.dx = dx
        self.dy = dy
        self.dz = dz
        
    def setEject(self, dx, steps):
        self.stored_friction = self.friction_mover.friction
        self.friction_mover.friction = 0.
        self.i = 0
        self.eject_dx = dx
        self.eject_steps = steps + 2

    def start(self, args):
        # Put your initialization code here, args stores the values from the UI.
        # self.object is the owner object of this component.
        # self.object.scene is the main scene.
        self.dx = 0.
        self.dy = 0.
        self.dz = 0.
        self.friction_mover = self.object.scene.objects["Conveyor_mover"]
        self.texture_mover = self.object.scene.objects["Conveyor_origo"]
        self.belt_core = self.object.scene.objects["BeltCore"]
        self.eject_steps = 0

    def update(self):
        # Put your code executed every logic step here.
        # self.object is the owner object of this component.
        # self.object.scene is the main scene.
        
        if self.eject_steps > 0:
            if self.i > 1:
                if self.i < self.eject_steps:
                    self.object.applyMovement((-self.eject_dx, 0, 0))
                    self.friction_mover.applyMovement((-self.eject_dx, 0, 0))
                    self.belt_core.applyMovement((-self.eject_dx, 0, 0))
                    self.texture_mover.applyMovement((2*self.eject_dx, 0, 0))
                else:
                    self.eject_steps = 0
                    self.friction_mover.friction = self.stored_friction
                    self.object.applyMovement((0, 0, 0))
                    self.friction_mover.applyMovement((0, 0, 0))
                    self.belt_core.applyMovement((0, 0, 0))
                    self.texture_mover.applyMovement((0, 0, 0))
            self.i += 1
            return
        
        if fabs(self.dx)>0.00001 or fabs(self.dy)>0.00001 or fabs(self.dz)>0.00001:
            
            dx = self.dx
            dy = self.dy
            dz = self.dz
            pos = self.object.localPosition + Vector((dx,dy,dz))
            if pos.x > 9.4812 and dx > 0:
                dx = 0
            if pos.y > 1.2917 and dy > 0:
                dy = 0
            if pos.y < -1.3 and dy < 0:
                dy = 0
            if pos.z < 0.4706 and dz < 0:
                dz = 0
            
            self.object.applyMovement((dx, dy, dz))
            self.friction_mover.applyMovement((dx, dy, dz))
            self.belt_core.applyMovement((dx, dy, dz))
            self.texture_mover.applyMovement((-dx, 0, 0))
