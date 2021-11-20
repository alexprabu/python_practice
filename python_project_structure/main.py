from prime.prime import Prime
import prime.constants as c


def run():
    print("Started running...")
    p = Prime(c.START, c.END)
    primes = p.calculate_primes()
    print(primes)


if __name__ == '__main__':
    run()
