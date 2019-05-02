# Project Euler
# Problem 42: Coded triangle numbers
import pe_functions as pe
import math

def sol():
    '''
    Solution to project euler problem.
    '''
    # Read text file
    with open("data/p042_words.txt", "r") as f:
        line = f.read()
        names = line.replace('"', '').split(',')
    
    tri_numbers = []
    for i in range(0, 50):
        tri_numbers.append((1/2)*i*(i+1))

    word_values = []
    for i, name in enumerate(names, 1):
        tval = 0
        for char in list(name):
            tval += ord(char)-64
        word_values.append(tval)

    final_vec = [v for v in word_values if v in tri_numbers]

    return len(final_vec)

if __name__ == '__main__':
    pe.runSolution(sol)