# yo gurt
# im tired of classes

import os
import argparse
import subprocess

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
    "me": "self",
}


def make_gurt_style(gurt_code): # YO_GURT
    # no multiline string support for now
    gurt_code = gurt_code + " "
    
    final_code = ""

    double_quote_count = 0
    single_quote_count = 0
    is_comment = False
    in_f_string = False
    
    def is_actual_code():
        return double_quote_count == 0 and not is_comment
    
    i = 0
    while i < len(gurt_code):
        
        if gurt_code[i] == "#" and double_quote_count == 0:
            is_comment = True
            
        elif gurt_code[i] == "\n":
            is_comment = False
        
        if gurt_code[i] == "\"" and gurt_code[i-1] != "\\":
            double_quote_count += 1
            if gurt_code[i-1] == "f" and double_quote_count == 1:
                in_f_string = True
            else:
                in_f_string = False
            
        if gurt_code[i] == "'":
            single_quote_count += 1
        
        if gurt_code[i] == "{" and in_f_string:
            double_quote_count = 0

        if gurt_code[i] == "}" and in_f_string:
            double_quote_count = 1

        if single_quote_count % 2 == 0:
            if is_actual_code() and single_quote_count != 0:
                print("I DONT LIKE SINGLE QUOTES, ONLY USE DOUBLE (from gurt-thon's developers!)")
                exit()
            single_quote_count = 0
            
        if double_quote_count % 2 == 0:
            double_quote_count = 0
            single_quote_count = 0
    
        
        for condition in conditions:
            spaced_condition = " " + condition + " "
            
            if gurt_code[i:i+len(spaced_condition)] == spaced_condition and is_actual_code():
                final_code+=conditions[condition]
                i+=len(spaced_condition)-1

        for replacement in replacements:
            if gurt_code[i:i+len(replacement)] == replacement and is_actual_code():
                final_code+=replacements[replacement]
                i+=len(replacement)
                break
        
        for special in special_replace:
            if i-1 >= 0:
                if gurt_code[i-1].isalpha():
                    break
            if i+1 <= len(gurt_code)-1:
                if gurt_code[i+1].isalpha():
                    break
            if gurt_code[i:i+len(special)] == special and is_actual_code():
                final_code+=special_replace[special]
                i+=len(special)
                break

        try:
            final_code += gurt_code[i]
        except:
            pass
        i += 1 # gurt iterate

    return final_code
    
def gurtvert(infilename, outfilename):
    gurt_style_string = "true=True;false=False;yo=True;gurt=False;yap = print"
    
    with open(infilename, "r") as f:
        gurt_in = f.read()
        
    with open(outfilename, "w") as f:
        gurt_out = gurt_style_string + "\n" + make_gurt_style(gurt_in)
        f.write(gurt_out)

parser = argparse.ArgumentParser()
parser.add_argument("filename", help="The file you would like to import")
parser.add_argument("-dist", "--dist-folder", help="The folder where you want your outfile to be stored")
parser.add_argument("-a", "--args", help="Arguments to pass into the program", nargs="*")
args = parser.parse_args()

filename = args.filename

if args.dist_folder:
    dist_folder = args.dist_folder
else:
    dist_folder = "."

try:
    os.mkdir(dist_folder)
except OSError:
    pass

if os.path.splitext(filename)[1] == ".gurt":
    new_file = os.path.splitext(os.path.join(dist_folder, filename))[0] + ".py"
    
    gurtvert(filename, new_file)
    
    if isinstance(args.args, list):
        subprocess.call(["python", new_file] + args.args)
    else:
        subprocess.call(["python", new_file])

    
else:
    print("that file doesn't look like a gurt-thon file")