import bge

def main():

    cont = bge.logic.getCurrentController()
    own = cont.owner

    sens_fl = cont.sensors['Keyboard_left']
    sens_fr = cont.sensors['Keyboard_up']
    sens_bl = cont.sensors['Keyboard_down']
    sens_br = cont.sensors['Keyboard_right']

    max_spd = own["max_spd"]

    obj = own.scene.objects["Cylinder"]
    obj.components["Controller"].setSpeed( sens_fl.positive * max_spd )

    obj = own.scene.objects["Cylinder.001"]
    obj.components["Controller"].setSpeed( sens_fr.positive * max_spd )

    obj = own.scene.objects["Cylinder.002"]
    obj.components["Controller"].setSpeed( sens_bl.positive * max_spd )

    obj = own.scene.objects["Cylinder.003"]
    obj.components["Controller"].setSpeed( sens_br.positive * max_spd )

main()
