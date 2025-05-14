def parse_input(expression: str) -> list:
    """Splits an input string like '5P2' or 'F5' into recognizable components."""
    temp_str, temp_num, parts = "", "", []
    for char in expression.upper():
        if char.isalpha():
            if temp_num:
                parts.append(temp_num)
                temp_num = ""
            temp_str += char
        elif char.isdigit():
            if temp_str:
                parts.append(temp_str)
                temp_str = ""
            temp_num += char

    if temp_str:
        parts.append(temp_str)
    elif temp_num:
        parts.append(temp_num)

    # Convert numeric parts to int
    return [int(x) if x.isdigit() else x for x in parts]


def factorial(n: int) -> int:
    """Returns factorial of n."""
    if n < 0:
        raise ValueError("Factorial is not defined for negative numbers.")
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result


def permutation(n: int, r: int) -> int:
    if r > n:
        raise ValueError("r cannot be greater than n in permutation.")
    return factorial(n) // factorial(n - r)


def combination(n: int, r: int) -> int:
    if r > n:
        raise ValueError("r cannot be greater than n in combination.")
    return factorial(n) // (factorial(r) * factorial(n - r))


def main():
    width = 60
    print("_" * width)
    print("Permutation, Combination & Factorials".center(width))
    print("¯" * width)
    print("Examples: 5P2 → 20\t5C2 → 10\tF5 → 120")
    print("-" * int(width * 0.85))

    while True:
        try:
            user_input = input("\nEnter the command (e.g., 5P2, 5C2, F5): ").strip()
            parts = parse_input(user_input)

            if not parts:
                raise ValueError("Invalid input format.")

            if parts[0] == "F":
                result = factorial(parts[1])
            elif parts[1] == "P":
                result = permutation(parts[0], parts[2])
            elif parts[1] == "C":
                result = combination(parts[0], parts[2])
            else:
                raise ValueError("Unknown command format.")

            print(f"Output: {result}")
            print("_" * width)

        except Exception as e:
            print(f"Error: {e}")
            print("-" * width)


if __name__ == "__main__":
    main()
