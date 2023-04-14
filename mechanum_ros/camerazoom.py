import bge


def main():

    cont = bge.logic.getCurrentController()
    own = cont.owner

    ms_up = cont.sensors['mouse_up']
    ms_down = cont.sensors['mouse_down']
    #actu = cont.actuators['myActuator']

    if ms_up.positive:
        #pos = own.localPosition.normalized()
        own.applyMovement((0,0,-0.5), True)
    elif ms_down.positive:
        own.applyMovement((0,0,0.5), True)

main()
