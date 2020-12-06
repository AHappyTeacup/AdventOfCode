"""https://adventofcode.com/2020/day/5"""
import aoc_interface


YEAR = 2020
DAY = 5

NUM_ROWS = 128
NUM_COLS = 8
LOWER_HALF_ROW = "F"
UPPER_HALF_ROW = "B"
LOWER_HALF_COL = "L"
UPPER_HALF_COL = "R"


def get_seat_row_col(boarding_pass):
    row_range = list(range(NUM_ROWS))
    col_range = list(range(NUM_COLS))
    max_row = NUM_ROWS
    min_row = 0
    max_col = NUM_COLS
    min_col = 0
    row_diff = NUM_ROWS // 2
    col_diff = NUM_COLS // 2
    for char in boarding_pass:
        if char in [LOWER_HALF_ROW, UPPER_HALF_ROW]:
            if char == LOWER_HALF_ROW:
                max_row -= row_diff
            if char == UPPER_HALF_ROW:
                min_row += row_diff
            row_diff = row_diff // 2
        if char in [LOWER_HALF_COL, UPPER_HALF_COL]:
            if char == LOWER_HALF_COL:
                max_col -= col_diff
            if char == UPPER_HALF_COL:
                min_col += col_diff
            col_diff = col_diff // 2
    return row_range[min_row], col_range[min_col]


def get_seat_id(row, col):
    seat_id = (row * 8) + col
    return seat_id


def part_one(boarding_passes):
    max_seat_id = 0
    for boarding_pass in boarding_passes:
        row, col = get_seat_row_col(boarding_pass)
        seat_id = get_seat_id(row, col)
        if seat_id > max_seat_id:
            max_seat_id = seat_id
    return max_seat_id


def part_two(boarding_passes):
    occupied_seats = list()
    for _ in range(NUM_ROWS):
        occupied_seats_in_row = list()
        for _ in range(NUM_COLS):
            occupied_seats_in_row.append(False)
        occupied_seats.append(occupied_seats_in_row)
    occupied_seat_ids = list()

    for boarding_pass in boarding_passes:
        row, col = get_seat_row_col(boarding_pass)
        occupied_seats[row][col] = True
        occupied_seat_ids.append(get_seat_id(row, col))

    for row in range(NUM_ROWS):
        for col in range(NUM_COLS):
            if not occupied_seats[row][col]:
                seat_id = get_seat_id(row, col)
                if seat_id+1 in occupied_seat_ids and seat_id-1 in occupied_seat_ids:
                    return seat_id


def main(boarding_passes):
    part_one_answer = part_one(boarding_passes)
    part_two_answer = part_two(boarding_passes)

    return part_one_answer, part_two_answer
    

if __name__ == "__main__":
    input_text = aoc_interface.get_input(YEAR, DAY)
    input_list = [x for x in input_text.split("\n")]
    answer_one, answer_two = main(input_list)

    print(answer_one, end="...")
    answer_one_correct = aoc_interface.post_answer(YEAR, DAY, 1, answer_one)
    print(answer_one_correct)

    print(answer_two, end="...")
    answer_two_correct = aoc_interface.post_answer(YEAR, DAY, 2, answer_two)
    print(answer_two_correct)
