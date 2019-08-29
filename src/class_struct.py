class   Sep:
    AND     = 0
    OR      = 1
    XOR     = 2
    END     = 3

class   Node:
    def __init__(self, sep, node):
        self.sep = sep
        self.isneg = 0
        self.node = node

class   Graph:
    def __init__(self, key):
        self.key = key
        self.state = 0
        self.lst = []
    def add_rule(self, rule):
        self.lst.append(rule)
    def add_node(self, newnode, sep):
        self.lst[len(self.lst) - 1].append(Node(sep, newnode))  


