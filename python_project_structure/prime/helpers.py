def is_prime(num):
    if num <= 1:
        return False
    else:
        for n in range(2, num):
            if num % n != 0:
                continue
            else:
                return False

        return True
