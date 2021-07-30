"""
Rekursion

Abbruchbedingung: eine rekursive Funktion muss terminieren,
d.h. mit jedem Rekursionsschritt muss das Problem reduziert werden und in 
Richtung der Abbruchbedingung bewegt werden

"""

# Bsp_ Fakultät
# n! = n * (n-1)!, if n > 1 and f(1) = 1
# 4! = 4 * 3 * 2 * 1

def factorial(n):
    if n == 1:
        return 1
    else:
        tmp = n * factorial(n-1)
        print("intermediate result for ", n, " * factorial(", n-1, "): ", tmp)
        return tmp
        
print(factorial(5))

# Bsp: Fibonacci
# Fn = Fn-1 + Fn-2, wobei F0=0 und F1=1
def fib(n):
    if n==0:
        return 0
    elif n==1:
        return 1
    else:
        return fib(n-1) + fib(n-2)
        
print(fib(10))
