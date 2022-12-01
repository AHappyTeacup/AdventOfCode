"""https://adventofcode.com/2020/day/11"""
import aoc_interface


TILE_FLOOR = "."
TILE_CHAIR_EMPTY = "L"
TILE_CHAIR_OCCUPIED = "#"


class _Tile:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self._is_occupied = False
        self.neighbours = set()
        self._recently_changed = False
        self._planning_change = False

    def __repr__(self):
        return "Tile(%s, %s), %s" % (self.x, self.y, str(self))

    @property
    def recently_changed(self):
        r_val = self._recently_changed
        self._recently_changed = False
        return r_val

    @property
    def is_occupied(self):
        return self._is_occupied

    @is_occupied.setter
    def is_occupied(self, val: bool):
        self._is_occupied = val
        self._recently_changed = True

    def add_neighbour(self, neighbour):
        self.neighbours.add(neighbour)
        neighbour.neighbours.add(self)

    def plan_change(self):
        occupied_neighbours = sum([x.is_occupied for x in self.neighbours])
        if self.is_occupied:
            if occupied_neighbours >= 4:
                self._planning_change = True
        else:
            if occupied_neighbours == 0:
                self._planning_change = True

    def change(self):
        if self._planning_change:
            self.is_occupied = not self.is_occupied
            self._planning_change = False


class Floor(_Tile):
    is_occupied = False
    recently_changed = False
    plan_change = lambda x: None

    def __str__(self):
        return TILE_FLOOR


class Seat(_Tile):
    def __init__(self, is_occupied, x, y):
        super(Seat, self).__init__(x, y)
        self._is_occupied = is_occupied

    def __str__(self):
        if self._is_occupied:
            return TILE_CHAIR_OCCUPIED
        else:
            return TILE_CHAIR_EMPTY


def tile(char, x, y):
    if char == TILE_FLOOR:
        return Floor(x, y)
    elif char == TILE_CHAIR_EMPTY:
        return Seat(False, x, y)
    elif char == TILE_CHAIR_OCCUPIED:
        return Seat(True, x, y)
    raise Exception("Bad character in input.")


class FloorPlan:
    def __init__(self):
        self.current_row = None
        self.current_x = 0
        self.current_y = -1
        self.rows = []
        self.all_tiles = []

    def add_row(self):
        self.current_row = []
        self.current_x = 0
        self.current_y += 1
        self.rows.append(self.current_row)

    def add_tile(self, new_tile_char: str):
        new_tile = tile(new_tile_char, self.current_x, self.current_y)
        self.current_row.append(new_tile)
        for y in range(self.current_y-1, self.current_y+2):
            y = abs(y)
            if y < len(self.rows):
                for x in range(self.current_x-1, self.current_x+2):
                    x = abs(x)
                    if x < len(self.rows[y]):
                        if x != self.current_x or y != self.current_y:
                            neighbour = self.rows[y][x]
                            new_tile.add_neighbour(neighbour)
        self.all_tiles.append(new_tile)
        self.current_x += 1

    def plan_changes(self):
        for _tile in self.all_tiles:
            _tile.plan_change()

    def change(self):
        for _tile in self.all_tiles:
            _tile.change()

    def get_tile(self, x, y):
        return self.rows[y][x]

    @property
    def recently_changed(self):
        return any([_tile.recently_changed for _tile in self.all_tiles])

    @property
    def occupied_seats(self):
        return sum(_tile.is_occupied for _tile in self.all_tiles)

    def __str__(self):
        return "\n".join(["".join([str(_tile) for _tile in row]) for row in self.rows])


def get_floorplan(input_list):
    floorplan = FloorPlan()
    for input_line in input_list:
        floorplan.add_row()
        for input_char in input_line:
            floorplan.add_tile(input_char)
    return floorplan


def get_seat_count(seat_list):
    floorplan = get_floorplan(seat_list)
    floorplan.plan_changes()
    floorplan.change()
    count = 0
    while floorplan.recently_changed:
        count += 1
        floorplan.plan_changes()
        floorplan.change()
        print("iter %s..." % count)
    print("Total occupied seats: %s" % floorplan.occupied_seats)
    return floorplan.occupied_seats


def part_one(seat_list):
    return get_seat_count(seat_list)


def part_two(seat_list):
    floorplan = get_floorplan(seat_list)


def main(seat_list):
    part_one_answer = part_one(seat_list)
    part_two_answer = part_two(seat_list)

    return part_one_answer, part_two_answer


if __name__ == "__main__":
    # test_main()
    input_text = aoc_interface.get_input()
    input_list = [x for x in input_text.split("\n") if x != '']
    answer_one, answer_two = main(input_list)

    print(answer_one, end="...")
    answer_one_correct = aoc_interface.post_answer(1, answer_one)
    print(answer_one_correct)
    #
    # print(answer_two, end="...")
    # answer_two_correct = aoc_interface.post_answer(2, answer_two)
    # print(answer_two_correct)
