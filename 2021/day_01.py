"""https://adventofcode.com/2021/day/2"""
import aoc_interface


def main(depth_list):
    part_one_answer = depth_increment_counter(depth_list, 1)

    part_two_answer = depth_increment_counter(depth_list, 3)

    return part_one_answer, part_two_answer

def depth_increment_counter(depth_list, windowsize):
    """For a sliding window of length windowsize through the list depthlist,
    count how many times the sum of the window increments.

    :param depth_list: A list of positive integers integers.
    :param windowsize: A non-zero positive integer. The length of the window.
    :return: An integer.
    """
    increment_count = 0
    last_depth_window = depth_list[0:windowsize]
    for current_depth_reading in depth_list[windowsize:]:
        last_depth_reading = sum(last_depth_window)
        last_depth_window.pop(0)
        current_depth_window = last_depth_window + [current_depth_reading]
        if sum(current_depth_window) > last_depth_reading:
            increment_count += 1
        last_depth_window = current_depth_window
    return increment_count

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
