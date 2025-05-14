def is_valid_binary(num: str) -> bool:
    """Check if the input string is a valid binary number."""
    return set(num).issubset({'0', '1'})


def binary_to_decimal(binary_str: str) -> int:
    """Convert binary string to its decimal equivalent with step-by-step output."""
    decimal_value = 0
    power = len(binary_str) - 1

    print("\nStep-by-step conversion:")
    for i, digit in enumerate(binary_str):
        value = int(digit) * (2 ** power)
        print(f"{digit} × 2^{power} = {value}", end="")

        if i < len(binary_str) - 1:
            print(" + ", end="")
        else:
            print()

        decimal_value += value
        power -= 1

    return decimal_value


def main():
    while True:
        binary_input = input("Enter a Binary Number: ").strip()

        while not is_valid_binary(binary_input):
            binary_input = input("Invalid input. Please enter a valid Binary Number: ").strip()

        result = binary_to_decimal(binary_input)
        print(f"\nBinary to Decimal Conversion: {result}\n")


if __name__ == "__main__":
    main()
