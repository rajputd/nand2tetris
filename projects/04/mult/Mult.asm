// This file is part of www.nand2tetris.org
// and the book "The Elements of Computing Systems"
// by Nisan and Schocken, MIT Press.
// File name: projects/04/Mult.asm

// Multiplies R0 and R1 and stores the result in R2.
// (R0, R1, R2 refer to RAM[0], RAM[1], and RAM[2], respectively.)
//
// This program only needs to handle arguments that satisfy
// R0 >= 0, R1 >= 0, and R0*R1 < 32768.

// Put your code here.

//create a counter and sum variable both set to zero
@sum
M=0
@counter
M=0
//while counter < R0
(LOOP)
    
    // set D = R0 - counter
    @counter
    D=M
    @R0
    D=M-D
    
    // jump to end if R0 == counter
    @END
    D;JEQ

    // add R1 to sum
    @R1
    D=M
    @sum
    M=D+M

    // increment counter
    @counter
    M=M+1

    //jump to top of loop
    @LOOP
    0;JMP

(END)

// write sum to R2
@sum
D=M
@R2
M=D
