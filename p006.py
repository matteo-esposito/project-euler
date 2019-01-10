# Project Euler
# Problem 6:  Sum square difference


def p6_sol():
    '''
    Sol to p6
    '''
    sum_of_squares = 0
    square_of_sum = 0
    ss = 0
    for i in range(0, 101):
        sum_of_squares += i**2
        ss += i
    square_of_sum = ss ** 2
    return abs(sum_of_squares-square_of_sum)

if __name__ == '__main__':
    print(p6_sol())
