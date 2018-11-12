## Assignment 9 Writeup

### Part 1 (60 Pts)
This part was easy given that the prompt given was literally telling us how to do it. I first made a loop to go through
 each password. Within that loop, I then iterated through the salt (all lower case letters) and pre-pending each lower 
 case letter onto the password and then comparing to the hash each time time. Example: if first password was hello, then each iteration would be ahello, bhello.... and then comparing it to the hashes given to get the correct output
  Answers are
  Salt: m            Password:   jordan
        u                        loveyou
	k                        neptune
 	p                        pizza

### Part 2 (40 Pts)
CMSC389R-{H4sh-5l!ngInG-h@sH3r
For this I was confused at first on what was happending. However, after running the nc command (hint) I noticed that th
e server was asking to basically hash the string given. This made me realize that I had to some how obtain the "hash" 
rovided by the server and the string and basically use a hash function to obtain an answer. I used regular expression to obtain the hash and the string I use the new function to c
reate a "hash function" instead of hard coding what hashes already existed. Thus at the end, the server printed the fla
g once I brute force
