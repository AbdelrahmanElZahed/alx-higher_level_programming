#!/usr/bin/python3
'''Module that definrs myint inherts drom int.'''


class MyInt(int):
    '''MyInt is a rebel integer class.'''
    def __eq__(self, other):
        '''Invert equality comparison.'''
        return super().__ne__(other)
    def __ne__(self, other):
        '''Invert inequality comparison.'''
        return super().__eq__(other)

