class Player:
    teamcolor = ""
    points = ""


def main():
    Team = Player()
    Team.teamcolor = "Blue"
    Team.points = 300
    print("The ", Team.teamcolor, "contender has ", Team.points, "points!")


if __name__ == '__main__':
    main()
