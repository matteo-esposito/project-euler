# Project Euler
# Problem 4: Largest Palindrome Product


def p4_sol():
    '''
    Sol to p4
    '''
    final = None
    for i in range(100, 1000):
        for j in range(100, 1000):
            val = i*j
            if str(val) == str(val)[::-1]:
                if final is None or val > final:
                    final = val
    return final

if __name__ == '__main__':
    print(p4_sol())
