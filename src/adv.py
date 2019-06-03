from room import Room
from player import Player
from item import Item

# Declare all the rooms

room = {
    'outside':  Room("Outside Cave Entrance","North of you, the cave mount beckons"),

    'foyer':    Room("Foyer", """Dim light filters in from the south. Dusty
passages run north and east.""",[Item("POTION","Life giving Elixr")]),

    'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm.""",[Item("SWORD","A Hero's Weapon")]),

    'narrow':   Room("Narrow Passage", """The narrow passage bends here from west
to north. The smell of gold permeates the air.""",[Item("SHEILD","A Heros best friend"),Item("DAGGER","Up close and personal")]),

    'treasure': Room("Treasure Chamber", """You've found the long-lost treasure
chamber! Sadly, it is cursed. The choice is yours to tempt fate.The only exit is to the south.""",[Item("TREASURE","The beggining to a better life")]),
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
x = hasattr(room, 'outside')
# if hasattr(player1.current_room, "n_to"):
# player1.current_room = player1.current_room.n_to

#
# Main
#

selection= input("What is your name Traveler? Enter Name or q to quit:").strip()
# Make a new player object that is currently in the 'outside' room.
if selection.upper() != "Q":
    playerOne =Player(selection,room["outside"])
    print("Welcome " + str(playerOne.name) + " you are currently in " + str(playerOne.current_room))
    print("You can check your current Inventory by selecting i or Inventory")
    print("If there is an item in the room you can get it by typing get and the name of the item")
    print("If you wish to drop an item you can by typing drop and the name of the item")
    print("Like get potion and drop potion. Notice the space between the words")
while selection[0].upper() != "Q":
    selection = input("Choose an action or a direction N,S,E,W or Q to quit:").strip().split()
    while not selection:
        print("Please enter a valid selection fool!")
        selection = input("Choose an action or a direction N,S,E,W or Q to quit:").strip().split()
    if selection[0].upper() == "N":
        if hasattr(playerOne.current_room,"n_to"):
            playerOne.current_room = playerOne.current_room.n_to
            print("You are entering " + str(playerOne.current_room))
        else:
            print("Fool you can't go that way")
    elif selection[0].upper() == "S":
        if hasattr(playerOne.current_room,"s_to"):
            playerOne.current_room = playerOne.current_room.s_to
            print("You are entering " + str(playerOne.current_room))
        else:
            print("Fool you can't go that way")
    elif selection[0].upper() == "E":
        if hasattr(playerOne.current_room,"e_to"):
            playerOne.current_room = playerOne.current_room.e_to
            print("You are entering " + str(playerOne.current_room))
        else:
            print("Fool you can't go that way")
    elif selection[0].upper() == "W":
        if hasattr(playerOne.current_room,"w_to"):
            playerOne.current_room = playerOne.current_room.w_to
            print("You are entering " + str(playerOne.current_room))
        else:
            print("Fool you can't go that way")
    elif (selection[0].upper() == "GET" or selection[0].upper() == "TAKE") and (len(selection) == 2):
        if len(playerOne.current_room.items) > 0:
            playerOne.get_item(selection[1].upper())
            print(str(playerOne.current_room))
        else:
            print("No items in here")
    elif (selection[0].upper() == "DROP") and (len(selection) == 2):
        if len(playerOne.items) > 0:
            playerOne.drop_item(selection[1].upper())
            print(str(playerOne.current_room))
        else:
            print("No items to drop")
    elif (selection[0].upper() == "I") or (selection[0].upper() == "INVENTORY"):        
        playerOne.current_items()
    elif selection[0].upper() == "Q":
        break
    elif len(selection) > 2:
        print("Please enter a valid selection fool!")
    else:
        print("Please enter a valid selection fool!")
    

print('Goodbye!')

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
