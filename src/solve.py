from class_struct import *

def     get_rule_res(rule):
    xor = 0
    is_def = False
    for elem in rule:
        is_def = is_define(elem.node)
        if (is_def):
            if ((elem.sep == Sep.OR or elem.sep == Sep.END) and xor == 0):
                return (True)
            elif (elem.sep == Sep.XOR):
                xor = 1
        else:
            if (xor == 1):
                return (True)
            if (elem.sep == Sep.END or elem.sep == Sep.AND):
                return (False)
    if (is_def and xor == 0):
        return (True)
    return (False)

def     is_define(node):
    if (node.state == 1):
        return (True)
    for rule in node.lst:
        if (get_rule_res(rule) == True):
            node.state = 1
            return (True)
    return (False)

def     solve_quest(rule, quest):
    true = ""
    false = ""
    for char in quest:
        find = 0
        for elem in rule:
            if elem.key == char and is_define(elem):
                true += char
                find = 1
                break
        if find == 0:
            false += char
    if len(true) == 0:
        print(false + " is false.")
    elif len(false) == 0:
        print(true + " is true.")
    else:
        print(true + " is true, " + false + " is false.")
