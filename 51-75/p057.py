# Project Euler
# Problem 57: Square root convergents
import pe_functions as pe
import numpy as np

def sol():
    counter = 0
    nume = 3
    denom = 2
    for i in range(1000):
        nume += 2*denom
        denom = nume - denom
        if pe.num_length(nume) > pe.num_length(denom):
            counter += 1
    return counter

if __name__ == '__main__':
    pe.runSolution(sol)