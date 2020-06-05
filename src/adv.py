from room import Room
from player import Player
from item import Item
import textwrap

# Declare all the rooms

room = {
    'outside':  Room("Outside Cave Entrance",
                     "North of you, the cave mount beckons"),

    'foyer':    Room("Foyer", """Dim light filters in from the south. Dusty
passages run north and east."""),

    'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm."""),

    'narrow':   Room("Narrow Passage", """The narrow passage bends here from west
to north. The smell of gold permeates the air."""),

    'treasure': Room("Treasure Chamber", """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south."""),
}


# Link rooms together

room['outside'].connections['n'] = room['foyer']
room['foyer' ].connections['s'] = room['outside']
room['foyer'].connections['n'] = room['overlook']
room['foyer'].connections['e'] = room['narrow']
room['overlook'].connections['s'] = room['foyer']
room['narrow'].connections['w'] = room['foyer']
room['narrow'].connections['n'] = room['treasure']
room['treasure'].connections['s'] = room['narrow']
 


#
# Main
#

# Make a new player object that is currently in the 'outside' room.
player = Player('David', room['outside'] )
item = Item('map', room['outside'] )
print("this is the room current items",room['outside'].items)

print(player)
# Write a loop that:

user_is_playing = True

while user_is_playing:
    print("Hi im ",player.name, "I currently have a", player.inventory ,"in my inventory.","I am currenly", player.currentRoom.name)
    
    

    for line in textwrap.wrap(player.currentRoom.description):
        print(line)

    user_input = input('Which direction would you like to go? n/e/s/w: ')

    if user_input in [ 'n', 's', 'e', 'w']:
        player.move(user_input)
    else:
        print('You exited the game')
        user_is_playing = False

    
#
# * Prints the current room name
# * Prints the current description (the textwrap module might be useful here).
# * Waits for user input and decides what to do.


#
# If the user enters a cardinal direction, attempt to move to the room there.
# Print an error message if the movement isn't allowed.
#
# If the user enters "q", quit the game.
