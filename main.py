import sys
sys.path.append("src")
import os.path
import parsing
import solve
import class_struct
import interface
from tkinter import *


class_struct.init()
class_struct.fenetre.bind("<Key>", interface.clavier)
        
class_struct.quest = StringVar()
class_struct.asser = StringVar()
if (len(sys.argv) < 2):
    interface.get_graph()
    sys.exit()
arg = sys.argv[1]
if (os.path.isfile(arg) == False):
    print("File does not exist.")
    sys.exit()
file = open(arg, "r")
data = file.read().split('\n')
class_struct.rule = parsing.parse_data(data, class_struct.quest, class_struct.asser)
solve.solve_quest(class_struct.rule, class_struct.quest.get())
file.close()
#get_graph(class_struct.rule, class_struct.quest, class_struct.asser)
