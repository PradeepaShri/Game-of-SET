from card import Card
import itertools


def generate_third_card(c1, c2):

    """
    function to generate the third card which forms a SET with the given two cards
    :rtype: object
    :param c1: card object1
    :param c2: card object2
    :return: card object3

    """
    color_set, symbol_set, shading_set, frequency_set = generate_sets()
    c3 = Card()
    if c1.color == c2.color:
        c3.color = c1.color
    else:
        c3.color = str((color_set - {c1.color, c2.color}).pop())

    if c1.symbol == c2.symbol:
        c3.symbol = c1.symbol
    else:
        c3.symbol = str((symbol_set - {c1.symbol, c2.symbol}).pop())

    if c1.shading == c2.shading:
        c3.shading = c1.shading
    else:
        c3.shading = str((shading_set - {c1.shading, c2.shading}).pop())

    if c1.no_of_symbols == c2.no_of_symbols:
        c3.no_of_symbols = c1.no_of_symbols
    else:
        c3.no_of_symbols = int((frequency_set - {c1.no_of_symbols, c2.no_of_symbols}).pop())
    return c3


def find(c3, set_of_cards):

    """
    function to check if a card is present in a given list of cards
    :rtype: boolean
    :param c3: card object
    :param set_of_cards: list of cards
    :return: true of false

    """
    for x in set_of_cards:
        if c3 == x:
            return True
    return False


def generate_all_pairs(set_of_cards):

    """
    function to generate all possible pairs of a given list of cards
    :rtype: list
    :param set_of_cards: list of cards
    :return: list of pairs of cards

    """
    pairs_of_cards = []
    for pair in itertools.combinations(set_of_cards, 2):
        pairs_of_cards.append(pair)
    return pairs_of_cards


def generate_sets():

    """
    function to return the attributes and their values
    :rtype: set
    :return: sets of attribute values

    """
    color_set = {'blue', 'green', 'yellow'}
    symbol_set = {'A', 'S', 'H'}
    shading_set = {'upper', 'lower', 'symbol'}
    frequency_set = {1, 2, 3}
    return color_set, symbol_set, shading_set, frequency_set
