class Trick:
    def __init__(self,name, difficulty):
        self.name = name
        self.difficulty = difficulty
        self.trickList = []

    def tricks(self):
        theTricks = []
        for t in self.trickList:
            theTricks.append(t)
        print(theTricks)


    def leveledUp(self, level):
        original = self.difficulty
        self.difficulty += level
        print(f'Trick leveled up from {original} to {self.difficulty}')
        return self



# Creating trick instances
jump = Trick('Jumping Bricks', 2)
sit = Trick('Sit when told', 2)
speak = Trick('Bark on command', 1)
dance = Trick('Dance when asked', 9)
paw = Trick('Give 5 or shake hands', 5)

jump.tricks()
sit.tricks()
speak.tricks()
dance.tricks()
paw.tricks()
