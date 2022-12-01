"""https://adventofcode.com/2020/day/10"""
import aoc_interface


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
    joltage_list.append(0)
    combinations_dict = {max(joltage_list) + 3: 1}

    for current_joltage in sorted(joltage_list, reverse=True):
        if current_joltage not in combinations_dict:
            current_combinations = 0
            for i in range(1, 4):
                if current_joltage+i in combinations_dict:
                    current_combinations += combinations_dict[current_joltage+i]
            combinations_dict[current_joltage] = current_combinations
        else:
            raise Exception
    return combinations_dict[0]


def main(joltage_list):
    part_one_answer = part_one(joltage_list)
    part_two_answer = part_two(joltage_list)

    return part_one_answer, part_two_answer


if __name__ == "__main__":
    input_text = aoc_interface.get_input()
    input_list = [int(x) for x in input_text.split("\n") if x != '']
    answer_one, answer_two = main(input_list)

    print(answer_one, end="...")
    answer_one_correct = aoc_interface.post_answer(1, answer_one)
    print(answer_one_correct)

    print(answer_two, end="...")
    answer_two_correct = aoc_interface.post_answer(2, answer_two)
    print(answer_two_correct)
