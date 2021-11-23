import sys
from modules.Parser import Parser
from modules.Code import Code
from modules.CommandTypes import CommandTypes

def print_usage():
    print("python assembler.py <source>.asm <out>.hack")

def assemble(infile, outfile):
    for line in infile.readlines():

        #clean and skip lines
        clean_line = Parser.clean(line)
        if len(clean_line) == 0:
            continue
        
        command_type = Parser.commandType(clean_line)
        bin = ""
        if (command_type == CommandTypes.A_COMMAND):
            symbol = Parser.symbol(clean_line)
            bin = Code.a2bin(int(symbol))
        elif (command_type == CommandTypes.C_COMMAND):
            dest = Parser.dest(clean_line)
            comp = Parser.comp(clean_line)
            jump = Parser.jump(clean_line)
            bin = Code.c2bin(comp, dest, jump)
        elif (command_type == CommandTypes.L_COMMAND):
            symbol = Parser.symbol(clean_line)
            bin = Code.a2bin(int(symbol))
        else:
            raise ValueError("got a invalid command: " + clean_line)

        outfile.write(bin + "\n")

def main():
    if len(sys.argv) != 3:
        print_usage()
        return

    input_filepath = sys.argv[1]
    output_filepath = sys.argv[2]

    with open(output_filepath, 'w+') as outfile:
        with open(input_filepath, 'r') as infile:
            assemble(infile, outfile)



if __name__ == "__main__":
    main()