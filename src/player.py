# Write a class to hold player information, e.g. what room they are in
# currently.

class Player:
    def __init__(self, name, currentRoom):
        self.name = name
        self.currentRoom = currentRoom
    
    def set_name(self, name):
        if not name:
                raise Exception('Invaild Name')
        self.name = name
    def get_name (self):
        return self.name
    name = property(get_name, set_name)


player = Player('Dave', "outside")
print(player.name)


        

