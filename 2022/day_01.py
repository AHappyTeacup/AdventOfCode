"""https://adventofcode.com/2022/day/1"""
import aoc_interface



def test():
    test_input_text = """1000
2000
3000

4000

5000
6000

7000
8000
9000

10000"""
    test_input_list = [x for x in test_input_text.split("\n")]
    elves = sort_calories_by_elf(test_input_list)
    print(max(elves))


def sort_calories_by_elf(food_list):
    elves_list = list()
    elven_calories = 0
    for food_item in food_list:
        if food_item == '':
            elves_list.append(elven_calories)
            elven_calories = 0
        else:
            elven_calories += int(food_item)
    return elves_list


def part_one(food_list):
    elves = sort_calories_by_elf(food_list)
    return max(elves)


def part_two(food_list):
    elves = sort_calories_by_elf(food_list)
    elves.sort()
    elves.reverse()
    top_3_elves = elves[:3]
    return sum(top_3_elves)



def main(food_list):
    part_one_answer = part_one(food_list)
    part_two_answer = part_two(food_list)

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
