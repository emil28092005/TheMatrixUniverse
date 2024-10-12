import numpy as np

class Entity:
    position = np.array([0,0])
    name = ""
    def __init__(self, InitialPosition, name):
        self.position = InitialPosition
        self.name = name
    
    
class Actor(Entity):
    perceptionRadius = 0
    percievedCells = None 
    def __init__(self, InitialPosition, name, perceptionRadius):
        super().__init__(InitialPosition, name)
        self.perceptionRadius = perceptionRadius
    
    
class Neo(Actor):
    keyMakerPosition = np.array([0,0])
    def __init__(self, InitialPosition, perceptionRadius, keyMakerPosition):
        super().__init__(InitialPosition, "Neo", perceptionRadius)
        self.keyMakerPosition = keyMakerPosition

class Smith(Actor):
    def __init__(self, InitialPosition, perceptionRadius):
        super().__init__(InitialPosition, "Smith", perceptionRadius)
    def Kill():
        print("Neo is killed.") #TODO: delete    

class Sentinel(Actor):
    def __init__(self, InitialPosition, perceptionRadius):
        super().__init__(InitialPosition, "Sentinel", perceptionRadius)
    def Kill():
        print("Neo is killed.") #TODO: delete

class Keymaker(Entity):
    def __init__(self, InitialPosition):
        super().__init__(InitialPosition, "Keymaker")

class BackdoorKey(Entity):
    def __init__(self, InitialPosition):
        super().__init__(InitialPosition, "BackdoorKey")


