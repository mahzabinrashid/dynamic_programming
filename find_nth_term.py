# A bottom-up solution to find the n-th Fibonacci number
def fib_bottom_up(n):
    # if we see the base cases, directly return the value 1
    if n == 1 or n == 2:
        return 1
    # making an array of length n
    bottom_up = [None] * n
    # initializing the values for n = 1 and n = 2
    bottom_up[0] = 1
    bottom_up[1] = 1
    # filling up the array by using previous stored values
    for i in range(2, n):
        bottom_up[i] = bottom_up[i - 1] + bottom_up[i - 2]
    # returns the last item in the array
    return bottom_up[n - 1]

