"""
Write an iterative and recursive function,
that implements the factorial of a number.
"""

def fact_iterative(n):
    ans = 1
    for i in range(1, n+1):
        ans *= i
    print( str(n) + "! is " + str(ans))

def fact_recursive(n):
    if n == 1:
        return 1
    else:
        return n * fact_recursive(n-1)

fact_iterative(5)
print(fact_recursive(5))
