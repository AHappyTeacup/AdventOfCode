"""https://adventofcode.com/2020/day/3"""
import aoc_interface


def main(input_map):
    answer_one = part_one(input_map)
    print(answer_one)
    answer_two = part_two(input_map)
    print(answer_two)


def part_one(input_map, slope=3, decline=1):
    """Travel down the input map by heading right slope, and down decline
    each iteration.
    The map repeats infinitely.
    Get the number of trees - '#' on the map - that would be encountered on
    this journey.

    :param input_map: A list of lines consisting of '.'s and '#'s.
    :param slope:
    :param decline:
    :return: int
    """
    tree_count = 0
    x_axis = 0
    for line in input_map[::decline]:
        if line[x_axis % len(line)] == "#":
            tree_count += 1
        x_axis += slope
    return tree_count


def part_two(input_map):
    """Travel down the input map at different slopes and declines.
    Get the product of the number of trees encountered on each run.

    :param input_map: A list of lines consisting of '.'s and '#'s.
    :return: int
    """
    tree_product = part_one(input_map, slope=1, decline=1)
    tree_product *= part_one(input_map, slope=3, decline=1)
    tree_product *= part_one(input_map, slope=5, decline=1)
    tree_product *= part_one(input_map, slope=7, decline=1)
    tree_product *= part_one(input_map, slope=1, decline=2)
    return tree_product


if __name__ == "__main__":
    input_text = aoc_interface.get_input(2020, 3)
    input_list = [x for x in input_text.split("\n") if x != '']
    main(input_list)
