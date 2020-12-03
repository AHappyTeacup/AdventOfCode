"""https://adventofcode.com/2020/day/3"""
import aoc_interface


def main(input_map):
    answer_one = part_one(input_map)
    print(answer_one)
    answer_two = part_two(input_map)
    print(answer_two)


def part_one(input_map, right=3, down=1):
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


def part_two(input_map):
    """Travel down the input map at different slopes.
    Get the product of the number of trees encountered on each run.

    :param input_map: A list of lines consisting of '.'s and '#'s.
    :return: int
    """
    tree_product = part_one(input_map, right=1, down=1)
    tree_product *= part_one(input_map, right=3, down=1)
    tree_product *= part_one(input_map, right=5, down=1)
    tree_product *= part_one(input_map, right=7, down=1)
    tree_product *= part_one(input_map, right=1, down=2)
    return tree_product


if __name__ == "__main__":
    input_text = aoc_interface.get_input(2020, 3)
    input_list = [x for x in input_text.split("\n") if x != '']
    main(input_list)
