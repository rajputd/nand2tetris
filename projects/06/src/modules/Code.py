from os import stat


class Code:
    @staticmethod
    def dest(mnemonic: str) -> str:
        dest_to_bin = {
            None: "000",
            "None": "000",
            "M": "001",
            "D": "010",
            "MD": "011",
            "A": "100",
            "AM": "101",
            "AD": "110",
            "AMD": "111",
        }
        return dest_to_bin[mnemonic]
    
    @staticmethod
    def comp(mnemonic: str) -> str:
        comp_to_bin = {
            "0" : "0101010",
            "1" : "0111111",
            "-1" : "0111010",
            "D" : "0001100",
            "A" : "0110000",
            "!D" : "0001101",
            "!A" : "0110001",
            "-D" : "0001111",
            "-A" : "0110011",
            "D+1" : "0011111",
            "A+1" : "0110111",
            "D-1" : "0001110",
            "A-1" : "0110010",
            "D+A" : "0000010",
            "D-A" : "0010011",
            "A-D" : "0000111",
            "D&A" : "0000000",
            "D|A" : "0010101",
            "M" : "1110000",
            "!M" : "1110001",
            "-M" : "1110011",
            "M+1" : "1110111",
            "M-1" : "1110010",
            "D+M" : "1000010",
            "D-M" : "1010011",
            "M-D" : "1000111",
            "D&M" : "1000000",
            "D|M" : "1010101"
        }
        return comp_to_bin[mnemonic]

    @staticmethod
    def jump(mnemonic: str) -> str:
        jump_to_bin = {
            None: "000",
            "None": "000",
            "JGT": "001",
            "JEQ": "010",
            "JGE": "011",
            "JLT": "100",
            "JNE": "101",
            "JLE": "110",
            "JMP": "111",
        }

        return jump_to_bin[mnemonic]

    @staticmethod
    def c2bin(comp: str, dest: str, jump: str) -> str:
        comp_bin = Code.comp(comp)
        dest_bin = Code.dest(dest)
        jump_bin = Code.jump(jump)
        return "111" + comp_bin + dest_bin + jump_bin

    @staticmethod
    def a2bin(val: int) -> str:
        bin = "{0:015b}".format(val)
        return "0" + bin
