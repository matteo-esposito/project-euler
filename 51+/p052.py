# Project Euler
# Problem 52: Permuted multiples
import pe_functions as pe
import itertools

def sol():
    '''
    Solution to project euler problem.
    '''
    for n in range(125875, 150000):
        permutations = list(itertools.permutations(list(str(n))))
        temp_vec = []
        for i in range(1,7):
            temp_vec.append(n*i)
            
        int_permutations = []
        for s in permutations:
            int_permutations.append(int(''.join(s)))

        compare_vec = [i for i in temp_vec if i in int_permutations]
        if len(compare_vec) == 6:
            return n
      
if __name__ == '__main__':
    pe.runSolution(sol)