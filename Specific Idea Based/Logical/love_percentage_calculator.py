def get_letter_frequencies(name_combination: str) -> list[int]:
    """Count the frequency of each unique character and return as a list."""
    counts = []
    characters = list(name_combination)

    while characters:
        ch = characters[0]
        count = characters.count(ch)
        counts.append(count)
        characters = list(filter(lambda c: c != ch, characters))

    return counts


def reduce_to_percentage(counts: list[int]) -> int:
    """Reduce a list of integers to a two-digit love percentage."""
    while len(counts) > 2:
        new_counts = []
        while len(counts) > 1:
            new_counts.append(counts[0] + counts[-1])
            counts = counts[1:-1]
        if counts:
            new_counts.append(counts[0])
        counts = [int(digit) for count in new_counts for digit in str(count)]
    return int("".join(map(str, counts)))


def calculate_love_percentage(name1: str, name2: str) -> int:
    """Calculate love percentage between two names."""
    combined = (name1 + "LOVES" + name2).upper().replace(" ", "")
    frequencies = get_letter_frequencies(combined)
    return reduce_to_percentage(frequencies)


def main():
    name1 = input("Enter Partner 1 Name: ").strip()
    name2 = input("Enter Partner 2 Name: ").strip()

    print()
    score1 = calculate_love_percentage(name1, name2)
    print(f"{name1.upper()} LOVES {name2.upper()}")
    print(f"Your Love Percentage is {score1}%.\n")

    score2 = calculate_love_percentage(name2, name1)
    print(f"{name2.upper()} LOVES {name1.upper()}")
    print(f"Your Love Percentage is {score2}%.\n")

    mutual_score = (score1 + score2) / 2
    print(f"Your Mutual Love Percentage is {mutual_score:.2f}%.")


if __name__ == "__main__":
    main()
