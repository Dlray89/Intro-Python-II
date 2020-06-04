# Implement a class to hold room information. This should have name and
# description attributes.


class Room:
    def __init__(self, name, description):
        self.name = name
        self.description = description

    def set_room(self, name):
        if not name:
                raise Exception('invalid room name')
        self.name = name
    def get_room(self):
        return self.name
    name = property(get_room, set_room)


outside = Room('outside', 'Outside Cave Entrance')
foyer = Room('floyer', 'Dim light filters in from the south')
overlook = Room('overlook', 'Grand Overlook')
narrow = Room('narrow', 'Narrow Passage')
treasure = Room('treasure', 'Treasure Chamber')


print(outside.name)
print(foyer.name)

        

        
       
