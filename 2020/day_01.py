"""https://adventofcode.com/2020/day/1"""
import aoc_interface
import itertools


YEAR = 2020
DAY = 1

TARGET = 2020


def part_one(expense_report):
    """Find two entries that sum to 2020, and return their product.

    :param expense_report: A list of integers.
    :return: int
    """
    for entry_1, entry_2 in itertools.combinations(expense_report, 2):
        if entry_1 + entry_2 == TARGET:
            answer = entry_1 * entry_2
            return answer


def part_two(expense_report):
    """Find the three entries that sum to 2020, and return their product.

    :param expense_report: A list of integers.
    :return: int
    """
    for entry_1, entry_2, entry_3 in itertools.combinations(expense_report, 3):
        if entry_1 + entry_2 + entry_3 == TARGET:
            answer = entry_1 * entry_2 * entry_3
            return answer


def main(expense_report):
    part_one_answer = part_one(expense_report)
    part_two_answer = part_two(expense_report)

    return part_one_answer, part_two_answer


if __name__ == "__main__":
    input_text = aoc_interface.get_input(YEAR, DAY)
    input_list = [int(x) for x in input_text.split("\n") if x != '']
    answer_one, answer_two = main(input_list)

    print(answer_one, end="...")
    answer_one_correct = aoc_interface.post_answer(YEAR, DAY, 1, answer_one)
    print(answer_one_correct)

    print(answer_two, end="...")
    answer_two_correct = aoc_interface.post_answer(YEAR, DAY, 2, answer_two)
    print(answer_two_correct)
