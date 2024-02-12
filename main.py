from player import Player
from dice import Dice
from turns import Turns
from jumper import Ladders, Snakes

class SnakeLadder:
    def __init__(self, boardSize, diceNum):
        self.players = []
        self.truns = Turns()
        self.dice = Dice(diceNum)
        self.boardSize = boardSize
        self.board = [n for n in range(1, self.boardSize + 1)]
        self.playerPositions = {}
        self.ladders = Ladders()
        self.snakes = Snakes()

    def AddPlayer(self, name):
        self.players.append(Player(name))

    def Start(self):
        for player in self.players:
            self.truns.put(player)
            self.playerPositions[player.name] = 0

        while(self.truns.Size() > 1): 
            
            currentPlayer = self.truns.pop()
            print(f">> {currentPlayer.name}'s chance, press 'r' to roll dice:")

            rollDice = input()
            
            if rollDice == "r":
                diceValue = self.dice.Roll()
                print(f"{currentPlayer.name} got {diceValue}")

                currentPositions = self.playerPositions[currentPlayer.name]
                nextPosition = currentPositions + diceValue
                
                if nextPosition > self.boardSize:
                    self.truns.put(currentPlayer)
                    print(f"{currentPlayer.name} is at {currentPositions}")
                    pass
                elif nextPosition == self.boardSize:
                    print(f"{currentPlayer.name} won the game!")
                    return
                else:
                    if self.ladders.Check(nextPosition):
                        self.playerPositions[currentPlayer.name] = self.ladders.Jump(nextPosition)
                        print(f"[+] {currentPlayer.name} got ladder from {nextPosition} to {self.playerPositions[currentPlayer.name]}")
                        print(f"{currentPlayer.name} moved to {self.playerPositions[currentPlayer.name]}")
                    elif self.snakes.Check(nextPosition):
                        self.playerPositions[currentPlayer.name] = self.snakes.Jump(nextPosition)
                        print(f"[-] {currentPlayer.name} bitten by snake from {nextPosition} to {self.playerPositions[currentPlayer.name]}")
                        print(f"{currentPlayer.name} moved to {self.playerPositions[currentPlayer.name]}")
                    else:
                        self.playerPositions[currentPlayer.name] = nextPosition
                        print(f"{currentPlayer.name} moved to {nextPosition}")
                    self.truns.put(currentPlayer)                

                
            else:
                print("invalid operation")

game = SnakeLadder(100, 1)

#Add Ladders
game.ladders.Add(1, 38)
game.ladders.Add(4, 14)
game.ladders.Add(28, 84)

#Add Snakes
game.snakes.Add(17, 7)
game.snakes.Add(54, 34)
game.snakes.Add(62, 19)
game.snakes.Add(93, 73)

#Add Players
game.AddPlayer("Raja")
game.AddPlayer("Rani")

#Start the game
game.Start()
