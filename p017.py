# Project Euler
# Problem 17: Number letter counts
import pe_functions as pe
import numpy as np
import math


def sol():
    '''
    Solution to project euler problem.
    '''
    ones = [0, 3, 3, 5, 4, 4, 3, 5, 5, 4, 3, 6, 6, 8, 8, 7, 7, 9, 8, 8]
    tens = [0, 3, 6, 6, 5, 5, 5, 7, 6, 6]
    hundred = 7
    thousand = 8

    charCount = 0
    # Get the digits
    for i in range(1, 1001):
        a = i % 10  # ones
        b = math.floor(((i % 100) - a) / 10)  # tens
        c = math.floor(((i % 1000) - b*10 - a) / 100)  # hundreds

        if c != 0:
            charCount += ones[c] + hundred  # i.e. 3 + hundred
            if b != 0 or a != 0:
                charCount += 3  # and
        if b == 0 or b == 1:
            charCount += ones[b * 10 + a]
        else:
            charCount += ones[a] + tens[b]

    charCount += ones[1] + thousand  # for the thousand case
    return charCount


if __name__ == '__main__':
    pe.runSolution(sol)
