import time
from player import *
from confirm import *
from tube import *
from turn import *

WIN_SCORE = 13

class Game:
    def __init__(self, players):
        self.allPlayers = players

    def __reset(self):
        for j in self.allPlayers:
            j.brains = 0

    def __orderPlayers(self, players, initialPlayer):
        index = players.index(initialPlayer)
        orderedPlayers = players[index:len(players)]
        orderedPlayers.extend(players[0:index])
        return orderedPlayers

    def __getWinners(self):
        winners = []
        maxScore = 0
        for j in self.allPlayers:
            if j.brains > maxScore:
                maxScore = j.brains
        for j in self.allPlayers:
            if j.brains == maxScore:
                winners.append(j)
        return winners

    def __playTurn(self, player):
        tube = Tube()
        turn = Turn()
        keepPlaying = True
        print(f"\n{player.name}'s turn")
        time.sleep(1)
        while keepPlaying and turn.shots < 3:
            turn.rollDices(tube)
            if turn.shots >= 3:
                print ("Limited of 3 shots reached, turn passed")
                time.sleep(1)
            else:
                print(f"You have {turn.brains} brain(s) this turn, totals: {player.brains + turn.brains} brain(s), {len(turn.stepDices)} step(s), {turn.shots} shot(s).")
                time.sleep(1)
                keepPlaying = confirm("Do you want to play 3 more dices Y/N? ")
                # if stopped, compute score
                if not keepPlaying:
                    player.brains += turn.brains
        print(f"{player.name} has {player.brains} brain(s)")
        time.sleep(1)

    def play(self, initialPlayer):
        players = self.__orderPlayers(self.allPlayers, initialPlayer)
        self.__reset()
        # play until someone reaches the goal score
        finalTurn = False
        while not finalTurn:
            for player in players:
                self.__playTurn(player)
                if player.brains >= WIN_SCORE:
                    print (f"Reached {player.brains} brains!!")
                    print("This is the final turn!")
                    time.sleep(1)
                    finalTurn = True
                    break
        # play the final turn until have only 1 winner
        players = self.__orderPlayers(self.allPlayers, player)
        skipWinning = True # skip the winning player in the first round
        while True:
            for player in players:
                if skipWinning:
                    skipWinning = False
                    continue
                self.__playTurn(player)
            # calculate the winners
            winners = self.__getWinners()
            # if only 1 winner, finish the game
            if len(winners) == 1:
                winner = winners[0]
                print("\nThe winner is", winner.name)
                time.sleep(1)
                break
            else:
                # tiebreak needed for the winners
                players = winners
                print("\nThe winners are:")
                for w in winners:
                    print(w.name)
                print("\nTiebreaker round!")
                time.sleep(1)
        return winner