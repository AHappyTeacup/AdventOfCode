"""https://adventofcode.com/2020/day/9"""
import aoc_interface
import itertools


def find_xmas_break(int_list, preamble=25, prev_len=25):
    for int_index in range(preamble, len(int_list)):
        my_int = int_list[int_index]
        sum_range = int_list[int_index-prev_len:int_index]
        for a, b in itertools.combinations(sum_range, 2):
            if a + b == my_int:
                break
        else:
            return my_int


def part_one(int_list):
    invalid_num = find_xmas_break(int_list, preamble=25, prev_len=25)
    return invalid_num


def part_two(int_list):
    invalid_num = find_xmas_break(int_list, preamble=25, prev_len=25)
    int_queue = list()
    for i in int_list:
        int_queue.append(i)
        while sum(int_queue) > invalid_num:
            int_queue.pop(0)
        if sum(int_queue) == invalid_num and len(int_queue) >= 2:
            encryption_weakness = min(int_queue) + max(int_queue)
            return encryption_weakness


def main(int_list):
    part_one_answer = part_one(int_list)
    part_two_answer = part_two(int_list)

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
