#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    i = []
    for a in range(list_length):
        try:
            i.append(my_list_1[a] / my_list_2[a])
        except ZeroDivisionError:
            i.append(0)
            print('division by 0')
            continue
        except IndexError:
            i.append(0)
            print('out of range')
            continue
        except TypeError:
            i.append(0)
            print('wrong type')
            continue
        finally:
            pass
    return i
