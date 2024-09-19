import sys
import pdb
import ast
import os

file_to_compile = open(sys.argv[1], "r+")

ccode = (file_to_compile.read()).replace('\n', '').split(';')

allowed_module = {
    "FILE": 0,
}

for parsArg in ccode:
    # Splits the syntax into function and arguments
    parsArg = parsArg.split("-")
    # Removes leading whitespace
    if len(parsArg[0]) > 0 and parsArg[0][0] == " ":
        parsArg[0] = parsArg[0].lstrip()

    tempParsArg = []
    for cO in parsArg:
        tempParsArg.append(cO.strip())
    parsArg = tempParsArg

    if (parsArg[0] == "rawPRINT"):
        print(parsArg[1], end="")
    elif (parsArg[0] == "PRINT"):
        print(parsArg[1])
    elif (parsArg[0] == "fPRINT"):
        print(eval(parsArg[1]), end="")
    elif (parsArg[0] == "LOOpRINT"):
        for parsArgIndexEl in range(1, len(parsArg)):
            print(parsArg[parsArgIndexEl], end="")
    elif (parsArg[0] == "TYPE"):
        print(f"<OBJECT {type(ast.literal_eval(parsArg[1])).__name__}>", end="")
    elif (parsArg[0] == "INPU"):
        exec(f"{str(parsArg[2])}=input('{parsArg[1]}')")
    elif (parsArg[0] == "showVAR"):
        print(eval(parsArg[1]), end="")
    elif (parsArg[0] == "take"):
        exec(f"{parsArg[1]} = {parsArg[2]}")
    elif (parsArg[0] == "@ALLOW"):
        allowed_module[str(parsArg[1])] = 1
    elif (parsArg[0] == "END"):
        exit()
    
    # BUILT-IN module
    # FILE module
    elif (parsArg[0][0:5] == "FILE."):
        if (allowed_module["FILE"] == 1):
            if (parsArg[0][5:] == "ACCESS"):
                exec(f"{parsArg[3]} = open('{parsArg[1]}', '{parsArg[2].lower()}')")
            elif (parsArg[0][5:] == "CLOSE "):
                exec(f"{parsArg[1]}.close()")
            elif (parsArg[0][5:] == "CREATE "):
                exec(f"{parsArg[2]} = open('{parsArg[1]}', 'x')")
            elif (parsArg[0][5:] == "DELETE "):
                exec(f"os.remove({parsArg[1]}.name)")        
            elif (parsArg[0][5:] == "WRITE "):
                exec(f"{parsArg[1]}.write({parsArg[2]})")
