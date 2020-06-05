# Write a class to hold player information, e.g. what room they are in
# currently.
import item
class Player:
    
    # setting params to attributes
    def __init__(self, name, currentRoom):
        self.inventory = ['rope']
        self.name = name
        self.currentRoom = currentRoom


        ##giving the player the ability to move
    def move(self, direction):
        if self.currentRoom.connections[direction] is None:
            self.currentRoom = self.currentRoom.connections[direction]
        else:
            print("your cannot move in that direction.")

        #this will give the player te ablity to pick up and add nto inventory
    def add(self, newItem):
        pass

  

    def print_inventory(self):
        for item in self.inventory:
            print(item,'\n')





        

    
    





        

