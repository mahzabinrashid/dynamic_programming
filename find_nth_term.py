# A bottom-up solution to find the n-th Fibonacci number
def fib(n):
    # if we see the base cases, directly return the value 1
    if n == 1 or n == 2:
        return 1
    # making an array of length n
    array = [None] * n
    # initializing the values for n = 1 and n = 2
    array[0] = 1
    array[1] = 1
    # filling up the array by using previous stored values
    for i in range(2, n):
        array[i] = array[i - 1] + array[i - 2]
    # returns the last item in the array
    return array[n - 1]
