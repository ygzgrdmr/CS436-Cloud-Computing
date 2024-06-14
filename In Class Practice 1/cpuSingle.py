import argparse


def is_prime(num):
    if num <= 1:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True


def find_primes(lower, higher):
    primes = []
    for num in range(lower, higher + 1):
        if is_prime(num):
            print(f"Found a prime {num}")
            primes.append(num)
    return primes


def main():
    parser = argparse.ArgumentParser(
        description="Find prime numbers in a given range")
    parser.add_argument("lower", type=int, help="Lower number of the range")
    parser.add_argument("higher", type=int, help="Higher number of the range")
    args = parser.parse_args()

    lower = args.lower
    higher = args.higher

    primes = find_primes(lower, higher)
    print(f"Prime numbers in the range [{lower}, {higher}]: {primes}")


if __name__ == "__main__":
    main()
