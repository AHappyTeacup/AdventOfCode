"""https://adventofcode.com/2020/day/8"""
import aoc_interface


YEAR = 2020
DAY = 8

ACC = "acc"
JMP = "jmp"
NOP = "nop"


def parse_instructions(raw_input_instructions):
    """"""
    input_instructions = list()
    for instruction in raw_input_instructions:
        cmd, arg = instruction.split(" ")
        mod = arg[0]
        val = int(arg[1:])
        input_instructions.append((cmd, mod, val))
    return input_instructions


def execute_instructions(instructions):
    """"""
    visited_lines = list()
    instruction_index = 0
    accumulator = 0
    while True:
        visited_lines.append(instruction_index)
        if instruction_index == len(instructions):
            break
        cmd, mod, val = instructions[instruction_index]

        if cmd == ACC or cmd == NOP:
            if cmd == ACC:
                if mod == "+":
                    accumulator += val
                elif mod == "-":
                    accumulator -= val
            instruction_index += 1
        elif cmd == JMP:
            if mod == "+":
                instruction_index += val
            elif mod == "-":
                instruction_index -= val
        if instruction_index in visited_lines:
            break

    return visited_lines, accumulator


def part_one(raw_input_instructions):
    """"""
    input_instructions = parse_instructions(raw_input_instructions)
    visited_lines, accumulator = execute_instructions(input_instructions)
    return accumulator


def part_two(raw_input_instructions):
    input_instructions = parse_instructions(raw_input_instructions)
    accumulator = 0
    for index in range(len(input_instructions)):
        cmd, mod, arg = input_instructions[index]
        old_cmd = cmd
        if cmd == JMP:
            cmd = NOP
        elif cmd == NOP:
            cmd = JMP
        else:
            continue
        input_instructions[index] = (cmd, mod, arg)
        visited_lines, accumulator = execute_instructions(input_instructions)
        if len(input_instructions) in visited_lines:
            break
        input_instructions[index] = (old_cmd, mod, arg)
    return accumulator


def main(input_instructions):
    part_one_answer = part_one(input_instructions)
    part_two_answer = part_two(input_instructions)

    return part_one_answer, part_two_answer


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
