class Buffer:

    def __init__(self):
        self.lst = []

    def add(self, *a):
        x = list(a)
        self.lst += x
        while len(self.lst) >= 5:
            if len(self.lst) >= 5:
                summ = sum(self.lst[:5])
                print(summ)
                del self.lst[:5]

    def get_current_part(self):
        return self.lst


buf = Buffer()
buf.add(1, 2, 3)
buf.get_current_part()
buf.add(4, 5, 6)
buf.get_current_part()
buf.add(7, 8, 9, 10)
buf.get_current_part()
buf.add(1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1)
buf.get_current_part()
