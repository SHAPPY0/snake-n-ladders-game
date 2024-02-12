class Turns:
    def __init__(self):
        self.queue = []

    def put(self, player):
        self.queue.insert(0, player)
    
    def pop(self):
        return self.queue.pop()
    
    def Size(self):
        return len(self.queue)