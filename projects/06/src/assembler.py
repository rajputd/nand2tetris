import sys
from modules.Parser import Parser
from modules.Code import Code
from modules.CommandTypes import CommandTypes
from modules.SymbolTable import SymbolTable

def print_usage():
    print("python assembler.py <source>.asm <out>.hack")

def first_pass(infile) -> SymbolTable:
    table = SymbolTable()
    instruction_addr = 0
    for line in infile.readlines():
        #clean and skip lines
        clean_line = Parser.clean(line)
        if len(clean_line) == 0:
            continue

        command_type = Parser.commandType(clean_line)
        if (command_type == CommandTypes.A_COMMAND or command_type == CommandTypes.C_COMMAND):
            instruction_addr += 1
        elif (command_type == CommandTypes.L_COMMAND):
            symbol = Parser.symbol(clean_line)
            table.addEntry(symbol, instruction_addr)
        else:
            raise ValueError("got a invalid command: " + clean_line)

    return table

def second_pass(infile, outfile, table):
    ram_address = 16
    for line in infile.readlines():
        #clean and skip lines
        clean_line = Parser.clean(line)
        if len(clean_line) == 0:
            continue
        
        command_type = Parser.commandType(clean_line)
        bin = ""

        if (command_type == CommandTypes.A_COMMAND):
            symbol = Parser.symbol(clean_line)
            if symbol.isnumeric():
                symbol = int(symbol)
            else:
                if table.contains(symbol):
                    symbol = table.getAddress(symbol)
                else:
                    table.addEntry(symbol, ram_address)
                    symbol = ram_address
                    ram_address += 1
            bin = Code.a2bin(symbol)
        elif (command_type == CommandTypes.C_COMMAND):
            dest = Parser.dest(clean_line)
            comp = Parser.comp(clean_line)
            jump = Parser.jump(clean_line)
            bin = Code.c2bin(comp, dest, jump)
        elif (command_type == CommandTypes.L_COMMAND):
            continue
        else:
            raise ValueError("got a invalid command: " + clean_line)

        outfile.write(bin + "\n")

def assemble(infile, outfile):
    table = first_pass(infile)
    infile.seek(0)
    second_pass(infile, outfile, table)

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