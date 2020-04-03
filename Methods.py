class Player:
    """Player-class: stores data on team colors and points."""
    teamcolor = "Blue"
    __points = 0

    def tellscore(self):
        print("I am a ", self.teamcolor, "and we have ", self.__points, "points!")

    def goal(self):
        self.__points = self.__points + 1


def main():
    team = Player()
    team.goal()
    team.tellscore()


if__name__ = "__main__"
main()


