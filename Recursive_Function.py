#Factorial
def factorial(n):
    if n == 1:
        return 1
    else:
        return n * factorial(n-1)

#Fibonacci 
def fib(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fib(n-1) + fib(n-2)

#Fibonacci
memo = {0:0, 1:1}
def fibm(n):
    if not n in memo:
        memo[n] = fibm(n-1) + fibm(n-2)
    return memo[n]

#Multi 5
def mult5(n):
    if n == 1:
        return 5
    else:
        return mult5(n-1) + 5

#Sum of a list
def sum(list):
    if len(list) == 1:
        return list[0]
    else:
        return list[0] + sum(list[1:])

#division
def division(a,b,x=0):
    if a < b:
        return x
    else:
        x += 1
        return division(a-b,b,x) 
    return x

#division 2
def division2(a, b):
    if a < b:
        return 0
    else:
        return 1 + division2(a-b, b)

#Log
def calculate_log(lo, hi, val, base, level=0):
    level += 1
    if level > 100:
        return (lo+hi)/2.0
    mid = (lo + hi)/2.0
    if pow(base, mid) == val:
        return mid
    if pow(base, mid) < val:
        return calculate_log(mid, hi, val, base, level+1)
    return calculate_log(lo, mid, val, base, level+1)

#Log2
def calculate_log2(lo, hi, val, level=0):
    level += 1
    if level > 100:
        return (lo+hi)/2.0
    mid = (lo + hi)/2.0
    if pow(2, mid) == val:
        return mid
    if pow(2, mid) < val:
        return calculate_log2(mid, hi, val, level+1)
    return calculate_log2(lo, mid, val, level+1)

#is Palindrome
def is_palindrome(string) :

    string = "".join(char.lower() for char in string if char.isalpha())

    if len(string) <= 1 :
        return True

    if string[0] == string[-1]:
        return is_palindrome(string[1:-1])

    else :
        return False

#Power
def power(x, y):
    if y == 1:
        return x
    else:
        return x * power(x, y - 1)


