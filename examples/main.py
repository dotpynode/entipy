import sys
import os

dir = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.dirname(dir))

from entipy import entity, component, manager, system, components

def main():
    m = manager.Manager()
    for i in range (0,100):
        id = i + 1
        sid = 'obj ' + str(id)

        # create entity
        e = entity.Entity(id)
        m.add_entity(e)

        # add components
        c = components.componentname.ComponentName(sid)
        m.add_component(e, c)
    
    

if __name__ == "__main__":
    main()