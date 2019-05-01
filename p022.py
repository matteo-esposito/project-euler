# Project Euler
# Problem 22: Names scores
import pe_functions as pe


def sol():
    '''
    Solution to project euler problem.
    '''

    # Read text file
    with open("p022-names.txt", "r") as f:
        line = f.read()
        fields = line.replace('"', '').split(',')
        fields.sort()

    # Calculate total value of names
    val = 0
    for i, name in enumerate(fields, 1):
        val += i*sum([(ord(char)-64) for char in list(name)])

    return val


if __name__ == '__main__':
    pe.runSolution(sol)
