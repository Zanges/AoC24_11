def load(filepath: str) -> list[int]:
    with open(filepath, "r") as fileobj:
        data = fileobj.read()
    return [int(element) for element in data.split(" ")]


def split_in_middle(element: int) -> tuple[int, int]:
    element = str(element)
    middle = len(element) // 2
    return int(element[:middle]), int(element[middle:])


def blink(data: list[int]) -> list[int]:
    new_data = []
    for element in data:
        if element == 0:
            new_data.append(1)
            continue
        str_element = str(element)
        if len(str_element) % 2 == 0:
            left, right = split_in_middle(element)
            new_data.append(left)
            new_data.append(right)
            continue
        new_data.append(element * 2024)
    return new_data


def main():
    data = load("input.txt")
    print(f"Initial arrangement:\n{' '.join([str(element) for element in data])}")
    for i in range(1, 26):
        data = blink(data)
        print(f"After {i} blink(s):\n{' '.join([str(element) for element in data])}")
    print(f"Length of the final arrangement: {len(data)}")


if __name__ == "__main__":
    main()