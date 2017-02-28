from card import Card


def get_input(file_name):

    """
    Ffunction to read the input file and create a list of cards
    :rtype: list
    :return: list of card objects

    """
    # num_of_cards = sys.stdin.readline()
    set_of_cards = []
    with open(file_name, "r") as txt:
        for line in txt:
            set_of_cards.append(line)
    stream_of_cards = set_of_cards[1:]
    set_of_cards = parse_card(stream_of_cards)
    return set_of_cards


def parse_card(set_of_cards):

    """
    function to create a list of card objects
    :rtype: list
    :param set_of_cards: list of cards
    :return: list of card objects

    """
    card_objects = []
    for x in set_of_cards:
        c = Card()
        l = x.split()
        c.color = l[0]
        c.no_of_symbols = len(l[1])

        s = l[1]
        s = str(s[0])
        if s.istitle():
            c.shading = 'upper'
            if s is 'A':
                c.symbol = 'A'
            elif s is 'H':
                c.symbol = 'H'
            elif s is 'S':
                c.symbol = 'S'
        elif s.islower():
            c.shading = 'lower'
            if s is 'a':
                c.symbol = 'A'
            elif s is 'h':
                c.symbol = 'H'
            elif s is 's':
                c.symbol = 'S'
        else:
            c.shading = 'symbol'
            if s is '@':
                c.symbol = 'A'
            elif s is '#':
                c.symbol = 'H'
            elif s is '$':
                c.symbol = 'S'
        card_objects.append(c)
    return card_objects



