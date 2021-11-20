import prime.constants as c
from prime.helpers import *


class Prime:

    def __init__(self, start, end):
        self.start = start
        self.end = end

    def calculate_primes(self):
        primes = []
        for n in range(self.start, self.end):
            if is_prime(n) and n not in c.SKIP_RANGE:
                primes.append(n)
        return primes
