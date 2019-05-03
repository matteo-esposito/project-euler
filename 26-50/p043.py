# Project Euler
# Problem 43: Substring divisibility
import pe_functions as pe
import itertools

def sol():
    '''
    Solution to project euler problem.
    '''
    digits = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    pandigitals = list(itertools.permutations(digits))
    int_pandigitals = []

    for n in pandigitals:
        int_pandigitals.append(int(''.join(n)))
    
    p43_set = []
    for i in int_pandigitals:
        if int(str(i)[1:4]) % 2 == 0 and int(str(i)[2:5]) % 3 == 0 and int(str(i)[3:6]) % 5 == 0 and int(str(i)[4:7]) % 7 == 0 and int(str(i)[5:8]) % 11 == 0 and int(str(i)[6:9]) % 13 == 0 and int(str(i)[7:10]) % 17 == 0:
           p43_set.append(i)

    return sum(p43_set)


if __name__ == '__main__':
    pe.runSolution(sol)