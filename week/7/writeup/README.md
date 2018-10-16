Writeup 7 - Forensics I
======

Name: *Erick Guzman*
Section: *0101*

I pledge on my honor that I have not given or received any unauthorized assistance on this assignment or examination.

Digital acknowledgement of honor pledge: *Erick Guzman*

## Assignment 7 writeup

### Part 1 (40 pts)

1. JPEG

2. Chicago, IL and John Hancock Center

3. 08/22/2018 at 11:33:24

4. iPhone 8

5. 539.5 m above sea level

6.CMSC389R-{look_I_f0und_a_str1ng}

### Part 2 (55 pts)

*SUBMIT YOUR WRITEUP DETAILING YOUR APPROACH AND SOLUTION TO THIS PROBLEM HERE (>250 words). Dont forget to include the flag!*
CMSC389R-{dropping_files_is_fun}
First, I looked up exactly what reveser enginnering was the the different approachs to do it. I came across various ways such as using gdb to step through the assembly program, using the strings command to see the commands it does and even using something called IDA. IDA sorta did help me by being able to look at all the code at once but it was not as useful using gdb. After struggling with figuring how to reverse the binary file I noticed that the program calls fputs and write. At first I got confused on if I had to provide a file however I noticed it said "Where is your flag?" This made me realize that the flag was getting written to a file in a directory. I figured this through gdb. It was getting written to my tmp file on my ubuntu machine. I went to the tmp file and copied the file into my home directory. I then realize that I could not simply open the image. This is because the image was broken. I needed a hex editor to fix the magic bytes of the file. The magic bytes of the file had a null byte in its first position. With a simple deletion of that, the file was able to made into a JPEG file. After I did that, I simply used the image of the dinosaur to realize that it was the passcode to the use to extract the hideen data by using steghide extract. That is how I got the flag.