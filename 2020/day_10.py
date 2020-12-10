"""https://adventofcode.com/2020/day/9"""
import aoc_interface


YEAR = 2020
DAY = 10


class JoltageAdaptor:
    def __init__(self, voltage):
        self.voltage = voltage
        self.combinations = None
        self.children = list()

    def add_child(self, child_adaptor):
        self.children.append(child_adaptor)

    def count_combinations(self):
        if not self.combinations:
            if self.children:
                combinations = 0
                for child in self.children:
                    combinations += child.count_combinations()
            else:
                combinations = 1
            self.combinations = combinations
        else:
            combinations = self.combinations
        return combinations


def part_one(joltage_list):
    diff_1 = 0
    diff_2 = 0
    diff_3 = 1
    prev_joltage = 0
    for current_joltage in sorted(joltage_list):
        diff = current_joltage - prev_joltage
        if diff == 1:
            diff_1 += 1
        elif diff == 2:
            diff_2 += 1
        elif diff == 3:
            diff_3 += 1
        else:
            raise Exception
        prev_joltage = current_joltage
    return diff_1 * diff_3


def part_two(joltage_list):
    adaptor_dict = dict()
    joltage_list.append(max(joltage_list) + 3)
    first_adaptor = JoltageAdaptor(0)
    adaptor_dict[0] = first_adaptor

    for current_joltage in sorted(joltage_list):
        if current_joltage not in adaptor_dict:
            adaptor_dict[current_joltage] = JoltageAdaptor(current_joltage)
        else:
            raise Exception
        current_adaptor = adaptor_dict[current_joltage]
        for i in range(1, 4):
            if current_joltage - i in adaptor_dict:
                adaptor_dict[current_joltage-i].add_child(current_adaptor)

    combinations = first_adaptor.count_combinations()
    return combinations


def main(joltage_list):
    part_one_answer = part_one(joltage_list)
    part_two_answer = part_two(joltage_list)

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
