class Banque:
    def __init__(self):
        pass


def decomposer(n):
    pieces_10 = n // 10
    n %= 10

    pieces_5 = n // 5
    n %= 5

    pieces_1 = n

    return pieces_10, pieces_5, pieces_1


print(decomposer(124))
n = 124
n %= 10
print(n)
