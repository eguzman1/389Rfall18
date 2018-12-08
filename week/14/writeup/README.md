Writeup 10 - Crypto II
=====

Name: *Erick Guzman*
Section: *0101*

I pledge on my honor that I have not given or received any unauthorized assistance on this assignment or examination.

Digital acknowledgement of honor pledge: Erick Guzman*

## Assignment 10 Writeup

### Part 1 (70 Pts)
I researched various ways to do SQL injection. https://en.wikipedia.org/wiki/SQL_injection was the source. I skimmed it and stumbled upon the section
"Blind SQL injection". I noticed the line "So the URL ...." and I looked on the cornerstone website and noticed that it has the form "....?id=x", x 
being the number. Then I played around alittle with the URL on the website. When I played around with url, it had crashed when i did a simply id='1' because of how 
wikiepdia had it. From there I kept playing with it and it did not produce the flag I wanted. So searched up "SQL url injection" and stumbled upon this https://www.w3schools.com/sql/sql_injection.asp .
It helped me noticed that what the types of SQL lines could be possible. In this I noticed in lecture slides (regex) as well as the website a  
line called "SQL injection based 1=1 is always true" and under that title there was another one that showed an example of using strings so I started to do the same thing
as the example from the website but with single quotes. The example they had was " or " and I used the same for the cornerstone website. I 
played around with the URL and I kept getting errors. I tried id = 1 'or 1=1' then id = 'or 1=1' then id = 1 'or' 1=1 and that produced the flag. 
CMSC38R-{y0U-are_the_5ql_n1nja}

### Part 2 (30 Pts)

	1. I was confused on how to start so I looked at each hint. The second told me to use html  <h1> into the query and i noticed it made the font
		change for "try again" so then I realized it executed any command I Wanted so then i wrote the <script> alert(1) </script> and it worked
	 
	2. I looked at each hint and one of the hints said we could not use just a simple html tag and have to use a html tag that uses a javascript 
		the last hint mentioned the onerror so i searched that it showed me an example of <img src="image.gif" onerror="myFunction()">
		(https://www.w3schools.com/jsref/event_onerror.asp) so then i simply put <img src = "disdisF.jpg" onerror="alert(1)"/> into the
		the text box and it worked
	
	3. I looked at the hints and it guided towards the code. It told me to look at window location hash. 
		It said that it can be influenced by the attacker. It shows the the num variable can be manipulated. I realized
		that I can put a single quote inside num and inject the code in there. I followed the same logic as last problem
		I put a ' onerror = 'alert()' This would replace the num and be inserted between the string and " jpg'
	
	4. Right off the bat, I inserted something, such as fdnjkefnjksde, and I noticed the timer basically executed that. This made me realize
	This was similar to levdl 1 and made me realize i can put a command inside the timer bar. THe hint mentions the source code.
	I go to the source code and notice the function evalutes what '{{timer}}' has inside its brackets. I can insert JS code into the create timer bar 
	So i put 1');alert('dd  which worked.

	5. In the hint it mentions to look up the signup.html. I also looked at the welcome.html. I noticed that in signup it executes whatever is in next
	and going to the welcome.html, confirm is passed into next. This is seen when you press the sign up button (in the URL). Now I can simply
	change confirm in the URL into the required JS command. I simply changed the url to https://xss-game.appspot.com/level5/frame/signup?next=javascript:alert()

	6. Looking at the source code and hints, it leads to me to index.html and the use of regex. Some of the comments says things such as
	"this will totally prevent us from loading evil URLs."  The hint also says how # will influence the loaded script as well as the last hint that 
	tells me to basically put https://www.google.com/jsapi?callback=(foo being a function) into the url. These hints mixed with the regex in the source
	code, I put 
	Https://xss-game.appspot.com/level6/frame#Https://www.google.com/jsapi?callback=alert that basically calls the alert function and thus wins
	the game