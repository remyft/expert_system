import class_struct
import parsing
import solve
from tkinter import *

def     clavier(event):
    #global class_struct.fenetre
    touch = event.keysym
    if (touch == "Escape"):
        class_struct.fenetre.quit()
    elif (touch == "Return"):
        get_value()

def     get_value():
    #global class_struct.asser
    #global class_struct.quest
    tmp_ass = "=" + class_struct.asser.get()
    tmp_que = class_struct.quest.get()
    class_struct.rule = []
    for elem in class_struct.block:
       tmp = []
       tmp.append(elem.value[0].get().replace(' ', ''))
       tmp.append(elem.value[2].get().replace(' ', ''))
       parsing.get_rule(tmp, class_struct.rule)
    parsing.get_assert(tmp_ass, class_struct.rule)
    solve.solve_quest(class_struct.rule, tmp_que)


def     del_node():
    for elem in class_struct.block:
        if elem.frame.winfo_exists() == False:
            class_struct.block.remove(elem)
    for elem in class_struct.block:
        print(1, end='')
    print()


def     add_rule():
    frame = Frame(class_struct.fenetre, borderwidth=2, relief=GROOVE)
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
    class_struct.block.append(class_struct.Block(value, frame))
    entree = Entry(frame, textvariable=value[0], width=20)
    entree.pack(side=LEFT)
    entree = Entry(frame, textvariable=value[1], width=5)
    entree.pack(side=LEFT)
    entree = Entry(frame, textvariable=value[2], width=20)
    entree.pack(side=LEFT)

def     add_txt_rule(impl):
    frame = Frame(class_struct.fenetre, borderwidth=2, relief=GROOVE)
    frame.pack(side=TOP)
    bouton=Button(frame, text="❌", command=lambda: [frame.destroy(),
                                                      del_node()])
    bouton.pack(side=RIGHT)
    value = []
    value.append(StringVar())
    value.append(StringVar())
    value.append(StringVar())
    value[0].set(impl[0])
    value[1].set("=>")
    value[2].set(impl[1])
    class_struct.block.append(class_struct.Block(value, frame))
    entree = Entry(frame, textvariable=value[0], width=20)
    entree.pack(side=LEFT)
    entree = Entry(frame, textvariable=value[1], width=5)
    entree.pack(side=LEFT)
    entree = Entry(frame, textvariable=value[2], width=20)
    entree.pack(side=LEFT)

def     set_button(implies, frame, fasser):
    if (len(implies) == 0):
        ass = "A + B"
        imp = "C"
    else:
        ass = implies[0]
        imp = implies[1]
    bouton=Button(frame, text="❌", command=lambda: [frame.destroy(),
                                                          del_node()])
    bouton.pack(side=RIGHT)
    value = []
    value.append(StringVar())
    value.append(StringVar())
    value.append(StringVar())
    value[0].set(ass)
    value[1].set("=>")
    value[2].set(imp)
    if (len(class_struct.asser.get()) == 0):
        class_struct.asser.set("AB")
    if (len(class_struct.quest.get()) == 0):
        class_struct.quest.set("C")
    class_struct.block.append(class_struct.Block(value, frame))
    entree = Entry(frame, textvariable=value[0], width=20)
    entree.pack(side=LEFT)
    entree = Entry(frame, textvariable=value[1], width=5)
    entree.pack(side=LEFT)
    entree = Entry(frame, textvariable=value[2], width=20)
    entree.pack(side=LEFT)
    entree = Entry(fasser, textvariable=class_struct.asser, width=20)
    entree.pack()
    entree = Entry(fasser, textvariable=class_struct.quest, width=20)
    entree.pack()

def     set_graph():
    frame = Frame(class_struct.fenetre, borderwidth=2, relief=GROOVE)
    frame.pack(side=TOP)
    bframe = Frame(class_struct.fenetre, borderwidth=2, relief=GROOVE)
    bframe.pack(side=BOTTOM)
    brule=Button(bframe, text="➕", command=add_rule)
    brule.pack()
    refresh=Button(bframe, text="♻︎", command=get_value)
    refresh.pack()
    fasser = Frame(class_struct.fenetre, borderwidth=2, relief=GROOVE)
    fasser.pack(side=BOTTOM)
    get_asser = Frame(fasser, relief=GROOVE)
    get_asser.pack(side=LEFT)
    label = Label(get_asser, text="=")
    label.pack(side=TOP)
    label = Label(get_asser, text="?")
    label.pack(side=BOTTOM)
    return (frame, fasser)


def     get_graph():
    frame, fasser = set_graph()
    #global class_struct.frame
    
    if (len(class_struct.rule) == 0):
        set_button([], frame, fasser)
    class_struct.fenetre.mainloop()

