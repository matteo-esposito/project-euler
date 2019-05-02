# Project Euler
# Problem 19: Counting Sundays
import pe_functions as pe
import datetime # Sort of cheating here...

def sol():
    '''
    Solution to project euler problem.
    '''
    num_sundays = 0 
    for year in range(1901, 2001):
        for month in range(1, 13):
            date = datetime.date(year, month, 1)
            if date.weekday() == 6:
                num_sundays += 1
    return num_sundays

if __name__ == '__main__':
    pe.runSolution(sol)