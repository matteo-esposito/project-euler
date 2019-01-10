# Project Euler
# Problem 2: Even Fibonacci numbers


def p2_sol():
    '''
    Sol to p2
    '''
    # Generate fibonacci numbers
    fib = [1, 2]
    num = 1
    for i in range(2, 10000):
        if num > 3000000:
            break
        else:
            fib.append(fib[i-1] + fib[i-2])
            num = fib[i]

    # Calculate sum
    sum = 0
    for i in fib:
        if i % 2 == 0:
            sum += i

    return(sum)


if __name__ == '__main__':
    print(p2_sol())
