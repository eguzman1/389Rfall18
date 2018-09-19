Writeup 3 - OSINT II, OpSec and RE
======

Name: *Erick Guzman*
Section: *0101*

I pledge on my honor that I have not given or received any unauthorized assistance on this assignment or examination.

Digital acknowledgement of honor pledge: *Erick Guzman*

## Assignment 3 Writeup

### Part 1 (100 pts)

1. One vulnerability is a weak password. He should be using a password that is not common. He should not use a password that has either been found by hackers nor easily something that is personal to him(something he likes,etc.). There is many things he can do to strengthen his password for his server. A simple search of "guidelines to making a strong password" is a good resource on how to make a very difficult for a hacker to use simple hacking techniques such as Brute Force. He should make a password of at least 8 charatcers, with a lower-case,upper-case number along with numbers and/or punctuation marks. He should basic passwords. these include using lower-case letters, words found in the dictionary, personal information(things he posts on social media), etc.

2. Another vulnerability is having an open port without having an extra layer of security. Fred could have an open port however he should use SSH keys so that not everyone could log into his server. People who log into his server would need the private key. Only the people with the private key are able to log in. If the person who has it loses it(deletes it) then that person can not log anymore unless they obtain another private key. This may not stop all hackers but it can increase security for his server by allowing only a select amount of people to log in. Thus, Fred should use SSH keys to allow people to log into the port(s)

3. Another vulneability is having an open port without having a firewall (could also use SSH keys). A firewall would allow Fred to only allow certain services (if any, in this case the flight records) to bebe or not be exposed to the network. This can block or restrict access to ports that should be or not be accessed to the public. He can put the server he has under a Internal Service. This means that only he(Krugster) can access that service within thr server. In this case, he does not want anyone to get through his server so in this case he would just put a firewall to block anyone from coming into except himself. I am also sure that you can have a firewall block all IPs expect his to allow him to come in.