def is_prime(n):
    for i in range(2, int(n ** 1/2) + 1):
        if n % i == 0:
            return False
    return True


def is_odd(n):
    if n % 2 == 0:
        return False
    return True
