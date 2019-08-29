import sys
import time
import math

class   Polynome:

    def __init__(self, degree, multi):
        self.degree = degree
        self.multi = multi
    
    def add_multi(self, add):
        self.multi += int(add)

class Color:
    RED = "\x1b[31m"
    GREEN = "\x1b[32m"
    YELLOW = "\x1b[33m"
    BLUE = "\x1b[34m"
    MAGENTA = "\x1b[35m"
    CYAN = "\x1b[36m"
    WHITE = "\x1b[1;37;40m"
    RESET = "\x1b[0m"
    ERROR = "\x1b[90m"

def get_max_pol(split):
    max = 0
    for spl in split:
        sp = spl.replace(' ', '')
        i = 0
        while i < len(sp):
            if sp[i] == 'X':
                if i + 2 < len(sp) and sp[i + 1] == '^' and sp[i + 2]:
                    if int(sp[i + 2]) > max:
                        max = int(sp[i + 2])
            i += 1
    print(max)

def is_degree(pol, degree):
    len_pol = len(pol)
    i = 0
    while (i < len(pol)):
        if (pol[i].degree == degree):
            return (i)
        i += 1
    return (-1)

def prepare_right(arg):
    len_arg = len(arg)
    i = 0
    while (i < len_arg):
        if (arg[i].find("-") == -1):
            arg[i] = "-" + arg[i]
        else:
            arg[i] = arg[i].replace('-', '')
        i += 1

def get_degree(degree):
    len_deg = len(degree)
    i = degree.find("X")
    if (i == len_deg - 1
            or (i != -1 and i + 1 < len_deg and degree[i + 1].isdigit == True)):
        return 1
    elif (i == -1):
        return (0)
    else:
        i = degree.find("^") + 1
        j = i
        while (j < len_deg and degree[j].isdigit()):
            j += 1
        return (int(degree[i:j]))


def get_param(pol):
    split = pol.split('*')
    print(pol)
    if (len(split) == 1):
        if (split[0].find("X") != -1):
            mul = split[0][:split[0].find("X")]
        else:
            mul = split[0]
        degree = split[0]
    else:
        if (split[0].isdigit() or (split[0][0] == '-' and split[0][1].isdigit())):
            mul = split[0]
            degree = split[1]
        else:
            mul = split[1]
            degree = split[0]
    if (mul == "-"):
        mul += "1"
    if (mul == ""):
        mul = "1"
    degree = get_degree(degree)
    return float(mul), int(degree)

def feed_poly(pol, lst):
    mul, degree = get_param(pol)
    for mod in lst:
        if mod.degree == degree:
            mod.add_multi(mul)
            return
    lst.append(Polynome(degree, mul))
                

def reduce_equ(equ):
    lst = []
    for mod in equ:
        feed_poly(mod, lst)
    return (lst)

def get_color(degree):
    if (degree == 0):
        col = Color.GREEN
    elif (degree == 1):
        col = Color.MAGENTA
    elif (degree == 2):
        col = Color.BLUE
    else:
        col = Color.RED
    print(col + "X^" + str(degree) + Color.RESET, end = '')

def ft_abs(nb):
    if (nb < 0):
        return (-nb)
    return (nb)

def get_reduced(mod, printed, count, max):
    if (mod.multi > 0):
        count += 1
    if (max < mod.degree):
        max = mod.degree
    if (mod.multi == 0):
        return (printed, max, count)
    if (printed != 0):
        if (mod.multi < 0):
            print(" - ", end = '')
            if (mod.multi != -1):
                print(str(-mod.multi) + " * ", end = '')
        else:
            print(" + ", end = '')
            if (mod.multi != 1):
                print(str(mod.multi) + " * ", end = '')
    else:
        if (ft_abs(mod.multi) != 1):
            print(str(mod.multi) + " * ", end = '')
        elif (mod.multi == -1):
            print("-", end = '')
    get_color(mod.degree)
    return (1, max, count)


