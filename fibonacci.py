# Write your code here :-)
def fibonacci_next(series = [1,1]):
    series.append(series[-1] + series[-2])
    return series

fib1 = fibonacci_next()
print(fib1)
fib1=fibonacci_next(fib1)
print (fib1)
fib2=fibonacci_next()
print (fib2)

#alternative
print("alternative...")
def fibonacci_next2(series = None):
    if series is None:
        series=[1,1]
    series.append(series[-1] + series[-2])
    return series

fib1 = fibonacci_next2()
print(fib1)
fib1=fibonacci_next2(fib1)
print (fib1)
fib2=fibonacci_next2()
print (fib2)

