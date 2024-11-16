def factorial(n):
    if n <= 1:
        return 1
    if n != 1:
        return n*factorial(n-1)

number = int(input("Enter a number for which the factorial is going to be calculated: "))

print(factorial(number))

def fibonachi(n):
    if n == 0 or n == 1:
        return n
    else: 
        return fibonachi(n-1) + fibonachi(n-2)
    
print(fibonachi(number))

def power(x,y):
    if y == 0:
        return 1
    elif y == 1:
        return x  
    else:
        return x*power(x,y-1)
    
print(power(number,3))