def get_continu(equ):
    max = 0
    count = 0
    len_lst = len(lst)
    printed = 0
    print("Reduced form: ", end = '')
    for mod in lst:
        printed, max, count = get_reduced(mod, printed, count, max)
    print(" = 0")
    print("Polynomial degree: " + str(max))
    if (max > 2):
        print("The polynomial degree is stricly greater than 2, I can't solve.")
        sys.exit()
    if (count == 0):
        print("The equation is null, all of the numbers are solution.")
        sys.exit()

def ft_sqrt(nb, preci, rou):
    if (nb == 0):
        return (0)
    tmp = float(nb / 2)
    while (tmp > 1):
        if (round(tmp * tmp, rou) == float(nb)):
            return (tmp)
        elif (round(tmp * tmp, rou) < float(nb) and rou == 4):
            return (tmp)
        tmp = tmp - preci
        tmp = round(tmp, rou)
    return (ft_sqrt(nb, preci / 10, rou + 1))

def get_pos_sol(dis, a, b):
    x1 = (-b - ft_sqrt(dis, 1, 0)) / (2 * a)
    x2 = (-b + ft_sqrt(dis, 1, 0)) / (2 * a)
    if (x1 == 0):
        x1 = -x1
    if (x2 == 0):
        x2 = -x2
    if (x1 == x2):
        print(str(x1))
    else:
        print(str(x1) + " and " + str(x2))

def int_sqrt(nb):
    i = 1
    while (i <= nb / 2):
        if (i * i == nb):
            return (i)
        i += 1
    return (0)

def get_neg_sol(dis, a, b):
    tmp = int_sqrt(-dis)
    if (tmp != 0):
        if (b == 0):
            tmp = tmp / (2 * a)
            if (tmp == 1):
                print("-i and i")
            else:
                print("-" + str(tmp) + "i" + " and " + str(tmp) + "i")
            return
    print(str(-b) + " + i√" + str(-dis) + " / " + str(2 * a) + " and " + str(-b) + " - i√" +
          str(-dis) + " / " + str(2 * a))

def solve_first_deg(b, c):
    if (b == 0):
        print("The equation has no solution.")
        return
    print("The solution is:")
    if (c == 0):
        print("0")
        return
    print(-c / b)

def solve(equ):
    a = 0
    b = 0
    c = 0
    for mod in lst:
        if (mod.degree == 0):
            c = mod.multi
        elif (mod.degree == 1):
            b = mod.multi
        else:
            a = mod.multi
    if (a == 0):
        solve_first_deg(b, c)
        return
    dis = b * b - (4 * a * c)
    if (dis >= 0):
        if (dis == 0):
            print("Discriminant is equal to zero, the solution is:")
        else:
            print("Discriminant is strictly positive, the two solutions are:")
        get_pos_sol(dis, a, b)
    else:
        print("Discriminant is strictly negative, the two complex solutions are:")
        get_neg_sol(dis, a, b)
    

if (len(sys.argv) != 2):
    sys.exit()
arg = sys.argv[1]
arg = arg.upper()
arg = arg.replace(' ', '')
equ = arg.split('=')
arg_left = equ[0].replace('+', ' ').replace('-', ' -').split(' ')
arg_right = equ[1].replace('+', ' ').replace('-', ' -').split(' ')
if (len(arg_left[0]) == 0):
    arg_left.remove(arg_left[0])
if (len(arg_right[0]) == 0):
    arg_right.remove(arg_right[0])
prepare_right(arg_right)
arg_left.extend(arg_right)
lst = reduce_equ(arg_left)
max = get_continu(lst)
solve(lst)
#for mod in lst:
 #   print("degree : " + str(mod.degree) + "\nmul : " + str(mod.multi))
#get_max_pol(split)
#for sp in split:
#    tmp = sp.replace(' ', '')
#    print(tmp)


