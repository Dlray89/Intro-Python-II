# Implement a class to hold room information. This should have name and
# description attributes.



class Room:
    def __init__(self, name, description, n_to=None, s_to=None, e_to=None, w_to=None, items=True):
        self.name = name
        self.description = description
        self.connections = {
            'n': n_to,
            's': s_to,
            'e': e_to,
            'w': w_to
        }
        self.items = [
            'map',
            'key',
            'torch',
            'Book'
        ]

    def about(self):
        print(f'This is the {self.name} and its purpose  {self.description}. There is an {self.items} in the room')

   
        
   
     

        
dining = Room('dining','is to eat dining here')

dining.about()




        



# outside = Room('outside', 'Outside Cave Entrance', 'N', 'map' )
# foyer = Room('floyer', 'Dim light filters in from the south')
# overlook = Room('overlook', 'Grand Overlook')
# narrow = Room('narrow', 'Narrow Passage')
# treasure = Room('treasure', 'Treasure Chamber')

# outside.About_room()
# foyer.About_room()
# overlook.About_room()
# narrow.About_room()
# treasure.About_room()

        

        
       
