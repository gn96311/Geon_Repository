import sys

n = int(sys.stdin.readline())

def fibonacci(first, second):
    number = first + second
    return number

if n == 0:
    print(0)
elif n == 1:
    print(1)
else:
    first_number = 0
    second_number = 1
    for i in range(n-1):
        next_number = fibonacci(first_number, second_number)
        first_number = second_number
        second_number = next_number
    print(next_number)
"""
num = int(input())

def fibonach(a, b, count):
    if(num == 0):
        print(a)
    elif(num == 1):
        print(b)
    else:  
        c = a + b

        if(count == num):
            return print(c)

        return fibonach(b, c, count + 1)
fibonach(0, 1, 2)
"""