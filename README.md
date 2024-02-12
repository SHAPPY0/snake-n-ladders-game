# snake-n-ladders-game

### Load The Game:
```python
    board_size = 100
    dice_num = 1
    game = SnakeLadder(board_size, dice_num)

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
    game.AddPlayer("Abc")
    game.AddPlayer("Xyz")
    
```

### Start The Game:

```python
    game.Start()

    #Roll The Dice:
    In CLI it will show player name based on the turns, press 'r' key and press Enter.
```