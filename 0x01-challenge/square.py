#!/usr/bin/python3

"""
a class representing a square
having class artributes of
width
"""


class Square():
    """
    class representing a square
    having class artributes of width
    and width
    """
    width = 0

    def __init__(self, *args, **kwargs):
        """
        declaration of the square
        class and asigning value to
        attributes using a loop
        """
        for key, value in kwargs.items():
            setattr(self, key, value)

    def area_of_my_square(self):
        """
        Area of the square
        is returened by geting product of width * width
        """
        return self.width * self.width

    def PermiterOfMySquare(self):
        """
        method to calculate the perimeter
        of the square
        """
        return (self.width * 2) * 2

    def __str__(self):
        """
        method to retuen string rep
        of the square
        """
        return "{}/{}".format(self.width, self.width)


if __name__ == "__main__":
    """
    the following will be executed
    when this code is run as the main
    function not imported
    """
    s = Square(width=12, height=9)
    print(s)
    print(s.area_of_my_square())
    print(s.PermiterOfMySquare())
