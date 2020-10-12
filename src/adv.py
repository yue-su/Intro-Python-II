from room import Room
from player import Player
from item import Item, Food, Weapon, Gun
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

room['outside'].n_to = room['foyer']
room['foyer'].s_to = room['outside']
room['foyer'].n_to = room['overlook']
room['foyer'].e_to = room['narrow']
room['overlook'].s_to = room['foyer']
room['narrow'].w_to = room['foyer']
room['narrow'].n_to = room['treasure']
room['treasure'].s_to = room['narrow']

rock = Item("rock", "This is a rock.")
sandwich = Food("sandwich", "some normal sandwiches", 100)
gun = Gun()
#
# Main
#

room['outside'].items.append(gun)

# Make a new player object that is currently in the 'outside' room.

player = Player(input("enter your name: "), room['outside'])
player.items.append(rock)
player.items.append(sandwich)
print(f"Hello , {player.name}")


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

# LOOP
while True:
    # READ
    cmd = input("\n~~~> ")
    cmd_list = cmd.split(" ")
    # EVAL
    if len(cmd_list) == 1:
        if cmd == "q":
            print("Goodbye!")
            exit(0)
        elif cmd in ("n", "s", "e", "w"):
            player.travel(cmd)
        elif cmd == 'i':
            player.print_inventory()
    if len(cmd_list) == 2:
        if cmd_list[0] == 'take':
            for item in player.current_room.items:
                if item.name == cmd_list[1]:
                    player.items.append(item)
            # player.current_room.items.remove(cmd_list[1])
            print("the current room items list is: ")
            player.current_room.get_items()
            print("the player's items list is: ")
            player.print_inventory()
        if cmd_list[0] == 'drop':
            player.current_room.items.append(cmd_list[1])
            # player.items.remove(cmd_list[1])
            print("the current room items list is: ")
            for item in player.current_room.items:
                print(f"{item}")
            print("the player's items list is: ")
            for item in player.items:
                print(f"{item}")
    else:
        print("I did not understand the command!")
