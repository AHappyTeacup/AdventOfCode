"""https://adventofcode.com/2020/day/1"""
import aoc_interface


def main(expense_report):
    answer_one = part_one(expense_report)
    print(answer_one)
    answer_two = part_two(expense_report)
    print(answer_two)


def part_one(expense_report):
    """Find two entries that sum to 2020, and return their product.

    :param expense_report: A list of integers.
    :return: int
    """
    for idx, entry_1 in enumerate(expense_report):
        for entry_2 in expense_report[idx:]:
            if entry_1 + entry_2 == 2020:
                answer = entry_1 * entry_2
                return answer


def part_two(expense_report):
    """Find the three entries that sum to 2020, and return their product.

    :param expense_report: A list of integers.
    :return: int
    """
    for idx, entry_1 in enumerate(expense_report):
        for idy, entry_2 in enumerate(expense_report[idx:]):
            for entry_3 in expense_report[idy:]:
                if entry_1 + entry_2 + entry_3 == 2020:
                    answer = entry_1 * entry_2 * entry_3
                    return answer


if __name__ == "__main__":
    input_text = aoc_interface.get_input(2020, 1)
    input_list = [int(x) for x in input_text.split("\n") if x != '']
    main(input_list)
