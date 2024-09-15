from functools import lru_cache
import matplotlib.pyplot as plt

@lru_cache(maxsize=1000)
def fibonacci(n):
    # Check that the input is a positive integer
    if type(n) != int:
        raise TypeError("n must be a positive integer")
    if n < 1:
        raise ValueError("n must be a positive integer")

    # Compute the nth Fibonacci number
    if n == 1:
        return 1
    elif n == 2:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)

n_values = range(1, 11)  # range for n
fibonacci_values = [fibonacci(n) for n in n_values]

plt.plot(n_values, fibonacci_values)
plt.xlabel("n")
plt.ylabel("Fibonacci(n)")
plt.title("Fibonacci Sequence")
plt.show()
