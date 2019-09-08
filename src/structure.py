import tkinter as tk
import tkinter.ttk as ttk
import interface as itfc

class   Rule:
    def __init__(self, frame):
        self.frame = frame
        #self.left = tk.StringVar()
        #self.right = tk.StringVar()
        #self.mid = ttk.Combobox(self.frame, values=["=>", "<=>"], width=5)
        #liste.set(mid)
    def create_rule(self, left, right, mid):
        self.left = tk.StringVar()
        self.left.set(left)
        entry = tk.Entry(self.frame, textvariable=self.left)
        entry.pack(side=tk.LEFT)
        self.mid = ttk.Combobox(self.frame, values=["=>", "<=>"], width=5,
                                state="readonly")
        self.mid.set(mid)
        self.mid.pack(side=tk.LEFT)
        self.right = tk.StringVar()
        self.right.set(right)
        entry = tk.Entry(self.frame, textvariable=self.right)
        entry.pack(side=tk.LEFT)
        button = tk.Button(self.frame, text="❌", command=lambda:[self.frame.destroy()])
        button.pack(side=tk.RIGHT)
        self.frame.pack()

def init():
    global root
    global data
    global quest
    global asser
    global rules
    rules = []
    root = tk.Tk()
    root.lift()
    root.attributes('-topmost',True)
    root.after_idle(root.attributes,'-topmost',False)
    root.bind("<Key>", itfc.keyboard)
    data = []
    quest = tk.StringVar()
    asser = tk.StringVar()
