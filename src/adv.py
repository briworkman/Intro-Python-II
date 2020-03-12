import textwrap
import sys
import os

from room import Room
from player import Player

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

#
# Main
#

# Make a new player object that is currently in the 'outside' room.
player = Player("Me", room["outside"])
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
def move():
    while True:
        current_room = player.current_room
        print("Current Room: ", player.current_room.name)
        print("Room Description: ", player.current_room.description)
        print("Which way do you want to go?")
        direction = input("[n] North  [s] South  [e] East   [w]  West  [q] Quit -> ")
        if direction.lower() == "q":
            print("Goodbye!")
            break
        elif direction.lower() == "n" and player.current_room != None:
            if player.current_room.n_to is not None:
                print("Going North")
                player.current_room = current_room.n_to
                os.system("clear")
            else:
                print("You cannot go that way! Please choose another direction")
        elif direction.lower() == "s" and player.current_room != None:
            if player.current_room.s_to is not None:
                print("Going South")
                player.current_room = current_room.s_to
                os.system("clear")
            else:
                print("You cannot go that way! Please choose another direction")
        elif direction.lower() == "e" and player.current_room != None:
            if player.current_room.e_to is not None:
                print("Going Easet")
                player.current_room = current_room.e_to
                os.system("clear")
            else:
                print("You cannot go that way! Please choose another direction")
        elif direction.lower() == "w" and player.current_room != None:
            if player.current_room.w_to is not None:
                print("Going West")
                player.current_room = current_room.w_to
                os.system("clear")
            else:
                print("You cannot go that way! Please choose another direction")
        else:
            print("Please choose a proper direction!")
            direction = input("[n] North  [s] South  [e] East   [w] West  [q] Quit -> ")
            os.system("clear")


move()
