import bge
from collections import OrderedDict
from mathutils import Vector
import math

class Navigation(bge.types.KX_PythonComponent):
    # Put your arguments here of the format ("key", default_value).
    # These values are exposed to the UI.
    args = OrderedDict([
    ])

    def start(self, args):
        # Put your initialization code here, args stores the values from the UI.
        # self.object is the owner object of this component.
        # self.object.scene is the main scene.
        self.keybd = bge.logic.keyboard
        self.mouse = bge.logic.mouse
        self.last_mspos = self.mouse.position
        self.lastMiddleMsState = False

        self.s_t = 150.
        self.s_r = 500.
        
        bge.render.showMouse(1)
        

    def update(self):
        # Put your code executed every logic step here.
        # self.object is the owner object of this component.
        # self.object.scene is the main scene.
        
        middleMsState = self.mouse.inputs[bge.events.MIDDLEMOUSE].values[-1]

        if middleMsState:
            mspos = Vector(self.mouse.position)
            mspos.x *= bge.render.getWindowWidth()
            mspos.y *= bge.render.getWindowHeight()

            if self.lastMiddleMsState:
                shiftKeyState = self.keybd.inputs[bge.events.LEFTSHIFTKEY].values[-1]
                dx = mspos.x - self.last_mspos.x
                dy = mspos.y - self.last_mspos.y

                if math.fabs(dx) > 0.001 or math.fabs(dy) > 0.001:
                    if shiftKeyState:
                        self.object.applyMovement((-dx/self.s_t, dy/self.s_t, 0), True)
                    else:
                        # look left/right
                        self.object.applyRotation((0,0,-dx/self.s_r),False)

                        # look up/down
                        self.object.applyRotation((-dy/self.s_r,0,0),True)

            self.last_mspos = mspos
            self.lastMiddleMsState = True

        else:
            self.lastMiddleMsState = False
