from collections import Counter


def load(filepath: str) -> Counter:
    """
    Load data and store as a Counter for efficient counting of duplicates.
    """
    with open(filepath, "r") as fileobj:
        data = fileobj.read()
    return Counter(int(element) for element in data.split(" "))


def split_in_middle(element: int) -> tuple[int, int]:
    """
    Split an element in the middle and return the two parts.
    """
    element = str(element)
    middle = len(element) // 2
    return int(element[:middle]), int(element[middle:])


def blink(counter: Counter) -> Counter:
    """
    Perform a blink transformation on the data, returning a new Counter.
    """
    new_counter = Counter()
    for element, count in counter.items():
        if element == 0:
            new_counter[1] += count
            continue
        str_element = str(element)
        if len(str_element) % 2 == 0:
            left, right = split_in_middle(element)
            new_counter[left] += count
            new_counter[right] += count
        else:
            new_counter[element * 2024] += count
    return new_counter


def main():
    data_counter = load("input.txt")
    print("Initial arrangement:")
    print(" ".join([f"{element} (x{count})" for element, count in data_counter.items()]))

    for i in range(1, 76):
        data_counter = blink(data_counter)
        print(f"{i} blink(s)")
    total_length = sum(data_counter.values())
    print(f"Length of the final arrangement: {total_length}")


if __name__ == "__main__":
    main()
