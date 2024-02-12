class Jumper:
    def __init__(self, start, end):
        self.start = start
        self.end = end

class Ladders(Jumper):
    def __init__(self):
        self.ladders = []

    def Add(self, start, end):
        self.ladders.append(Jumper(start, end))

    def Check(self, next_position):
        for position in self.ladders:
            if position.start == next_position:
                return True
            
        return False
    
    def Jump(self, next_position):
        for position in self.ladders:
            if position.start == next_position:
                return position.end
            
        return next_position
    
    

class Snakes(Jumper):
    def __init__(self):
        self.snakes = []

    def Add(self, start, end):
        self.snakes.append(Jumper(start, end))

    def Check(self, curr_position):
        for position in self.snakes:
            if position.start == curr_position:
                return True
            
        return False
    
    def Jump(self, next_position):
        for position in self.snakes:
            if position.start == next_position:
                return position.end
            
        return next_position
    
