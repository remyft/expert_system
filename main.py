import sys
sys.path.append("src")
import os.path
import parsing
import solve
from tkinter import *

class   Block:
    def     __init__(self, value, frame):
        self.value = value
        self.frame = frame

value = []
fenetre = Tk()
block = []
rule = []
quest = ""
asser = ""
def     clavier(event):
    global fenetre
    touch = event.keysym
    fenetre.quit()

fenetre.bind("<Escape>", clavier)
def clavier(event):
    global value
    touche = event.keysym
    print(touche)

def     get_value():
    global rule
    global block
    global asser
    global quest
    asser = "=" + block[0].value[3].get()
    quest = block[0].value[4].get()
    rule = []
    for elem in block:
       tmp = []
       tmp.append(elem.value[0].get().replace(' ', ''))
       tmp.append(elem.value[2].get().replace(' ', ''))
       parsing.get_rule(tmp, rule)
    parsing.get_assert(asser, rule)
    solve.solve_quest(rule, quest)


def     del_node():
    global block
    for elem in block:
        if elem.frame.winfo_exists() == False:
            block.remove(elem)
    for elem in block:
        print(1, end='')
    print()


def     add_rule():
    frame = Frame(fenetre, borderwidth=2, relief=GROOVE)
    frame.pack(side=TOP)
    bouton=Button(frame, text="❌", command=lambda: [frame.destroy(),
                                                      del_node()])
    bouton.pack(side=RIGHT)
    value = []
    value.append(StringVar())
    value.append(StringVar())
    value.append(StringVar())
    value[0].set("A + B")
    value[1].set("=>")
    value[2].set("C")
    block.append(Block(value, frame))
    entree = Entry(frame, textvariable=value[0], width=20)
    entree.pack(side=LEFT)
    entree = Entry(frame, textvariable=value[1], width=5)
    entree.pack(side=LEFT)
    entree = Entry(frame, textvariable=value[2], width=20)
    entree.pack(side=LEFT)


def     get_graph(rule, quest, asser):
    frame = Frame(fenetre, borderwidth=2, relief=GROOVE)
    frame.pack(side=TOP)
    bframe = Frame(fenetre, borderwidth=2, relief=GROOVE)
    bframe.pack(side=BOTTOM)
    brule=Button(bframe, text="➕", command=add_rule)
    brule.pack()
    refresh=Button(bframe, text="♻︎", command=get_value)
    refresh.pack()
    asser = Frame(fenetre, borderwidth=2, relief=GROOVE)
    asser.pack(side=BOTTOM)
    get_asser = Frame(asser, relief=GROOVE)
    get_asser.pack(side=LEFT)
    label = Label(get_asser, text="=")
    label.pack(side=TOP)
    label = Label(get_asser, text="?")
    label.pack(side=BOTTOM)

    if (len(rule) == 0):
        bouton=Button(frame, text="❌", command=lambda: [frame.destroy(),
                                                          del_node()])
        bouton.pack(side=RIGHT)
        value = []
        value.append(StringVar())
        value.append(StringVar())
        value.append(StringVar())
        value.append(StringVar())
        value.append(StringVar())
        value[0].set("A + B")
        value[1].set("=>")
        value[2].set("C")
        value[3].set("AB")
        value[4].set("C")
        block.append(Block(value, frame))
        entree = Entry(frame, textvariable=value[0], width=20)
        entree.pack(side=LEFT)
        entree = Entry(frame, textvariable=value[1], width=5)
        entree.pack(side=LEFT)
        entree = Entry(frame, textvariable=value[2], width=20)
        entree.pack(side=LEFT)
        entree = Entry(asser, textvariable=value[3], width=20)
        entree.pack()
        entree = Entry(asser, textvariable=value[4], width=20)
        entree.pack()

        
    fenetre.mainloop()

if (len(sys.argv) < 2):
    get_graph(rule, quest, asser)
    sys.exit()
arg = sys.argv[1]
if (os.path.isfile(arg) == False):
    print("File does not exist.")
    sys.exit()
file = open(arg, "r")
data = file.read().split('\n')
rule, quest, asser = parsing.parse_data(data)
solve.solve_quest(rule, quest)
get_graph(rule, quest, asser)
