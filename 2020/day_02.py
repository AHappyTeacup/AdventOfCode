"""https://adventofcode.com/2020/day/2"""
import aoc_interface


def main(raw_password_list):
    password_list = parse_input(raw_password_list)
    answer_one = part_one(password_list)
    print(answer_one)
    answer_two = part_two(password_list)
    print(answer_two)


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
    input_text = aoc_interface.get_input(2020, 2)
    input_list = [x for x in input_text.split("\n") if x != '']
    main(input_list)
