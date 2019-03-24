from random import randint, choice

class card:
    """
    The card class contains the dog's name
    and other attributes which are randomly
    generated.
    """
    def __init__(self, name):
        self.name = name
        self.attrs = [
            randint(1, 5),   # exercise
            randint(1, 100), # intelligence
            randint(1, 10),  # friendliness
            randint(1, 10)   # drool
        ]
    def __repr__(self):
        return "<card_class name:{} attrs:{}>".format(self.name, self.attrs)
    def display(self, point=-1):
        side = '-' * (len(self.name) + 6)
        attrs = self.attrs.copy()
        if point>=0: attrs[point] = str(attrs[point]) + '\t<---'

        print(side + '\nName: {}\nExercise: {}\nIntelligence: {}\nFriendliness: {}\nDrool: {}\n'.format(
            self.name,
            *attrs) + side)