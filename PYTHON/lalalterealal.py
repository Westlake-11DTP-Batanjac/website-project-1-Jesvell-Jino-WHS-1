def is_prime(n):
    n = int((n ** 0.5))
    for i in range(1, n + 1):
        print(i)
        if i != 1 and i != (n + 1) and n % i == 0:
            pass
        else:
            return True
    return False

print(is_prime(4))