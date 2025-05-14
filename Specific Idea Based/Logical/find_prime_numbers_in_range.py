def is_prime(n: int) -> bool:
    """Check if a number is prime."""
    if n <= 1:
        return False
    for i in range(2, int(n / 2) + 1):
        if n % i == 0:
            return False
    return True


def main():
    width = 40
    print("~" * width)
    print("Finding Prime Numbers".center(width))
    print("~" * width)
    print()

    # Input
    start = int(input("Enter the first number: "))
    end = int(input("Enter the second number: "))
    print("*" * width)

    # Ensure proper range ordering
    if end < start:
        start, end = end, start

    # Find primes
    primes = [num for num in range(start, end + 1) if is_prime(num)]

    # Output
    if not primes:
        print("There are no prime numbers in the given range!")
    else:
        word = "is" if len(primes) == 1 else "are"
        print(f"Prime number(s) between {start} & {end} {word}: ", end="")
        print(", ".join(map(str, primes)) + ".")


if __name__ == "__main__":
    main()
