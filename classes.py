from random import randint, choice

HELP_MSG='\tYou will be presented with the card\n\ton top of your pile. You then chose a category\n\t(exercise, intelligence, friendliness, drool) to play.\n\tIf you chose a category that is higher than\n\tthe computer\'s card then you win (unless you chose drool)\n\tand take the computer\'s card. If the computer wins vice versa.\n\tThe final winner is crowned when their opponent has no cards left.'

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
