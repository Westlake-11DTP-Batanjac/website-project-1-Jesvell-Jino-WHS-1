def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

numbers = list(map(int, input().split()))
count = 0
for n in numbers:
    if is_prime(n) == True:
        count += 1

print(count)