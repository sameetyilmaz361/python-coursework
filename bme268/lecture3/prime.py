def isPrime(n):
    if n < 2:
        return False
    for i in range(2, (n // 2) + 1):
        if n % i == 0:
            return False
    return True


print("Prime numbers between 1 and 100:")
for n in range(1, 101):
    if isPrime(n):
        print(n, end=" ")