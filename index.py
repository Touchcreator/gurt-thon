true=True;false=False;yo=True;gurt=False;yap=print;gettypeof=type;
# new releases will be written in gurt-thon and compiled in the older version
# IF THIS COMMENT IS IN A .PY FILE, IT HAS BEEN COMPILED FROM GURT SOURCE CODE!!!

# GURT-THON WILL TREAT LINES WITHIN 3 QUOTES AS REAL CODE, USE \n IF YOURE WORRIED

import os
import argparse
import subprocess
import random

conditions = { # "gurtversion": "pyversion"
    "goons like": "==",
    "goons different than": "!=",
    "goons less than": "<",
    "goons more than": ">",
    "goons less or like": "<=",
    "goons more or like": ">="
}

replacements = { # conditions but smarter
    "pmo ": "import ",
    "type": "class",
    "gurtfunc ": "def ",
    "sybau": "exit()",
    # "types"
    "gurtint ": "",
    "gurtstr ": "",
    "gurtlist ": "",
    "gurttuple ": "",
    "gurtdict ": "",
    "gurtbool ": "",

}

special_replace = {
    
}

random_replace = { # basically, its just the operations, but it replaces shit randomly (like during compilation), use tuples!!
    "plus or minus": ("+", "-")
}

def make_gurt_style(gurt_code): # YO_GURT
    # no multiline string support for now
    gurt_code = gurt_code + " "
    
    final_code = ""

    double_quote_count = 0
    single_quote_count = 0
    is_comment = gurt
    in_f_string = gurt
    
    def is_actual_code():
        return double_quote_count== 0 and not is_comment== yo
    
    i = 0
    while i< len(gurt_code):
        
        if gurt_code[i]== "#" and double_quote_count== 0:
            is_comment = yo
            
        elif gurt_code[i]== "\n":
            is_comment = gurt
        
        if gurt_code[i]== "\"" and gurt_code[i-1]!= "\\": #" needed to fix quote errors (i suck at code)
            double_quote_count += 1
            if gurt_code[i-1] ==  "f" and double_quote_count ==  1:
                in_f_string = yo
            else:
                in_f_string = gurt
            
        if gurt_code[i]== "'":
            single_quote_count += 1
        
        if gurt_code[i]== "{" and in_f_string:
            double_quote_count = 0

        if gurt_code[i]== "}" and in_f_string:
            double_quote_count = 1

        if single_quote_count % 2== 0:
            if is_actual_code() and single_quote_count!= 0:
                yap("I DONT LIKE SINGLE QUOTES, ONLY USE DOUBLE (from gurt-thon's developers!)") # (I HATE GURT)
                dispose()
                exit()
            single_quote_count = 0
            
        if double_quote_count % 2== 0:
            double_quote_count = 0
            single_quote_count = 0
    
        
        for condition in conditions:
            spaced_condition = " " + condition + " "
            
            if gurt_code[i:i+len(spaced_condition)]== spaced_condition and is_actual_code():
                final_code+=conditions[condition]
                i+=len(spaced_condition)-1

        for stupid in random_replace:
            spaced_stupid = " " + stupid + " "
            
            if gurt_code[i:i+len(spaced_stupid)]== spaced_stupid and is_actual_code():
                final_code+=random.choice(random_replace[stupid])
                i+=len(spaced_stupid)-1

        for replacement in replacements:
            if replacement[-1] == " ":
                if gurt_code[i:i+len(replacement)]== replacement and is_actual_code():
                    final_code+=replacements[replacement]
                    i+=len(replacement)
                    break
            else:
                if gurt_code[i:i+len(replacement)]== replacement and is_actual_code():
                    if gurt_code[i-1].isspace() and gurt_code[i+len(replacement)].isspace():
                        final_code+=replacements[replacement]
                        i+=len(replacement)
                        break
        
        for special in special_replace:
            if i-1>= 0:
                if gurt_code[i-1].isalpha():
                    break
            if i+1<= len(gurt_code)-1:
                if gurt_code[i+1].isalpha():
                    break
            if gurt_code[i:i+len(special)]== special and is_actual_code():
                final_code+=special_replace[special]
                i+=len(special)
                break

        try:
            final_code += gurt_code[i]
        except:
            pass
        i += 1 # gurt iterate

    constant_vars = []

    for line in final_code.splitlines():
        stripped_line = line.strip()
        splitted_line = stripped_line.split()

        if len(splitted_line)> 2:
            if splitted_line[0]== "const":
                constant_vars.append(splitted_line[1])
            if (splitted_line[1]== "=" and splitted_line[0] in constant_vars) or splitted_line[0][-1]== "=":
                yap("you cant change a constant value")
                dispose()
                exit()

    double_quote_count = 0
    single_quote_count = 0
    is_comment = gurt
    in_f_string = gurt
    gurt_code = final_code
    final_code = ""
    i = 0

    while i< len(gurt_code):

        if gurt_code[i]== "#" and double_quote_count== 0:
            is_comment = yo
            
        elif gurt_code[i]== "\n":
            is_comment = gurt
        
        if gurt_code[i]== "\"" and gurt_code[i-1]!= "\\": #" needed to fix quote errors (i suck at code)
            double_quote_count += 1
            if gurt_code[i-1] ==  "f" and double_quote_count ==  1:
                in_f_string = yo
            else:
                in_f_string = gurt
            
        if gurt_code[i]== "'":
            single_quote_count += 1
        
        if gurt_code[i]== "{" and in_f_string:
            double_quote_count = 0

        if gurt_code[i]== "}" and in_f_string:
            double_quote_count = 1

        if single_quote_count % 2== 0:
            if is_actual_code() and single_quote_count!= 0:
                yap("I DONT LIKE SINGLE QUOTES, ONLY USE DOUBLE (from gurt-thon's developers!)") # (I HATE GURT)

                dispose()
                exit()
            single_quote_count = 0
            
        if double_quote_count % 2== 0:
            double_quote_count = 0
            single_quote_count = 0

        if gurt_code[i:i+len("const ")]== "const " and is_actual_code():
            i+=len("const ")

        try:
            final_code += gurt_code[i]
        except:
            pass

        i += 1

    # now i need to remove those starts and ends
    split_final = final_code.splitlines()
    realrealfinal = ""
    i = 1
    while i< len(split_final) - 1:
        realrealfinal += split_final[i] + "\n"

        i += 1

    return realrealfinal
    
