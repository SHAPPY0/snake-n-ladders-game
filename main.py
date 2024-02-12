from player import Player
from dice import Dice
from turns import Turns
from jumper import Ladders, Snakes

class SnakeLadder:
    def __init__(self, board_size, dice_num):
        self.players = []
        self.truns = Turns()
        self.dice = Dice(dice_num)
        self.board_size = board_size
        self.board = [n for n in range(1, self.board_size + 1)]
        self.player_positions = {}
        self.ladders = Ladders()
        self.snakes = Snakes()

    def AddPlayer(self, name):
        self.players.append(Player(name))

    def Start(self):
        for player in self.players:
            self.truns.put(player)
            self.player_positions[player.name] = 0

        while(self.truns.Size() > 1): 

            current_player = self.truns.pop()
            print(f">> {current_player.name}'s chance, press 'r' to roll dice:")

            roll_dice = input()
            
            if roll_dice == "r":
                dice_value = self.dice.Roll()
                print(f"{current_player.name} got {dice_value}")

                current_positions = self.player_positions[current_player.name]
                next_position = current_positions + dice_value
                
                if next_position > self.board_size:
                    self.truns.put(current_player)
                    print(f"{current_player.name} is at {current_positions}")
                    pass
                elif next_position == self.board_size:
                    print(f"{current_player.name} won the game!")
                    return
                else:
                    if self.ladders.Check(next_position):
                        self.player_positions[current_player.name] = self.ladders.Jump(next_position)
                        print(f"[+] {current_player.name} got ladder from {next_position} to {self.player_positions[current_player.name]}")
                        print(f"{current_player.name} moved to {self.player_positions[current_player.name]}")
                    elif self.snakes.Check(next_position):
                        self.player_positions[current_player.name] = self.snakes.Jump(next_position)
                        print(f"[-] {current_player.name} bitten by snake from {next_position} to {self.player_positions[current_player.name]}")
                        print(f"{current_player.name} moved to {self.player_positions[current_player.name]}")
                    else:
                        self.player_positions[current_player.name] = next_position
                        print(f"{current_player.name} moved to {next_position}")
                    self.truns.put(current_player)                

                
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
