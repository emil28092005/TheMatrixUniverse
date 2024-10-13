from tools import *

class entity:
    position = Vector2(0,0)
    name = ""
    def __init__(self, initial_position, name):
        self.position = initial_position
        self.name = name

class actor(entity):
    perception_radius = 0
    perceived_cells = None 
    def __init__(self, initial_position, name, perception_radius):
        super().__init__(initial_position, name)
        self.perception_radius = perception_radius

class neo(actor):
    key_maker_position = Vector2(0,0)
    def __init__(self, initial_position, perception_radius, key_maker_position):
        super().__init__(initial_position, "neo", perception_radius)
        self.key_maker_position = key_maker_position

class smith(actor):
    def __init__(self, initial_position, perception_radius):
        super().__init__(initial_position, "smith", perception_radius)
    def kill():
        print("Neo is killed.") #TODO: delete

class sentinel(actor):
    def __init__(self, initial_position, perception_radius):
        super().__init__(initial_position, "sentinel", perception_radius)
    def kill():
        print("Neo is killed.") #TODO: delete

class key_maker(entity):
    def __init__(self, initial_position):
        super().__init__(initial_position, "key_maker")

class backdoor_key(entity):
    def __init__(self, initial_position):
        super().__init__(initial_position, "backdoor_key")
