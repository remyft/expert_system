import structure as st
import tkinter as tk
import tkinter.filedialog as tkf
from tkinter.messagebox import askquestion
import os.path

def rm_rules():
    for elem in st.rules:
        elem.frame.destroy()
    rules = []

def exit():
    rm_rules()
    st.root.destroy()
    st.root.quit()

def keyboard(event):
    touch = event.keysym
    if (touch == "Escape"):
        exit()
    elif (touch == "Return"):
        default()

def remove_comment(list):
    data = []
    for elem in list:
        find = elem.find('#')
        if (len(elem) == 0 or elem[0] == '#'):
            continue
        elif (find != -1):
            elem = elem[:find]
        if (elem[0] == '?'):
            st.quest.set(elem[1:])
            continue
        elif (elem[0] == '='):
            st.asser.set(elem[1:])
            continue
        data.append(elem)
    return (data)

def get_rule(str):
    if (str.find("<=>") != -1):
        split = str.split("<=>")
        mid = "<=>"
    else:
        split = str.split("=>")
        mid = "=>"
    frame = tk.Frame(st.root)
    rule = st.Rule(frame)
    rule.create_rule(split[0], split[1], mid)
    st.rules.append(rule)

def set_new_rule():
    frame = tk.Frame(st.root)
    rule = st.Rule(frame)
    rule.create_rule("A + B", "C", "=>")
    st.rules.append(rule)

def default():
    print("Quest : " + st.quest.get() + ", asser : " + st.asser.get())
    print("DEFAULT");

def import_file():
    filepath = tkf.askopenfilename(title="Open file", filetypes=[("all", ".txt")])
    if (os.path.isfile(filepath) == False):
        return
    file = open(filepath, "r")
    rm_rules()
    read = file.read().split('\n')
    file.close()
    data = remove_comment(read)
    for str in data:
        get_rule(str)

def deal_ask(event):
    global ask
    touch = event.keysym
    if touch == "Escape":
        ask.destroy()

def get_save():
    name = tkf.asksaveasfilename(defaultextension=".txt")
    if (name == ""):
        return 
    if (os.path.isfile(name) == True):
        file = open(name, "w")
    else:
        file = open(name, "x")
    for elem in st.rules:
        file.write(elem.left.get() + elem.mid.get() + elem.right.get() + "\n")
    file.write("=" + st.asser.get() + "\n")
    file.write("?" + st.quest.get() + "\n")
    file.close()

def set_menu():
    menubar = tk.Menu(st.root)
    file = tk.Menu(menubar, tearoff=0)
    file.add_command(label="Save", command=get_save)
    file.add_command(label="Import", command=import_file)
    file.add_separator()
    file.add_command(label="Exit", command=exit)
    menubar.add_cascade(label="File", menu=file)
    edit = tk.Menu(menubar, tearoff=0)
    edit.add_command(label="Add", command=set_new_rule)
    edit.add_command(label="Clean", command=rm_rules)
    menubar.add_cascade(label="Edit", menu=edit)
    help = tk.Menu(menubar, tearoff=0)
    help.add_command(label="About", command=default)
    menubar.add_cascade(label="Help", menu=help)
    st.root.config(menu=menubar)

def set_interface(data):
    set_menu()
    for str in data:
        get_rule(str)
    frame = tk.Frame(st.root)
    add = tk.Button(frame, text="➕", command=set_new_rule)
    add.pack(side=tk.TOP)
    reload = tk.Button(frame, text="♻︎", command=default)
    reload.pack(side=tk.TOP)
    asframe = tk.Frame(frame)
    aslabel = tk.Label(asframe, text='=')
    aslabel.pack(side=tk.LEFT)
    asentry = tk.Entry(asframe, textvariable=st.asser)
    asentry.pack(side=tk.LEFT)
    asframe.pack(side=tk.TOP)
    quframe = tk.Frame(frame)
    qulabel = tk.Label(quframe, text='?')
    qulabel.pack(side=tk.LEFT)
    quentry = tk.Entry(quframe, textvariable=st.quest)
    quentry.pack(side=tk.LEFT)
    solve = tk.Button(frame, text="SOLVE!", command=default)
    solve.pack(side=tk.BOTTOM)
    quframe.pack(side=tk.TOP)
    frame.pack(side=tk.BOTTOM)

