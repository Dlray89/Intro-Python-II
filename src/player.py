# Write a class to hold player information, e.g. what room they are in
# currently.
from item import Item
class Player:
    def __init__(self, name, currentRoom):
        self.name = name
        self.currentRoom = currentRoom
        
    def move(self, direction):
        if self.currentRoom.connections[direction] is None:
            self.currentRoom = self.currentRoom.connections[direction]
        else:
            print("your cannot move in that direction.")
        

    
    





        

