#!/usr/bin/python3

def simple_delete(a_dictionary, key=""):
    if key == a_dictionary.get(key):
        del a_dictionary[key]
    return a_dictionary
