class Item:
    def __init__(self, name, description):
        self.name = name
        self.description = description
        self.current_room = None


class Food(Item):
    def __init__(self, name, description, calories):
        super().__init__(name, description)
        self.calories = calories


class Weapon(Item):
    def __init__(self, name, description, type_of_weapon):
        super().__init__(name, description)
        self.type_of_weapon = type_of_weapon


class Gun(Weapon):
    def __init__(self):
        super().__init__("gun", "automatic gun", "automatic weapon")
