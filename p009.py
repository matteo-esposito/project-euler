# Project Euler
# Problem 9:  Special Pythagorean triplet


def isPythagorean(a, b, c):
    return a**2 + b**2 == c**2


def p9_sol(sum):
    '''
    Sol to p9
    '''
    for a in range(sum):
        for b in range(a):
            c = sum - a - b
            if isPythagorean(a, b, c):
                return(a*b*c)

if __name__ == '__main__':
    print(p9_sol(1000))
