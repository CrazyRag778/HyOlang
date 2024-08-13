import sys
import pdb
import ast
import os

file_to_compile = open(sys.argv[1], "r+")

ccode = (file_to_compile.read()).split("\n")

allowed_module = {
    "FILE": 0,
}

for i in ccode:        
    i = i.split("-")
    for elem in i:
        elem.replace("&hypen", "-")
    if (i[0]=="rawPRINT "):
        print(i[1][2:-1], end="")
    if (i[0]=="PRINT "):
        print(i[1][2:-1])
    elif (i[0]=="fPRINT "):
        print(eval(i[1][1:]), end="")
    elif (i[0]=="LOOpRINT "):
        for iIndexEl in range(1, len(i)):
            print(i[iIndexEl][2:-2], end="")
    elif (i[0]=="TYPE "):
        print(f"<OBJECT {type(ast.literal_eval(i[1])).__name__}>", end="")
    elif (i[0]=="INPUT "):
        exec(f"{str(i[2][1:])}=input('{i[1][2:-2]}')")
    elif (i[0]=="showVAR "):
        print(eval(i[1][1:]), end="")
    elif (i[0]=="takeVAR "):
        exec(f"{i[1][1:-1]} = {i[2][1:]}")
    elif (i[0]=="ALLOW "):
        allowed_module[str(i[1][1:])] = 1
    elif (i[0]=="END"):
        exit()
    
    # BUILT-IN module
    # FILE module
    elif (i[0][0:5]=="FILE."):
        if (allowed_module["FILE"]==1):
            if (i[0][5:]=="ACCESS "):
                exec(f"{i[3][1:]} = open('{i[1][1:-1]}', '{i[2][1:-1].lower()}')")
            elif (i[0][5:]=="CLOSE "):
                exec(f"{i[1][1:]}.close()")
            elif (i[0][5:]=="CREATE "):
                exec(f"{i[2][1:]} = open('{i[1][1:-1]}', 'x')")
            elif (i[0][5:]=="DELETE "):
                exec(f"os.remove({i[1][1:]}.name)")        
    