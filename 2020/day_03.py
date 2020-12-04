"""https://adventofcode.com/2020/day/3"""
import aoc_interface


YEAR = 2020
DAY = 3


def main(input_map):
    answer_one = part_one(input_map)
    answer_two = part_two(input_map)

    return answer_one, answer_two


def part_one(input_map):
    """Get the tree count of one map traversal.

    :param input_map: A list of lines consisting of '.'s and '#'s.
    :return: int
    """
    tree_count = traverse_map(input_map)
    return tree_count


def part_two(input_map):
    """Travel down the input map at different slopes.
    Get the product of the number of trees encountered on each run.

    :param input_map: A list of lines consisting of '.'s and '#'s.
    :return: int
    """
    tree_product = traverse_map(input_map, right=1, down=1)
    tree_product *= traverse_map(input_map, right=3, down=1)
    tree_product *= traverse_map(input_map, right=5, down=1)
    tree_product *= traverse_map(input_map, right=7, down=1)
    tree_product *= traverse_map(input_map, right=1, down=2)
    return tree_product


def traverse_map(input_map, right=3, down=1):
    """Travel down the input map by heading right and down a fixed amount each
    iteration.
    The map consists of clear ground '.', and trees '#'.
    The map repeats to the right infinitely.
    Get the number of trees that would be encountered travelling from the top
    left at the specified slope.

    :param input_map: A list of lines consisting of '.'s and '#'s.
    :param right: The number of grid spaces to move right each iteration
    :param down: The number of grid spaces to move down each iteration
    :return: int
    """
    tree_count = 0
    x_axis = 0
    for line in input_map[::down]:
        if line[x_axis % len(line)] == "#":
            tree_count += 1
        x_axis += right
    return tree_count


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
