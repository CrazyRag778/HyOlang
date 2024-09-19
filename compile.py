import sys
import pdb
import ast
import os

file_to_compile = open(sys.argv[1], "r+")

ccode = (file_to_compile.read()).replace('\n', '').split(';')

allowed_module = {
    "FILE": 0,
}

for i in ccode:
    # Splits the syntax into function and arguments
    i = i.split("-")
    # Removes leading whitespace
    if len(i[0]) > 0 and i[0][0] == " ":
        i[0] = i[0].lstrip()

    tempI = []
    for cO in i:
        tempI.append(cO.strip())
    i = tempI

    if (i[0]=="rawPRINT"):
        print(i[1], end="")
    elif (i[0]=="PRINT"):
        print(i[1])
    elif (i[0]=="fPRINT"):
        print(eval(i[1]), end="")
    elif (i[0]=="LOOpRINT"):
        for iIndexEl in range(1, len(i)):
            print(i[iIndexEl], end="")
    elif (i[0]=="TYPE"):
        print(f"<OBJECT {type(ast.literal_eval(i[1])).__name__}>", end="")
    elif (i[0]=="INPU"):
        exec(f"{str(i[2])}=input('{i[1]}')")
    elif (i[0]=="showVAR"):
        print(eval(i[1]), end="")
    elif (i[0]=="take"):
        exec(f"{i[1]} = {i[2]}")
    elif (i[0]=="@ALLOW"):
        allowed_module[str(i[1])] = 1
    elif (i[0]=="END"):
        exit()
    
    # BUILT-IN module
    # FILE module
    elif (i[0][0:5]=="FILE."):
        if (allowed_module["FILE"]==1):
            if (i[0][5:]=="ACCESS"):
                exec(f"{i[3]} = open('{i[1]}', '{i[2].lower()}')")
            elif (i[0][5:]=="CLOSE "):
                exec(f"{i[1]}.close()")
            elif (i[0][5:]=="CREATE "):
                exec(f"{i[2]} = open('{i[1]}', 'x')")
            elif (i[0][5:]=="DELETE "):
                exec(f"os.remove({i[1]}.name)")        
            elif (i[0][5:]=="WRITE "):
                exec(f"{i[1]}.write({i[2]})")    