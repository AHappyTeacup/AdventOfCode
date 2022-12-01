"""https://adventofcode.com/2021/day/2"""
import aoc_interface


FORWARD = "forward"
DOWN = "down"
UP = "up"


def main(input_list):
    answer_one = part_one(input_list)
    answer_two = part_two(input_list)
    return answer_one, answer_two


def part_one(input_list):
    depth = 0
    horizontal_distance = 0
    for line in input_list:
        command, distance = line.split(" ")
        distance = int(distance)
        if command == FORWARD:
            horizontal_distance += distance
        elif command == DOWN:
            depth += distance
        elif command == UP:
            depth -= distance
        else:
            raise Exception
    return depth * horizontal_distance


def part_two(input_list):
    depth = 0
    aim = 0
    horizontal_distance = 0
    for line in input_list:
        command, distance = line.split(" ")
        distance = int(distance)
        if command == FORWARD:
            horizontal_distance += distance
            depth += (distance * aim)
        elif command == DOWN:
            aim += distance
        elif command == UP:
            aim -= distance
        else:
            raise Exception
    return depth * horizontal_distance



if __name__ == "__main__":
    input_text = aoc_interface.get_input()
    input_list = [x for x in input_text.split("\n") if x != '']

    answer_one, answer_two = main(input_list)

    print(answer_one, end="...")
    answer_one_correct = aoc_interface.post_answer(1, answer_one)
    print(answer_one_correct)

    print(answer_two, end="...")
    answer_two_correct = aoc_interface.post_answer(2, answer_two)
    print(answer_two_correct)
