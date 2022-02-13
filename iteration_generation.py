class multifilter:

    def judge_half(pos, neg): 
        if pos >= neg:
            return True
        else:
            return False

    def judge_any(pos, neg):
        if pos >= 1:
            return True
        else:
            return False

    def judge_all(pos, neg):
        if neg == 0:
            return True
        else:
            return False

    def __init__(self, iterable, *funcs, judge = judge_any):
        self.iterable = iterable
        self.funcs = funcs
        self.judge = judge
        self.index = 0

    def __iter__(self):
        while self.index < len(self.iterable):
            pos = 0
            neg = 0
            for i in self.funcs:
                if i(self.iterable[self.index]) == True:
                    pos += 1
                else:
                    neg += 1
            if self.judge(pos, neg) == True:
                yield self.iterable[self.index]
            self.index += 1

def mul2(x):
    return x % 2 == 0

def mul3(x):
    return x % 3 == 0

def mul5(x):
    return x % 5 == 0

a = [i for i in range(31)]

print(list(multifilter(a, mul2, mul3, mul5, judge=multifilter.judge_all)))