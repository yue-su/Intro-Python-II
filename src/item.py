class Item:
    def __init__(self, name, description):
        self.name = name
        self.description = description
        self.current_room = None


class Food(Item):
    def __init__(self, name, description, calories):
        super().__init__(name, description)
        self.calories = calories
