import sys
import pdb
import ast

file_to_compile = open(sys.argv[1], "r+")

ccode = (file_to_compile.read()).split("\n")

for i in ccode:        
    i = i.split("-")
    for elem in i:
        elem.replace("&hypen", "-")
    if (i[0]=="PRINT "):
        print(i[1][2:-1], end="")
    elif (i[0]=="fPRINT "):
        print(eval(i[1][1:]), end="")
    elif (i[0]=="LOOpRINT "):
        for iIndexEl in range(1, len(i)):
            print(i[iIndexEl][2:-2], end="")
    elif (i[0]=="TYPE "):
        print(f"<OBJECT {type(ast.literal_eval(i[1])).__name__}>", end="")
    elif (i[0]=="INPUT "):
        exec(f"{str(i[2][1:])}=input(i[1][2:-2])")
    elif (i[0]=="showVAR "):
        print(eval(i[1][1:]), end="")
    elif (i[0]=="takeVAR "):
        exec(f"{i[1][1:-1]} = {i[2][1:]}")
    elif (i[0]=="END"):
        exit()