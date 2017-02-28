
class set_of_three:

    def __init__(self, c1, c2, c3):
        self.c1 = c1
        self.c2 = c2
        self.c3 = c3

    def __str__(self):
        card_string = []
        attrs = ["c1", "c2", "c3"]
        for x in attrs:
            card_string.append(str(getattr(self, x)))
        card_string = sorted(card_string)
        result = ''
        for x in card_string:
            result += x
            result += ' '
        return result


