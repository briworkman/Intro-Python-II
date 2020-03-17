# Implement a class to hold room information. This should have name and
# description attributes.
from item import Item


class Room:
    def __init__(self, name, description):
        self.name = name
        self.description = description
        self.items = []
        self.n_to = None
        self.s_to = None
        self.e_to = None
        self.w_to = None

    def __str__(self):
        return_string = "---------"
        return_string += "\n\n"
        return_string += self.name
        return_string += "\n\n"
        return_string += self.description
        return_string += "\n\n"
        return_string += f"{self.get_exits_string()}"
        if len(self.items) >= 1:
            return_string += "\n\n"
            return_string += "You've found an item!"
            return_string += "\n"
            return_string += str(self.items[0])
            return_string += "\n"
            return_string += "Press [g] to pick it up!"
        else:
            return_string += "\n\n"
            return_string += "No items here!"
        return return_string

    def get_exits_string(self):
        exits = []
        if self.n_to:
            exits.append("n")
        if self.s_to:
            exits.append("s")
        if self.e_to:
            exits.append("e")
        if self.w_to:
            exits.append("w")
        return exits

