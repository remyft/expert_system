class   Sep:
    AND = 0
    OR  = 1
    XOR = 2
    END = 3

class   Side:
    def __init__(self, sep, isneg, name, isbeg):
        self.name = name
        self.sep = sep
        self.isneg = isneg
        self.isbeg = isbeg

    def add_node(self, node):
        self.node = node

class   Bin_tree:
    def __init__(self, sep, isneg, name, isbeg, selfneg):
        self.side = Side(sep, isneg, name, isbeg)
        self.selfneg = selfneg

    def add_imp(self, sep, isneg, node, name, isbeg):
        self.imp = Side(sep, isneg, name, isbeg)
        self.imp.add_node(node)

class   Block:
    def __init__(self, name):
        self.name = name
        self.state = 0
        self.lst = []

def deal_imp(elem):
    try:
        if (elem.imp.sep == Sep.OR and (check_define(elem.imp.node) == False
                                    and elem.imp.node.state != 0)):
            return True
        elif (elem.imp.sep == Sep.AND):
            return True
        elif (elem.imp.sep == Sep.XOR and  check_define(elem.imp.node) == False):
            return True
    except RecursionError:
        return False
    return False

def check_define(block):
    if block.state == 1:
        return True
    elif block.state == -1:
        return False
    if len(block.lst) == 0:
        return False
    for elem in block.lst:
        if elem.side.isbeg == False:
            continue
        if (elem.side.sep == Sep.END and check_define(elem.side.name) == True):
            if (elem.imp.sep == Sep.END or deal_imp(elem) == True):
                return True
        elif (elem.side.sep == Sep.OR and
              (check_define(elem.side.name) == True or
              check_define(elem.side.node) == True)):
            #if elem.selfneg == True:
            #    block.state = -1
            #else:
            #    block.state = 1
            if (deal_imp(elem) == True):
                return True
        elif (elem.side.sep == Sep.AND and check_define(elem.side.name) == True
              and check_define(elem.side.node) == True):
            if (elem.imp.sep == Sep.END or deal_imp(elem) == True):
                return True
        #elif (elem.side.sep == Sep.XOR and 

    if block.state == 1:
        return (True)
    return (False)



list = ["A|B", "=>", "C|D"]

A = Block("A")
A.state = 1
B = Block("B")
B.state = 0
C = Block("C")
C.state = 0
D = Block("D")
D.state = -1
blocks = []
blocks.append(A)
blocks.append(B)
blocks.append(C)
blocks.append(D)
blockA = Bin_tree(Sep.OR, False, A, True, False)
blockB = Bin_tree(Sep.OR, False, B, False, False)
blockA.side.add_node(B)
#blockC.side.add_node(blockD)
C.lst.append(blockA)
D.lst.append(blockA)
C.lst[0].add_imp(Sep.OR, False, D, C, True)
D.lst[0].add_imp(Sep.OR, False, C, D, False)
print(list)
for elem in blocks:
    print(elem.name + " : ", end='')
    print(check_define(elem))
#A.lst[0].add_imp(Sep.AND, False, D.lst[0], C.lst[0])
#B.lst[0].add_imp(Sep.AND, False, D.lst[0], C.lst[0])

