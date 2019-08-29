from class_struct import *

def     find_key(rule, key):
    i = 0
    rlen = len(rule)
    while (i < rlen):
        if (rule[i].key == key):
            return (i)
        i += 1
    return (-1)

def     save_rule(str, index, rule):
    for i in index:
        rule[i].add_rule([])
        j = 0
        tlen = len(str)
        while j < tlen:
            if (str[j].isalpha() == False):
                j += 1
                continue
            l = find_key(rule, str[j])
            if (l == -1):
                rule.append(Graph(str[j]))
                l = len(rule) - 1
            if j == tlen - 1:
                rule[i].add_node(rule[l], Sep.END)
            else:
                if str[j + 1] == '+':
                    rule[i].add_node(rule[l], Sep.AND)
                elif str[j + 1] == '|':
                    rule[i].add_node(rule[l], Sep.OR)
                elif str[j + 1] == '+':
                    rule[i].add_node(rule[l], Sep.XOR)
            j += 1


def     get_rule(tmp, rule):
    index = []
    for char in tmp[1]:
        if char == '#':
            break
        if char.isalpha():
            i = find_key(rule, char)
            if (i == -1):
                index.append(len(rule))
                rule.append(Graph(char))
            else:
                index.append(i)
    save_rule(tmp[0], index, rule)


def     get_assert(str, rule):
    i = 1;
    slen = len(str)
    while (i < slen):
        for elem in rule:
            if elem.key == str[i]:
                elem.state = 1
                break
        i += 1

def     parse_data(data):
    rule = []
    for str in data:
        dlen = len(str)
        if (dlen == 0 or str[0] == '#'):
            continue
        elif (str[0] == '='):
            asser = str.replace('=', '')
            get_assert(str, rule)
        elif (str[0] == '?'):
            quest = str.replace('?', '')
        else:
            get_rule(str.replace(' ', '').split("=>"), rule)
    return (rule, quest, asser)
