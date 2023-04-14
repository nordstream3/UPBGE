import bge
import random

cont = bge.logic.getCurrentController()
own = cont.owner
key = bge.logic.keyboard.inputs
#sens = cont.sensors['Keyboard']

def foo(event):
    if key[event].values[-1] and key[event].active:
        val = bge.events.EventToString(event)
        own["key"] = val
        return True, val
    return False, ""

def getKeyActive():
    pressedKeyVal = own["key"]

    if pressedKeyVal != "":
        own["key"] = ""
        return False, pressedKeyVal

    active, val = foo(bge.events.LEFTARROWKEY)
    if (active):
        return True, val

    active, val = foo(bge.events.RIGHTARROWKEY)
    if (active):
        return True, val

    active, val = foo(bge.events.UPARROWKEY)
    if (active):
        return True, val

    active, val = foo(bge.events.DOWNARROWKEY)
    if (active):
        return True, val

    active, val = foo(bge.events.SPACEKEY)
    if (active):
        return True, val

    active, val = foo(bge.events.SKEY)
    if (active):
        return True, val

    active, val = foo(bge.events.AKEY)
    if (active):
        return True, val

    active, val = foo(bge.events.ZKEY)
    if (active):
        return True, val

    active, val = foo(bge.events.EKEY)
    if (active):
        return True, val

    return True, val

robot_step = 0.005

def main():
    
    robot_step = own["robot_spd_m_s"] / 60.
    
    active, val = getKeyActive()
    
    if active and val == "":
        print("No key pressed?")
        return

    if val == "LEFTARROWKEY":
        print("LEFTARROWKEY ", end="")
        comp = own.scene.objects["Belt"].components["Controller"]
        if active:
            print("active")
            comp.set(0, robot_step, 0)
        else:
            print("inactive")
            comp.set(0, 0, 0)
        
    if val == "RIGHTARROWKEY":
        print("RIGHTARROWKEY ", end="")
        comp = own.scene.objects["Belt"].components["Controller"]
        if active:
            print("active")
            comp.set(0, -robot_step, 0)
        else:
            print("inactive")
            comp.set(0, 0, 0)

    if val == "UPARROWKEY":
        print("UPARROWKEY ", end="")
        comp = own.scene.objects["Belt"].components["Controller"]
        if active:
            print("active")
            comp.set(0, 0, robot_step)
        else:
            print("inactive")
            comp.set(0, 0, 0)

    if val == "DOWNARROWKEY":
        print("DOWNARROWKEY ", end="")
        comp = own.scene.objects["Belt"].components["Controller"]
        if active:
            print("active")
            comp.set(0, 0, -robot_step)
        else:
            print("inactive")
            comp.set(0, 0, 0)

    if val == "AKEY":
        print("AKEY ", end="")
        comp = own.scene.objects["Belt"].components["Controller"]
        if active:
            print("active")
            comp.set(2*robot_step, 0, 0)
        else:
            print("inactive")
            comp.set(0, 0, 0)

    if val == "ZKEY":
        print("ZKEY ", end="")
        comp = own.scene.objects["Belt"].components["Controller"]
        if active:
            print("active")
            comp.set(-2*robot_step, 0, 0)
        else:
            print("inactive")
            comp.set(0, 0, 0)

    if val == "EKEY":
        print("EKEY ", end="")
        eject_dx = own["robot_eject_spd_m_s"] / 60.
        eject_steps = int(own["robot_eject_len_m"] / eject_dx)
        comp = own.scene.objects["Belt"].components["Controller"]
        if active:
            print("active")
            comp.setEject(eject_dx, eject_steps)
        else:
            print("inactive")

    if val == "SPACEKEY":
        print("SPACEKEY ", end="")
        conv_component = own.scene.objects["Conveyor_mover"].components["Controller"]
        if active:
            print("active")
            conv_component.setMove(True)
        else:
            print("inactive")
            conv_component.setMove(False)
    
    if val == "SKEY":
        print("SKEY ", end="")
        if active:
            print("active")
            scene = bge.logic.getCurrentScene()
            spawn_obj_ref = scene.objects["SpawnEmpty"]
            belt = scene.objects["Belt"]
            pos = belt.worldPosition.copy()
            pos.x += 1
            pos.z += 1
            spawn_obj_ref.worldPosition = pos
            pos = belt.localPosition.copy()
            pos.x += 1
            pos.z += 1
            spawn_obj_ref.localPosition = pos
            i = random.randint(0,1)
            if i==0:
                obj = scene.addObject("cardboard_simple", spawn_obj_ref, 0, 1)
            elif i==1:
                obj = scene.addObject("mashed_bag_white", spawn_obj_ref, 0, 1)
            elif i==2:
                obj = scene.addObject("Parcel_Bag", spawn_obj_ref, 0, 1)
            elif i==3:
                obj = scene.addObject("Cardboard_Box", spawn_obj_ref, 0, 1)

            xscale = random.uniform(0.5, 2.)
            yscale = random.uniform(0.4, 1.3)
            zscale = random.uniform(0.3, 1.1)
            obj.worldScale = (xscale, yscale, zscale)
            
        else:
            print("inactive")
    


#bge.events.LEFTARROWKEY
#bge.events.DOWNARROWKEY
#bge.events.RIGHTARROWKEY
#bge.events.UPARROWKEY¶


main()



