def generate_single_pythagorean_triplet(m: int):
    """Generates a single Pythagorean triplet using the formula (2m, m² - 1, m² + 1)."""
    width = 50
    print("\n" + "*" * width)
    print("Pythagorean Triplets".center(width))
    print("*" * width)
    print("Formula → (2m, m² - 1, m² + 1)\n")

    a = 2 * m
    b = m ** 2 - 1
    c = m ** 2 + 1
    triplet = sorted([a, b, c])

    print(f"→ {triplet[0]}² + {triplet[1]}² = {triplet[2]}²")
    print(f"→ {triplet[0]**2} + {triplet[1]**2} = {triplet[2]**2}")
    print(f"::: Hence, Pythagorean Triplet → ({triplet[0]}, {triplet[1]}, {triplet[2]})")
    print("*" * width)


def main():
    while True:
        try:
            m = int(input("Enter a number (m > 1): "))
            if m > 1:
                generate_single_pythagorean_triplet(m)
                break
            else:
                print("Please enter a number greater than 1.")
        except ValueError:
            print("Invalid input. Please enter a valid integer.")


if __name__ == "__main__":
    main()
