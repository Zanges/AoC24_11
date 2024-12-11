def load(filepath: str) -> str:
    with open(filepath, "r") as fileobj:
        return fileobj.read()


def split_in_middle(element: int) -> tuple[int, int]:
    element = str(element)
    middle = len(element) // 2
    return int(element[:middle]), int(element[middle:])


def blink(data: str) -> str:
    unique_numbers = set([int(number) for number in data.split(" ")])
    new_data = []
    for element in unique_numbers:
        count_of_element = data.count(str(element))
        if element == 0:
            for _ in range(count_of_element):
                new_data.append(str(1))
            continue
        str_element = str(element)
        if len(str_element) % 2 == 0:
            left, right = split_in_middle(element)
            for _ in range(count_of_element):
                new_data.append(str(left))
                new_data.append(str(right))
            continue
        for _ in range(count_of_element):
            new_data.append(str(element * 2024))
    return " ".join(new_data)


def get_result(data: str, n: int) -> str:
    previous_iterations = {}
    for i in range(n):
        print(f"Calculating iteration {i + 1}")
        for previous_data, new_data in previous_iterations.items():
            if previous_data == data:
                print(f"Found a loop")
                return new_data
            if previous_data in data:
                print(f"Found a part of the loop")
                pre_calculation = blink(data[:data.index(previous_data)])
                post_calculation = blink(data[data.index(previous_data) + len(previous_data):])
                return pre_calculation + new_data + post_calculation
        new_data = blink(data)
        previous_iterations[data] = new_data
        data = new_data
    return data


def main():
    data = load("input.txt")
    final_data = get_result(data, 75)
    print(f"Length of the final arrangement: {len(final_data)}")


if __name__ == "__main__":
    main()