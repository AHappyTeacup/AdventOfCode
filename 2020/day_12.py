"""https://adventofcode.com/2020/day/12"""
import aoc_interface
import math

NORTH = "N"
SOUTH = "S"
EAST = "E"
WEST = "W"
CARDINAL_DIRECTIONS = [EAST, SOUTH, WEST, NORTH]
LEFT = "L"
RIGHT = "R"
ROTATIONAL_DIRECTIONS = [LEFT, RIGHT]
FORWARD = "F"


class Boat:
    def __init__(self):
        # X, Y co-ordinates
        # Positive Y for North, positive X for East
        self.ship_coords = [0, 0]
        self.direction = 0
        self.directions = {
            0: self.head_east,
            1: self.head_south,
            2: self.head_west,
            3: self.head_north,
        }
        self.travel_coords = self.ship_coords

    def head_north(self, distance):
        self.travel_coords[1] += distance

    def head_east(self, distance):
        self.travel_coords[0] += distance

    def head_south(self, distance):
        self.travel_coords[1] -= distance

    def head_west(self, distance):
        self.travel_coords[0] -= distance

    def move_cardinal_direction(self, direction, distance):
        self.directions[CARDINAL_DIRECTIONS.index(direction)](distance)

    def turn_right(self, degrees):
        if degrees % 90 != 0:
            raise Exception
        turn_increments = degrees // 90
        self.direction = (self.direction + turn_increments) % 4

    def turn_left(self, degrees):
        # Rotate waypoint anticlockwise about ship
        clockwise_degrees = 360 - (degrees % 360)
        self.turn_right(clockwise_degrees)

    def move_forward(self, distance):
        self.directions[self.direction](distance)

    def get_manhattan_distance(self):
        x_distance = int(math.fabs(self.ship_coords[0]))
        y_distance = int(math.fabs(self.ship_coords[1]))
        distance = x_distance + y_distance
        return distance


def apply_instructions_to_boat(boat, input_instructions):
    for line in input_instructions:
        instruction = line[0]
        distance = int(line[1:])
        if instruction in CARDINAL_DIRECTIONS:
            boat.move_cardinal_direction(instruction, distance)
        elif instruction in ROTATIONAL_DIRECTIONS:
            if instruction == LEFT:
                boat.turn_left(distance)
            else:
                boat.turn_right(distance)
        elif instruction == FORWARD:
            boat.move_forward(distance)
        else:
            raise Exception
    return boat


def part_one(input_instructions):
    myboat = Boat()
    apply_instructions_to_boat(myboat, input_instructions)
    return myboat.get_manhattan_distance()


class BoatWithWaypoint(Boat):
    def __init__(self):
        super(BoatWithWaypoint, self).__init__()
        self.waypoint_coords = [10, 1]
        self.travel_coords = self.waypoint_coords

    def turn_right(self, degrees):
        # Rotate waypoint clockwise about ship
        if degrees % 90 != 0:
            raise Exception
        sin_theta = int(math.sin(math.radians(degrees)))
        cos_theta = int(math.cos(math.radians(degrees)))

        wp_vector_x = self.waypoint_coords[0]
        wp_vector_y = self.waypoint_coords[1]

        rotated_wp_vector_x = int(wp_vector_x*cos_theta + wp_vector_y*sin_theta)
        rotated_wp_vector_y = int(- wp_vector_x*sin_theta + wp_vector_y*cos_theta)

        self.waypoint_coords[0] = rotated_wp_vector_x
        self.waypoint_coords[1] = rotated_wp_vector_y

    def move_forward(self, distance):
        delta_x = self.waypoint_coords[0] * distance
        delta_y = self.waypoint_coords[1] * distance

        self.ship_coords[0] += delta_x
        self.ship_coords[1] += delta_y


def part_two(input_instructions):
    myboat = BoatWithWaypoint()
    apply_instructions_to_boat(myboat, input_instructions)
    return myboat.get_manhattan_distance()


def main(joltage_list):
    part_one_answer = part_one(joltage_list)
    part_two_answer = part_two(joltage_list)

    return part_one_answer, part_two_answer


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
