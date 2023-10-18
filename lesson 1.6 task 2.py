class ExtendedStack(list):
    def sum(self):
        x = self[-1]
        y = self[-2]
        summ = x + y
        self.pop(-1)
        self.pop(-1)
        self.append(summ)

    def sub(self):
        x = self[-1]
        y = self[-2]
        subs = x - y
        self.pop(-1)
        self.pop(-1)
        self.append(subs)

    def mul(self):
        x = self[-1]
        y = self[-2]
        mult = x * y
        self.pop(-1)
        self.pop(-1)
        self.append(mult)

    def div(self):
        x = self[-1]
        y = self[-2]
        result = x // y
        self.pop(-1)
        self.pop(-1)
        self.append(result)

