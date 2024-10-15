#!/usr/bin/python3
'''Module for Mylist class.'''


class MyList(list):
    '''Custom MyList class.'''
    def print_sorted(self):
        '''Method for printing sorted list.'''
        print(sorted(self))

