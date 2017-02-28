import support_methods
from set_of_three import set_of_three


def find_set(set_of_cards):

    """
    function to find SET's in a given set of cards

    :rtype: int, list
    :param set_of_cards: list of card objects
    :return: number of SET's, list of SET's

    """
    generated_set = set()
    set_list = []
    all_pairs = support_methods.generate_all_pairs(set_of_cards)
    for pair in all_pairs:
        x = pair[0]
        y = pair[1]
        z = support_methods.generate_third_card(x, y)
        if support_methods.find(z, set_of_cards):
            set_of_set_cards = set_of_three(x, y, z)
            before_adding = len(generated_set)
            generated_set.add(str(set_of_set_cards))
            after_adding = len(generated_set)
            if before_adding != after_adding:
                each_set = [str(x), str(y), str(z)]
                set_list.append(each_set)

    return len(generated_set), set_list
