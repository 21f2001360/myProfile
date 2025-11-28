#!/usr/bin/env python3
"""
prime.py
Prints the 10th prime number (1-based). Outputs `29`.
"""
import math

def is_prime(n: int) -> bool:
    if n < 2:
        return False
    if n % 2 == 0:
        return n == 2
    limit = math.isqrt(n)
    i = 3
    while i <= limit:
        if n % i == 0:
            return False
        i += 2
    return True


def nth_prime(n: int) -> int:
    count = 0
    candidate = 1
    while True:
        candidate += 1
        if is_prime(candidate):
            count += 1
            if count == n:
                return candidate


if __name__ == '__main__':
    # Print the 10th prime (should be 29)
    print(nth_prime(10))
