"""https://adventofcode.com/2020/day/7"""
import aoc_interface


MY_BAG = "shiny gold"


class BagRule:
    """Each type of bag - identified by it's colour - in this problem space can
      a) be contained within certain bags. Parents.
      b) contain a fixed number of other bags (can be none). Children.
    This class allows a sort of doubly-linked linked list approach to bag relations.
    """
    def __init__(self, colour):
        self.colour = colour
        # A list of parent BagRules
        self.parents = list()
        # Children BagRules alongside the required number of each child type.
        self.children = dict()

    def add_parent(self, parent):
        self.parents.append(parent)

    def add_child(self, child, quantity):
        self.children[child] = quantity

    def get_colour(self):
        return self.colour

    def get_parents(self):
        return self.parents

    def get_children(self):
        return self.children


def parse_input(raw_bag_rules):
    """Take a list of text rules for the contents of different types of bags.
    Parse the input and create and link all the necessary BagRule objects.
    Return a dictionary of bag colour strings to BagRule objects.

    :param raw_bag_rules: A list of strings.
    :return: A dictionary of bag colours to BagRule objects.
    """
    bag_rules = dict()

    for single_rule in raw_bag_rules:
        parent_bag_colour = " ".join(single_rule.split(" contain ")[0].split(" ")[:-1])

        # Get BagRule obeject, create and add it if necessary
        if parent_bag_colour not in bag_rules:
            parent_bag = BagRule(parent_bag_colour)
            bag_rules[parent_bag_colour] = parent_bag
        else:
            parent_bag = bag_rules[parent_bag_colour]

        child_bags = single_rule.split(" contain ")[1]
        # Some bags mark the end of the chain and contain no further bags.
        if child_bags != "no other bags.":
            for child_bag_rule in child_bags.split(", "):
                child_bag_quantity = int(child_bag_rule.split(" ")[0])
                child_bag_colour = " ".join(child_bag_rule.split(" ")[1:-1])

                # Get BagRule object, create and add it if necessary
                if child_bag_colour not in bag_rules:
                    child_bag = BagRule(child_bag_colour)
                    bag_rules[child_bag_colour] = child_bag
                else:
                    child_bag = bag_rules[child_bag_colour]

                # Link the BagRule objects
                parent_bag.add_child(child_bag, child_bag_quantity)
                child_bag.add_parent(parent_bag)

    return bag_rules


def part_one(raw_bag_rules):
    """Determine the number of different types of bag that could contain the bag of type MY_BAG."""
    bag_rules = parse_input(raw_bag_rules)
    my_bag = bag_rules[MY_BAG]

    bag_queue = [bag for bag in my_bag.get_parents()]
    bags_eventually_containing_my_bag = set()
    while True:
        this_bag = bag_queue.pop(0)
        bags_eventually_containing_my_bag.add(this_bag.get_colour())
        bag_queue += [bag for bag in this_bag.get_parents()]
        if len(bag_queue) == 0:
            break

    return len(bags_eventually_containing_my_bag)


def count_total_child_bags(bag):
    """Take a BagRule object, and get a count of the number of bags it contains according to it's rules.

    :param bag: BagRule object
    :return: int
    """
    child_bags = bag.get_children()

    child_bag_count = 0
    for bag in child_bags:
        count = child_bags[bag]
        # Add the number of bags, and the number of bags each bag contains.
        child_bag_count += count + (count * count_total_child_bags(bag))
    return child_bag_count


def part_two(raw_bag_rules):
    """Determine the total number of bags that the bag of type MY_BAG would contain."""
    bag_rules = parse_input(raw_bag_rules)
    my_bag = bag_rules[MY_BAG]

    count = count_total_child_bags(my_bag)

    return count


def main(question_input):
    part_one_answer = part_one(question_input)
    part_two_answer = part_two(question_input)

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
