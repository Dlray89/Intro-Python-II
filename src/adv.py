from room import Room
from player import Player
from item import Item

# Declare all the rooms

room = {
    'outside':  Room("Outside Cave Entrance",
                     "North of you, the cave mount beckons"),

    'foyer':    Room("Foyer", """ A Dim light filters in from the south and Dusty
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

item = {
    'Torch': Item('A Torch', """an item that will give you light""" )
}

# Link rooms together

room['outside'].n_to = room['foyer']
room['foyer'].s_to = room['outside']
room['foyer'].n_to = room['overlook']
room['foyer'].e_to = room['narrow']
room['overlook'].s_to = room['foyer']
room['narrow'].w_to = room['foyer']
room['narrow'].n_to = room['treasure']
room['treasure'].s_to = room['narrow']



#
# Main
#REPL - Read, Evaluate, Print, Loop

# # Make a new player object that is currently in the 'outside' room.
player = Player()

# player name input
game = True
if game:
    player.name = input('Enter your name adventurer: ')
    print('Are you ready to begin your adventure ' + player.name)

# yes or no for player to start game

yes_or_no = input('yes or no: ')
if yes_or_no == 'yes':
    print('lets begin')
elif yes_or_no == 'no':
    print('Your not ready')
else:
    print('You enter an invaild command')
print('--------------------------------------------------------------------')

# players current position
player.current_room = room['outside']
print(str(player.current_room) + ' ' + 'and' + ' ' + player.name + ' heads in to take a look')
print(player.name + 'takes a look around and right in front of you are two additional paths.')
print('To the North is' + str(room['foyer']) + '.')
print('To the East is ' + str(room['narrow']) + '.')
print('and south leads back outside')
print('-------------------------------------------------------------------')

# input for player to decide which way to go in the cave
direction = input('Which way would you like to go n or e or s: ')
if direction == 'n':
    player.current_room = room['foyer']

    print('As ' + player.name + ' walks up the dark tunnel you notice an item on the ground ' + '.')
    grab = input('Would you like to pick up the item?: yes or no ')
    if grab == 'yes':
        print(' you have picked up a ' + str(item['Torch']))
    elif grab == 'no':
        print('You continue to walk down the tunnel')
    else:
        print('choose a valid selections')

    print('You have enter the ' + '' + str(player.current_room))
elif direction == 'e':
    player.current_room = room['narrow']
    print(room['narrow'])
elif direction == 's':
    player.current_room = room['outside']
    print('You are back ' + '' + player.current_room)
else:
    print("you cant go that way")







# Write a loop that:
#
# * Prints the current room name
# * Prints the current description (the textwrap module might be useful here).
# * Waits for user input and decides what to do.


#
# If the user enters a cardinal direction, attempt to move to the room there.
# Print an error message if the movement isn't allowed.
#
# If the user enters "q", quit the game.
