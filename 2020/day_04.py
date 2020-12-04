"""https://adventofcode.com/2020/day/4"""
import aoc_interface


YEAR = 2020
DAY = 4

BYR = 'byr'
IYR = 'iyr'
EYR = 'eyr'
HGT = 'hgt'
HCL = 'hcl'
ECL = 'ecl'
PID = 'pid'
CID = 'cid'

REQUIRED_PASSPORT_FIELDS = [
    BYR, IYR, EYR, HGT, HCL, ECL, PID,
]
VALID_PASSPORT_FIELDS = REQUIRED_PASSPORT_FIELDS + [CID]


def main(input_passport_list):
    answer_one = part_one(input_passport_list)
    answer_two = part_two(input_passport_list)

    return answer_one, answer_two


def part_one(input_passport_list):
    """Get a count of passports where all the required fields are present,
    and no additional fields are present.

    :param input_passport_list: [str]
    :return: int
    """
    valid_passport_count = 0
    for passport in passport_parser(input_passport_list):
        try:
            for key in REQUIRED_PASSPORT_FIELDS:
                assert(key in passport.keys())
            for key in passport.keys():
                assert(key in VALID_PASSPORT_FIELDS)
            valid_passport_count += 1
        except AssertionError:
            pass
    return valid_passport_count


def part_two(input_passport_list):
    """Get a count of passports where all the required fields are present,
    no additional fields are present, and each field meets strict conditions.

    :param input_passport_list: [str]
    :return: int
    """
    valid_passport_count = 0
    valid_ecl_list = ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']
    for passport in passport_parser(input_passport_list):
        try:
            byr = passport[BYR]
            digit_assertions(byr, min_max=(1920, 2002), val_len=4)

            iyr = passport[IYR]
            digit_assertions(iyr, min_max=(2010, 2020), val_len=4)

            eyr = passport[EYR]
            digit_assertions(eyr, min_max=(2020, 2030), val_len=4)

            hgt = passport[HGT]
            assert('cm' in hgt or 'in' in hgt)
            if 'cm' in hgt:
                digit_assertions(hgt.replace('cm', ''), min_max=(150, 193))
            elif 'in' in hgt:
                digit_assertions(hgt.replace('in', ''), min_max=(59, 76))

            hcl = passport[HCL]
            assert(hcl[0] == '#')
            for char in hcl[1:]:
                assert(char.isdigit() or char in ['a', 'b', 'c', 'd', 'e', 'f'])

            ecl = passport[ECL]
            assert(ecl in valid_ecl_list)

            pid = passport[PID]
            digit_assertions(pid, val_len=9)

            for key in passport.keys():
                assert(key in VALID_PASSPORT_FIELDS)

            valid_passport_count += 1

        except (KeyError, AssertionError):
            pass
    return valid_passport_count


def passport_parser(input_passport_list):
    """Parse the input list for groups of keys.
    The input list separates each group with an empty line.
    Each group consists of space separated "<key>:<val>" pairs.
    Separate these into dictionaries, and yield on an empty line.

    :param input_passport_list: [str]
    :return: dict
    """
    passport = dict()
    for line in input_passport_list:
        if line.strip() == '':
            yield passport
            passport = dict()
        else:
            split_line = line.split(" ")
            for passport_field in split_line:
                key_val = passport_field.split(":")
                passport[key_val[0]] = key_val[1]


def digit_assertions(digit, min_max=None, val_len=None):
    """Apply assertions to strings that are expected to be digits.

    :param digit: A string that may be digits.
    :param min_max: A tuple of minimum and maximum values for 'digits'.
    :param val_len: Assert a strict length for 'digits'.
    :return: None
    """
    assert(digit.isdigit())
    if min_max:
        assert(min_max[0] <= int(digit) <= min_max[1])
    if val_len:
        assert(len(digit) == val_len)


if __name__ == "__main__":
    input_text = aoc_interface.get_input(YEAR, DAY)
    input_list = [x for x in input_text.split("\n")]
    answer_one, answer_two = main(input_list)

    print(answer_one, end="...")
    answer_one_correct = aoc_interface.post_answer(YEAR, DAY, 1, answer_one)
    print(answer_one_correct)

    print(answer_two, end="...")
    answer_two_correct = aoc_interface.post_answer(YEAR, DAY, 2, answer_two)
    print(answer_two_correct)
