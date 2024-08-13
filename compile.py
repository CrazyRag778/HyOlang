import sys
import pdb
import ast

file_to_compile = open(sys.argv[1], "r+")

ccode = (file_to_compile.read()).split("\n")

def strCL(str_t):
    lt = []
    for i in str_t:
        lt.append(i)
def get_real_type(s):
    try:
        evaluated = ast.literal_eval(s)
        return type(evaluated).__name__
    except (ValueError, SyntaxError):
        return "str"  # If it's not a valid literal, it's just a string    

for i in ccode:        
    i = i.split("-")
    if (i[0]=="PRINT "):
        print(i[1][2:-1], end="")
    elif (i[0]=="fPRINT "):
        print(eval(i[1][1:]))
    elif (i[0]=="TYPE "):
        print(f"<OBJECT {get_real_type(i[1])}>")
    elif (i[0]=="INPUT "):
        exec(f"{str(i[2][1:])}=input(i[1][2:-2])")
    elif (i[0]=="showVAR "):
        print(eval(i[1][1:]))