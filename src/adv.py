from room import Room
from player import Player
from item import Item

# Declare all the rooms

room = {
    "outside": Room("Outside Cave Entrance", "North of you, the cave mount beckons"),
    "foyer": Room(
        "Foyer",
        """Dim light filters in from the south. Dusty
passages run north and east.""",
    ),
    "overlook": Room(
        "Grand Overlook",
        """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm.""",
    ),
    "narrow": Room(
        "Narrow Passage",
        """The narrow passage bends here from west
to north. The smell of gold permeates the air.""",
    ),
    "treasure": Room(
        "Treasure Chamber",
        """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south.""",
    ),
}


# Link rooms together

room["outside"].n_to = room["foyer"]
room["foyer"].s_to = room["outside"]
room["foyer"].n_to = room["overlook"]
room["foyer"].e_to = room["narrow"]
room["overlook"].s_to = room["foyer"]
room["narrow"].w_to = room["foyer"]
room["narrow"].n_to = room["treasure"]
room["treasure"].s_to = room["narrow"]

item = {
    "key": Item("Key", "This is a key. Use it to unlock the secret door."),
    "sword": Item("Sword", "This is a sword. Use it to fight your enemies."),
    "treasure": Item("Treasure", "This is the secret treasure. You've found it!"),
}

room["outside"].items.append(item["key"])
room["foyer"].items.append(item["sword"])
room["treasure"].items.append(item["treasure"])
#
# Main
#

# Make a new player object that is currently in the 'outside' room.
player = Player("Me", room["outside"], [])
print(player.current_room)
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

directions = ("n", "s", "e", "w")

while True:
    cmd = input("\nWhich way do you want to go? -> ")
    if cmd == "q":
        print("Goodbye!")
        break
    elif cmd in directions:
        player.travel(cmd)
    elif cmd == "i":
        print(player.print_inventory())
    elif cmd == "g":
        if player.current_room.items[0] == item["key"]:
            player.items.append(item["key"])
            player.current_room.items.remove(item["key"])
        elif player.current_room.items[0] == item["sword"]:
            player.items.append(item["sword"])
            player.current_room.items.remove(item["sword"])
        elif player.current_room.items[0] == item["treasure"]:
            player.items.append(item["treasure"])
            player.current_room.items.remove(item["treasure"])
    elif cmd == "d":
        if player.items[0] == item["key"]:
            player.items.remove(item["key"])
            player.current_room.items.append(item["key"])
        elif player.items[0] == item["sword"]:
            player.items.remove(item["sword"])
            player.current_room.items.append(item["sword"])
        elif player.items[0] == item["treasure"]:
            player.items.remove(item["treasure"])
            player.current_room.items.append(item["treasure"])
    else:
        print("Please choose a proper direction")
