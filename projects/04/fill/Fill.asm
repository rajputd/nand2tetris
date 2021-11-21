// This file is part of www.nand2tetris.org
// and the book "The Elements of Computing Systems"
// by Nisan and Schocken, MIT Press.
// File name: projects/04/Fill.asm

// Runs an infinite loop that listens to the keyboard input.
// When a key is pressed (any key), the program blackens the screen,
// i.e. writes "black" in every pixel;
// the screen should remain fully black as long as the key is pressed. 
// When no key is pressed, the program clears the screen, i.e. writes
// "white" in every pixel;
// the screen should remain fully clear as long as no key is pressed.

// Put your code here.

//INIT SCREEN_END VARIABLE
@SCREEN
D=A
@8000
D=D+A
@SCREEN_END
M=D


//infinite loop start
(MAIN)
    
    //CHECK KEYBOARD AND SET SCREEN_COLOR VAR
    @CHECK_KBD
    0;JMP
    (CHECK_KBD_END)

    //write to screen
    @WRITE_TO_SCREEN
    0;JMP
    (WRITE_TO_SCREEN_END)
//loop back to top
@MAIN
0;JMP

//write to screen
(WRITE_TO_SCREEN)

    //INIT SCREEN POINTER TO START OF SCREEN MAP
    @SCREEN
    D=A
    @SCREEN_POINTER
    M=D

    //write loop
    (WRITE_SCREEN_LOOP)
        //CHECK IF WE ARE AT END OF MAP
        @SCREEN_END
        D=M
        @SCREEN_POINTER
        D=D-M
        
        //GO TO LOOP END IF SCREEN_POINTER == SCREEN_END
        @WRITE_SCREEN_LOOP_END
        D;JEQ

        //WRITE SCREEN_COLOR TO M[SCREEN_POINTER]
        @SCREEN_COLOR
        D=M
        @SCREEN_POINTER
        A=M
        M=D

        //INCREMENT SCREEN_POINTER
        @SCREEN_POINTER
        M=M+1

        //GO BACK TO TOP OF LOOP
        @WRITE_SCREEN_LOOP
        0;JMP        

    (WRITE_SCREEN_LOOP_END)

    //GO BACK TO CALLER
    @WRITE_TO_SCREEN_END
    0;JMP

//check if keyboard key is pressed
(CHECK_KBD)
    //load keyboard address
    @KBD
    D=M

    @SET_WHITE
    D;JEQ

    //SET BLACK
    @SCREEN_COLOR
    M=-1
    @CHECK_KBD_END
    0;JMP

    (SET_WHITE)
    @SCREEN_COLOR
    M=0
    @CHECK_KBD_END
    0;JMP

