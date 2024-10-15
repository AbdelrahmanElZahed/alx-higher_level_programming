#!/usr/bin/python3
class MyList(list):
    """A class that inherits from the built-in list class."""

    def print_sorted(self):
        """Print the list in ascending order.

        This method creates a sorted copy of the list and prints it,
        without modifying the original list.
        """
        print(sorted(self))

