class NonPositiveError(Exception):
    pass


class PositiveList(list):

    def append(self, elem):
        if elem > 0:
            super().append(elem)
        else:
            raise NonPositiveError

