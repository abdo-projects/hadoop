#!/usr/bin/env python
"""A more advanced Reducer, using Python iterators and generators."""

from itertools import groupby
from operator import itemgetter
import operator

import sys

def read_mapper_output(file, separator='\t'):
    for line in file:
        yield line.rstrip().split(separator, 1)

def main(separator='\t'):
    # input comes from STDIN (standard input)
    data = read_mapper_output(sys.stdin, separator=separator)
    max_value = 0
    max_current_word =''
    maxValue = 0
    dict ={'First':0}

    for current_word, group in groupby(data, itemgetter(0)):
        try:
            total_count = sum(int(count) for current_word, count in group)
            dict[current_word]= total_count
        except ValueError:
            # count was not a number, so silently discard this item
            pass

    maxValue =  max(dict.values())
    for key, value in dict.items():
        if value == maxValue and 'True' in key:
            print(key, separator, value)
if __name__ == "__main__":
    main()