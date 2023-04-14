import bge
from collections import OrderedDict

class LaserSensor(bge.types.KX_PythonComponent):
    # Put your arguments here of the format ("key", default_value).
    # These values are exposed to the UI.
    args = OrderedDict([("speed", 4.),("amplitude", 3.3)
    ])

    def start(self, args):
        # Put your initialization code here, args stores the values from the UI.
        # self.object is the owner object of this component.
        # self.object.scene is the main scene.
        self.pos = self.object.localPosition[1]
        self.step = args["speed"] / 60.
        self.amp_max = self.pos + args["amplitude"]
        self.amp_min = self.pos - args["amplitude"]

        #print(self.object.scene)
        #print(dir(self.object.scene))

    def update(self):
        # Put your code executed every logic step here.
        # self.object is the owner object of this component.
        # self.object.scene is the main scene.
        self.object.applyMovement((0, self.step, 0))

        if self.object.position[1] < self.amp_min or self.object.position[1] > self.amp_max:
            self.step = -self.step
