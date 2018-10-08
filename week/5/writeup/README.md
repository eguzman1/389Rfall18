Writeup 5 - Binaries I
======

Name: *Erick Guzman*
Section: *0101*

I pledge on my honor that I havie not given or received any unauthorized assistance on this assignment or examination.

Digital acknowledgement of honor pledge: Erick Guzman

## Assignment 5 Writeup

*Put your writeup words here in accordance to the Part 3 requirements*

This assignment was similar to a pass assignment I had in 216. However, it was a different assembler. My initial thoughts of them problem was to search how to a "for loop" in x86 and how to do control flow. I used the slides from lectrue tounderstand how to access the registers of the arguments. I then searched online to see the types of control flow statements such as jne (jump to a place in memory if the thing you are comparing is not equal to the other thing). I had trouble at first implementing this because I did not understand how to setup a for loop (I did not find examples on how to increment a variable to a point). However, i tried to certain operations such as inc(increment a variable) and then I used jne and je(compare if two are equal) to compare to the value in register that had the len value. I had issues such as seg faults because I had leave and after the leave statement I had a ret which ruined the program. That was the only bug I had. Also, I keep struggling to get the array to accept the value for the rdx register. However, by looking through piazza, I saw that someone used mov byte[] and so I tried that. When I first tried it, it gave me an error for invalid size so I tried different registers that given in table format in the lecture slides and I used sil (same as rsi register)

For part 2 I did not struggle at all. I followed the same process as part 1. However, the only thing I struggled was when I was trying to put the value that in src into the index in dst. It was not working(I do not remember the error) so i simply put the value into a variable and did the move [], temp register and it worked. 