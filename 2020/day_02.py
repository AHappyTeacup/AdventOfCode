"""https://adventofcode.com/2020/day/2"""
import aoc_interface


YEAR = 2020
DAY = 2


def main(raw_password_list):
    password_list = parse_input(raw_password_list)
    answer_one = part_one(password_list)
    answer_two = part_two(password_list)

    return answer_one, answer_two


def parse_input(raw_password_list):
    """Take lines of input of the form "1-3 a: abcde", and break it out into
    its component pieces. 1, 3, a, abcde

    :param raw_password_list: A list of strings
    :return: A list of tuples
    """
    parsed_input = []
    for line in raw_password_list:
        rule = line.split(":")[0]
        count = rule.split(" ")[0]
        range_start = int(count.split("-")[0])
        range_end = int(count.split("-")[1])
        character = rule.split(" ")[1]

        # This leaves the password with a leading whitespace.
        password = line.split(":")[1]
        parsed_input.append(
            (range_start, range_end, character, password)
        )
    return parsed_input


def part_one(password_list):
    """Count the number of passwords that meet their accompanying criteria.
    In this case, a password must have a specified character occur between a
    minimum and maximum number of times.

    :param password_list: A list of tuples from parse_input
    :return: int
    """
    valid_password_count = 0
    for line in password_list:
        minimum, maximum, character, password = line

        if minimum <= password.count(character) <= maximum:
            valid_password_count += 1

    return valid_password_count


def part_two(password_list):
    """Count the number of passwords that meet their accompanying criteria.
    In this case, a password must have a specified character in one of twp
    positions, but not both.

    :param password_list: A list of tuples from parse_input
    :return: int
    """
    valid_password_count = 0

    for line in password_list:
        first_pos, second_pos, character, password = line
        a = password[first_pos] == character
        b = password[second_pos] == character
        if (a or b) and not(a and b):
            valid_password_count += 1

    return valid_password_count


if __name__ == "__main__":
    input_text = aoc_interface.get_input(YEAR, DAY)
    input_list = [x for x in input_text.split("\n") if x != '']
    answer_one, answer_two = main(input_list)

    print(answer_one, end="...")
    answer_one_correct = aoc_interface.post_answer(YEAR, DAY, 1, answer_one)
    print(answer_one_correct)

    print(answer_two, end="...")
    answer_two_correct = aoc_interface.post_answer(YEAR, DAY, 2, answer_two)
    print(answer_two_correct)
