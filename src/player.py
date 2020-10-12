# Write a class to hold player information, e.g. what room they are in
# currently.
class Player:
    def __init__(self, name, starting_room):
        self.name = name
        self.current_room = starting_room
        self.items = []

    def travel(self, direction):
        if getattr(self.current_room, f"{direction}_to") is not None:
            self.current_room = getattr(self.current_room, f"{direction}_to")
            print(self.current_room)
            for item in self.current_room.items:
                print(f"Items in this Room: {item.name}")
        else:
            print("You cannot move in that direction")

    def print_inventory(self):
        print("holding:")
        for item in self.items:
            print(item.name)