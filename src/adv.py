from room import Room
from player import Player
from item import Item
import textwrap
# Declare all the rooms




Backpack = Item('Backpack', 'To store your stuff')
Flashlight: Item('Flashlight', "I can now see")
Sword = Item('Sword', 'You need this to protect yourself')
Bow = Item('Bow', 'bow to shot long distances')
Treasure = Item("Treasure chest", "Someone took all of it")






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





room['outside'].n_to = room['foyer']
room['foyer'].s_to = room['outside']
room['foyer'].n_to = room['overlook']
room['foyer'].e_to = room['narrow']
room['overlook'].s_to = room['foyer']
room['narrow'].w_to = room['foyer']
room['narrow'].n_to = room['treasure']
room['treasure'].s_to = room['narrow']




outside = room["outside"]
foyer = room["foyer"]
overlook = room["overlook"]
narrow = room["narrow"]
treasure = room["treasure"]


outside.add_items(Backpack, Flashlight)
foyer.add_items(Sword)
overlook.add_items(Bow)
treasure.add_items(Treasure)





#
# Main
#

# Make a new player object that is currently in the 'outside' room.
name = input("\n What is your name? : ")
player = Player(name, room['outside'])

# Write a loop that:
while True:
    print(player.current_room.name)
    print(player.current_room.description)
    if  len(player.current_room.items) >= 1:
        print("\n<<< Items in this room >>>")
    for item in player.current_room.items:
        print(f" {item.name}: {item.description}")
    if len(player.current_room.items) == 0:
        print("\n<<< No items in this room >>>")

    Input = input(f"Which direction do you want to go?: ")

    if (Input == 'n'):
         player.current_room = player.current_room.n_to
    elif  (Input == 'w'):
        player.current_room = player.current_room.w_to
    elif (Input =='s'):
        player.current_room = player.current_room.s_to
    elif (Input == 'e'):
        player.current_room = player.current_room.e_to
    elif (Input == 'q'):
          print(f"Thanks for playing")
          break
    elif (Input == 'i'):
        print(f"\n<<< Player inventory >>>")
        for item in player.inventory:
            print(f" {item.name}: {item.description}") 


    elif(Input.split()[0] == 'Get'):
        for item in player.current_room.items:
            if item.name == Input.split()[1]:
               player.pick_item(item)
               print(f"\n<<< You picked up the{Input[3:]} >>>")

    elif(Input.split()[0] == 'Set'):
        for item in player.inventory:
            if item.name == Input.split()[1]:
               player.drop_item(item)
               print(f"\n<<< You dropped up your{Input[3:]} >>>")

    elif(Input == 'Command'):
        print(f" \n<<< n = Go North, e = Go East, s = Go South, w = Go West, Get [ITEM NAME] = Add item to inventory,\n Drop [ITEM NAME] =Drop item from inventory, i = Inventory, q = Quit game >>>")

    else: print(f"That's the wrong key")

   
   
    
# * Prints the current room name
# * Prints the current description (the textwrap module might be useful here).
# * Waits for user input and decides what to do.
#
# If the user enters a cardinal direction, attempt to move to the room there.
# Print an error message if the movement isn't allowed.
#
# If the user enters "q", quit the game.
