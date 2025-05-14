def calculate_triplet_from_side(n: float, choice: int):
    """Returns the Pythagorean triplet derived from a given side and choice."""
    if choice == 1:
        m = round(n / 2, 3)
    elif choice == 2:
        m = round((n + 1) ** 0.5, 3)
    elif choice == 3:
        m = round((n - 1) ** 0.5, 3)
    else:
        raise ValueError("Invalid choice")

    a = round(2 * m, 3)
    b = round((m ** 2) - 1, 3)
    c = round((m ** 2) + 1, 3)
    return sorted([a, b, c])


def main():
    width = 50
    print('*' * width)
    print('Find Pythagorean Triplet of'.center(width))
    print('*' * width)
    print("\nFormula → (2m, m² - 1, m² + 1)\n")

    # Input number
    while True:
        try:
            n = float(input("Enter a number (> 1): "))
            if n > 1:
                break
            else:
                print("Please enter a number greater than 1.")
        except ValueError:
            print("Invalid input. Please enter a number.")

    print("\nPlease select which side the number corresponds to:")
    print("\t1. Smallest side (2m)")
    print("\t2. Middle side (m² - 1)")
    print("\t3. Hypotenuse (m² + 1)")

    # Choice input
    while True:
        try:
            choice = int(input("Enter your choice (1-3): "))
            if 1 <= choice <= 3:
                break
            else:
                print("Choice must be between 1 and 3.")
        except ValueError:
            print("Invalid input. Enter an integer between 1 and 3.")

    # Calculate triplet
    triplet = calculate_triplet_from_side(n, choice)

    # Print result
    print(f"\n→ {triplet[0]}² + {triplet[1]}² = {triplet[2]}²")
    print(f"→ {triplet[0]**2} + {triplet[1]**2} = {triplet[2]**2}")
    print(f"::: Hence, Pythagorean Triplet → ({triplet[0]}, {triplet[1]}, {triplet[2]})")
    print('*' * width)


if __name__ == "__main__":
    main()
