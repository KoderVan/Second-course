class MoneyBox:
    def __init__(self, capacity):
        self.max = capacity
        self.count = 0

    def can_add(self, v):
        if self.count + v <= self.max:
            return True
        if self.count + v > self.max:
            return False

    def add(self, v):
        self.count += v


x = MoneyBox(10)
x.add(5)
x.add(5)
print(x.can_add(1))




