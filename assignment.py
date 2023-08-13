def fibonacci_series(limit):
    a, b = 0, 1
    while a <= limit:
        print(a, end=' ')
        a, b = b, a + b

# Set the limit to 50
limit = 50

print("Fibonacci series between 0 and 50:")
fibonacci_series(limit)