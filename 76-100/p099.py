# Project Euler
# Problem 99: Largest exponential
import pe_functions as pe
import math

def sol():
    # Read csv
    values = []
    with open("_data/p099_base_exp.txt", "r") as f:
        for line in f:
            values.append([int(i) for i in line.rstrip('\n').split(",")])
        new_vals = [i[0] for i in values]

    max_vals = []
    max_val = 0
    base = 0
    result = 0
    exponent = 0    
    for i in range(0, len(new_vals), 2):
        base = new_vals[i]
        exponent = new_vals[i+1]
        result = exponent*math.log(base)
        if result > max_val:
            max_val = result
            max_vals = [base, exponent]
    return max_vals

if __name__ == '__main__':
    pe.runSolution(sol)
