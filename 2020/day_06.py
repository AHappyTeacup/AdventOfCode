"""https://adventofcode.com/2020/day/6"""
import aoc_interface


def part_one(question_answers):
    total_questions_answers = 0
    group_answers = set()
    for answer in question_answers:
        if answer.strip() == '':
            total_questions_answers += len(group_answers)
            group_answers = set()
            continue
        for char in answer:
            group_answers.add(char)
    return total_questions_answers


def part_two(question_answers):
    total_questions_answers = 0
    group_answers = list()
    for answer in question_answers:
        if answer.strip() == '':
            total_questions_answers += len(set.intersection(*group_answers))
            group_answers = list()
            continue
        individual_answers = set()
        for char in answer:
            individual_answers.add(char)
        group_answers.append(individual_answers)
    return total_questions_answers


def main(question_answers):
    part_one_answer = part_one(question_answers)
    part_two_answer = part_two(question_answers)

    return part_one_answer, part_two_answer


if __name__ == "__main__":
    input_text = aoc_interface.get_input()
    input_list = [x for x in input_text.split("\n")]
    answer_one, answer_two = main(input_list)

    print(answer_one, end="...")
    answer_one_correct = aoc_interface.post_answer(1, answer_one)
    print(answer_one_correct)

    print(answer_two, end="...")
    answer_two_correct = aoc_interface.post_answer(2, answer_two)
    print(answer_two_correct)
