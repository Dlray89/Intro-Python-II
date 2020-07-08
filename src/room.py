# Implement a class to hold room information. This should have name and
# description attributes.
class Room:
    def __init__(self, name, description, n_to=None, s_to=None, w_to=None, e_to=None):
        self.name = name
        self.description = description
        self.n_to = n_to
        self.s_to = s_to
        self.e_to = e_to
        self.w_to = w_to
        
    def __str__(self):
        return f'{self.name}, {self.description}'

# outside = Room('Outside Cave Entrance', 'Outside Cave Entrance')
# foyer = Room('foyer', 'Dusty passages run north and east.')
# overlook = Room('Grand Overlook', 'A steep cliff appears before you')
# npassage = Room("Narrow Passage", 'The narrow passage bends here from west to north')
# tchambers = Room("Treasure Chamber", "You've found the long-lost treasure chamber!")
# print(outside.name, outside.description)
# print(foyer.name, foyer.description)
# print(overlook.name, overlook.description)
# print(npassage.name, npassage.description)
# print(tchambers.name, tchambers.description)