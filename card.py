class Card:

    def __init__(self, color=None, symbol=None, shading=None, no_of_symbols=None):
        """

        :param color: string
        :param symbol: string
        :param shading: string
        :param no_of_symbols: int

        """
        self.color = color
        self.symbol = symbol
        self.shading = shading
        self.no_of_symbols = no_of_symbols

    def __eq__(self, other):
        """
        Function to check whether two card objects are equal
        :param other: card object
        :return: boolean

        """
        return self.__dict__ == other.__dict__

    def __str__(self):
        """
        Function to generate the string representation of a card object
        :return:
        """
        second_part = ''
        if self.shading == 'upper':
            if self.symbol == 'A':
                second_part = self.no_of_symbols * 'A'
            elif self.symbol == 'S':
                second_part = self.no_of_symbols * 'S'
            elif self.symbol =='H':
                second_part = self.no_of_symbols * 'H'

        if self.shading == 'lower':
            if self.symbol == 'A':
                second_part = self.no_of_symbols * 'a'
            elif self.symbol == 'S':
                second_part = self.no_of_symbols * 's'
            elif self.symbol =='H':
                second_part = self.no_of_symbols * 'h'

        if self.shading == 'symbol':
            if self.symbol == 'A':
                second_part = self.no_of_symbols * '@'
            elif self.symbol == 'S':
                second_part = self.no_of_symbols * '$'
            elif self.symbol == 'H':
                second_part = self.no_of_symbols * '#'

        return self.color + " " + second_part





