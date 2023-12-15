from player import *

class InitialInput:

    @staticmethod
    def readNumOfPlayers():
        numOfPlayers = 0
        while True:
            numOfPlayers = input('How many players will participate? ')
            if not numOfPlayers.isdigit():
                print ('Type only digits')
                continue
            numOfPlayers = int(numOfPlayers)
            if 2 <= numOfPlayers <= 99:
                return numOfPlayers
            print('The quantity of players must be between 2 and 99')

    @staticmethod
    def readPlayerList(qty):
        players = []
        for i in range(qty):
            while True:
                name = input(f"Player's {i+1} name: ").strip()
                if len(name) < 2:
                    print('The name must have at least two chars')
                    continue
                if InitialInput.__getPlayerByName(players, name): # Testa se o player já existe na lista com aquele name.
                    print('Name repeated, try another name')
                    continue
                break
            players.append(Player(name))
        return players

    @staticmethod
    def readInitialPlayer(players):
        while True:
            name = input("Type the name of the player who said 'Brain' in the zombiest way: ").strip()
            initialPlayer = InitialInput.__getPlayerByName(players, name)
            if initialPlayer:
                return initialPlayer
            print("Player not found, try again.")

    @staticmethod
    def __getPlayerByName(players, name):
        for j in players:
            if j.name == name:
                return j
        return None