#!/usr/bin/python3

""" Class Rectangel """


class Rectangle:

    """
    initialize rectangle:
    private instance property: width (int)
    private instance property: height (int)
    """

    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """ constructor method """
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

    @property
    def width(self):
        """ width retrieve """
        return self.__width

    @width.setter
    def width(self, value):
        """ set width """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")

        self.__width = value
        if value < 0:
            raise ValueError("width must be >= 0")
        return self.__width

    @property
    def height(self):
        """ retrieve height """
        return self.__height

    @height.setter
    def height(self, value):
        """ set height """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")

        self.__height = value
        if value < 0:
            raise ValueError("height must be >= 0")
        return self.__height

    def area(self):
        """ find rectangle area """
        return self.__height * self.__width

    def perimeter(self):
        """ find perimeter of rectangle """
        if self.__height == 0 or self.__width == 0:
            return 0
        else:
            return ((2 * self.__height)+(2 * self.__width))

    def __str__(self):
        """ class str: print rectangle with # char """
        if self.__height == 0 or self.__width == 0:
            return ""

        print_str = ""
        for i in range(self.__height):
            for j in range(self.__width):
                print_str += str(self.print_symbol)
            if i != self.__height - 1:
                print_str += "\n"
        return print_str

    def __repr__(self):
        """ return a string representation of an rectangle """
        return "Rectangle({}, {})".format(self.__width, self.__height)

    def __del__(self):
        """ when class object is deleted """
        Rectangle.number_of_instances -= 1
        print("Bye rectangle...")

    def bigger_or_equal(rect_1, rect_2):
        """ bigger or equal """
        if not isinstance(rect_1, Rectangle):
            raise TypeError('rect_1 must be an instance of Rectangle')
        if not isinstance(rect_2, Rectangle):
            raise TypeError('rect_2 must be an instance of Rectangle')
        return rect_1 if rect_1.area() >= rect_2.area() else rect_2

@classmethod
    def square(cls, size=0):
        """Return a new Rectangle with width and height equal to size."""
        return (cls(size, size))

    def __str__(self):
        """Return the printable representation of the Rectangle."""
        if self.__width == 0 or self.__height == 0:
            return ("")

        rect = []
        for i in range(self.__height):
            [rect.append(str(self.print_symbol)) for j in range(self.__width)]
            if i != self.__height - 1:
                rect.append("\n")
        return ("".join(rect))

    def __repr__(self):
        """Return the string representation of the Rectangle."""
        rect = "Rectangle(" + str(self.__width)
        rect += ", " + str(self.__height) + ")"
        return (rect)

    def __del__(self):
        """Print a message for every deletion of a Rectangle."""
        type(self).number_of_instances -= 1
        print("Bye rectangle...")
