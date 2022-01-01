class Buffer:
    def __init__(self):
            self.list = []
    def add (self, *a):
        self.list += (a)
        if len(self.list) >= 5:
            while len(self.list) >= 5:
                sum = 0
                for i in range(5):
                    sum += self.list[i]
                print(sum)
                Buffer.get_current_part(self)
    def get_current_part(self):
        if len(self.list) >= 5:
            for i in range(5):
                self.list.pop(0)
        return self.list