def gurtvert(infilename, outfilename):
    gurt_style_string = "true=True;false=False;yo=True;gurt=False;yap=print;gettypeof=type;"
    
    with open(infilename, "r") as f:
        gurt_in = f.read()
        
    with open(outfilename, "w") as f:
        gurt_out = gurt_style_string + "\n" + make_gurt_style(gurt_in)
        f.write(gurt_out)

def check_doctype(infile):
    with open(infile, "r") as f:
        lines = f.read().splitlines()
        if lines[0].strip()== "<!DOCTYPE gurt>" and lines[-1].strip()== "<!END gurt>":
            return yo
        else:
            return gurt

parser = argparse.ArgumentParser()
parser.add_argument("filename", help="The file you would like to import")
parser.add_argument("-dist", "--dist-folder", help="The folder where you want your outfile to be stored")
parser.add_argument("-a", "--args", help="Arguments to pass into the program", nargs="+")
parser.add_argument("-d", "--dispose", help="Whether or not to dispose of files ran", action="store_true")
args = parser.parse_args()

filename = args.filename
to_dispose = args.dispose

if args.dist_folder:
    dist_folder = args.dist_folder
else:
    dist_folder = "."

try:
    os.mkdir(dist_folder)
except OSError:
    pass

new_file = os.path.splitext(os.path.join(dist_folder, filename))[0] + ".py"

def dispose():
    try:
        os.remove(new_file)
    except:
        pass

if os.path.splitext(filename)[1]== ".gurt":
    
    if check_doctype(filename)== yo:
        gurtvert(filename, new_file)
        
        if isinstance(args.args, list):
            subprocess.call(["python", new_file] + args.args)
        else:
            subprocess.call(["python", new_file])

        if to_dispose== yo:
            dispose()
    else:
        yap("you need to have doctype and end!")

    
else:
    print("that file doesn't look like a gurt-thon file")

