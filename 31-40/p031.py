# Project Euler
# Problem 31: Coin sums
import pe_functions as pe

def sol():
    '''
    Solution to project euler problem.
    '''
    coins = [1, 2, 5, 10, 20, 50, 100, 200]
    combination_list = [1] + [0]*200

    for coin in coins:
        for index, value in enumerate(combination_list):
            if index >= coin:
                combination_list[index] += combination_list[index - coin]
    return combination_list[len(combination_list)-1]

if __name__ == '__main__':
    pe.runSolution(sol)