#!/usr/bin/python3

def print_sorted_dictionary(a_dictionary):
    i = list(a_dictionary.keys())
    i.sort()
    for j in i:
        print("{:}: {:}".format(j, a_dictionary[j]))
