import sys
sys.path.append("src")
import os.path
import structure as st
import interface as itfc

st.init()

if (len(sys.argv) == 1):
    read = ['A+B=>C', '=AB', '?C']
else:
    arg = sys.argv[1]
    if (os.path.isfile(arg) == False):
        print("File does not exist.")
        sys.exit()
    file = open(arg, "r")
    read = file.read().split('\n')
    file.close()
data = itfc.remove_comment(read)
for elem in data:
    print(elem)
itfc.set_interface(data)
st.root.mainloop()
