Writeup 10 - Crypto II
=====

Name: *Erick Guzman*
Section: *0101*

I pledge on my honor that I have not given or received anyunauthorized assistance on this assignment or examination.

Digital acknowledgement of honor pledge: *Erick Guzman*

## Assignment 10 Writeup

### Part 1 (70 Pts)
CMSC389R-{i_still_put_the_M_between_the_DV}
I bruteforced my way into getting the flag. First, I picked a message that would make my padding easier to code. Then I nc'd into the server and I put my message, and that returned the string for legit. Then I followed the comments to craft the payload. I started at 6 and for each number in between 6-15(inclusive) I recreated the secret+ message + padding + maliciuous  md5 block  and for each number between 6-15, I went back to the server and checked each answer that was produced until I got the answer I wanted(aka the Flag above)


### Part 2 (30 Pts)

Commands to encrypt the key provided and dumping it to message.private
gpg --import pgpassignment.key
gpg -e -u -r msg.txt (this prompted me to enter the people I want to able to look at the message)--> president@csec.uiacs.umd.edu 

After this it asked me to be sure I wanted to use key because there was no 
assurance that the key belongs to the named user, I pressed y 
and it encrypted the key
Done


1. Generating keys: gpg --gen-key
2. Impoting someone's key: gpg --import pubkey.asc
3. Encrypting: gpg -e -u "Your name" -r "Their name" msg.txt
