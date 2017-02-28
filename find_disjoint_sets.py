
def find_disjoint(set_list):

    """
    function to find disjoint SET's given a list of SET's
    :rtype: int, list
    :param set_list: list of SET's

    """
    max_disjoint = []
    for x in combine(set_list):
        if len(x) > len(max_disjoint):
            max_disjoint = x
    return len(max_disjoint),max_disjoint


def combine(set_of_cards, current=None, list_of_sets=set()):

    """
    function to find disjoint SET's by recursively combining them
    :rtype: object
    :param set_of_cards: list of SET's
    :param current: list of current disjoint SET's
    :param list_of_sets: list of disjoint SET's

    """
    if current is None:
        current = []
    if current:
        yield current
    for index, elem in enumerate(set_of_cards):
        if list_of_sets.isdisjoint(elem):
            for element in combine(set_of_cards[index + 1:], current + [elem], list_of_sets | set(elem)):
                yield element
