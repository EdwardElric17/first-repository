class MoneyBox:
    def __init__(self, capacity):
        self.capacity = capacity
    def can_add(self, v):
        return self.capacity - v >= 0
    def add(self, v):
        if MoneyBox.can_add(self, v) == True:
            self.capacity -= v
            return self.capacity