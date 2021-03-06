# Project Euler
# Problem 1: Multiples of 3 and 5


def p1_sol():
    """
    Sol to p1
    """
    vals = []
    for i in range(1000):
        if i % 3 == 0 or i % 5 == 0:
            vals.append(i)
    sum1 = 0
    for j in vals:
        sum1 += j
    return vals, sum1


if __name__ == '__main__':
    print(p1_sol())
