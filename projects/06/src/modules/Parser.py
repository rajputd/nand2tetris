from os import stat
from .CommandTypes import CommandTypes

class Parser:
    """Takes in a given *.asm file and allows it to be read line by line while providing useful semantic information"""

    @staticmethod
    def clean(line: str) -> str:
        stripped = line.strip()
        location = stripped.find("//")
        if (location == -1):
            return stripped
        else:
            return stripped[:location].strip()

    @staticmethod
    def commandType(line: str) -> CommandTypes:
        if "(" in line and ")" in line:
            return CommandTypes.L_COMMAND
        elif "@" == line[0]:
            return CommandTypes.A_COMMAND
        elif ";" in line or "=" in line:
            return CommandTypes.C_COMMAND
        else:
            return CommandTypes.INVALID_COMMAND

    @staticmethod
    def symbol(line: str) -> str:
        ctype = Parser.commandType(line)

        if ctype == CommandTypes.A_COMMAND:
            return line[1:]
        
        if ctype == CommandTypes.L_COMMAND:
            return line[1:-1]

        raise ValueError("Parser.symbol() can only handle A or L commands as input!")

    def dest(line: str) -> str:
        ctype = Parser.commandType(line)

        if ctype != CommandTypes.C_COMMAND:
            raise ValueError("Parser.dest() can only handle C commands as input!")
        
        location = line.find("=")
        if location == -1:
            return None
        
        return line[:location]
        

    def comp(line: str) -> str:
        ctype = Parser.commandType(line)

        if ctype != CommandTypes.C_COMMAND:
            raise ValueError("Parser.comp() can only handle C commands as input!")

        equals_location = line.find("=")
        semi_location = line.find(";")

        if equals_location == -1 and semi_location == -1:
            return None
        elif equals_location != -1 and semi_location == -1:
            return line[equals_location + 1:]
        elif equals_location == -1 and semi_location != -1:
            return line[:semi_location]
        else:
            line[equals_location+1:semi_location]

    def jump(line: str) -> str:
        ctype = Parser.commandType(line)

        if ctype != CommandTypes.C_COMMAND:
            raise ValueError("Parser.jump() can only handle C commands as input!")

        location = line.find(";")
        if location == -1:
            return None
        
        return line[location+1:]