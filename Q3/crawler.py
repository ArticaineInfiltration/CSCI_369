import requests,sys,socket


meta_ip ="192.168.234.135" #Your Metasploitable’s IP can be different
target_website = "http://"+meta_ip+"/mutillidae"

##EDIT MANUALLY AS REQUIRED
filePath="./dirs.txt" 

def directory_bruteforce(target_website,md=1):
	dnsFail = 0
	
	"""
	MODES:

	 1 - prints ONLY 200 success codes  (-s)
	 2 - prints all NON 404 codes 		(-ne)
	 3 - prints all codes 				(-a)
	"""
	
	mode = md	
	
 	# force user to add scheme
	if not target_website.startswith(('http://', 'https://')):
		print("Please include scheme in website (e.g. https:// )")        
		return -1
	
	
	with open(filePath) as dir:
		try:
			for line in dir:
				to_append = line.strip()
				#print(to_append)  #--for debug
				if line =='' or line is None:
					continue
		            #get the response:
				try:
					url = target_website+"/"+to_append
					#print(f'url is:{url}')
					response = requests.get(url)
					#print(response)
					responseCode = response.status_code
					
					if mode ==3:
						print(f"[{responseCode}]\t"+url.strip())
					elif mode == 2:
						if responseCode != 404:
							print(f"[{responseCode}]\t"+url.strip())
					elif mode == 1:
						if responseCode == 200:
							print(f"[{responseCode}]\t"+url.strip())
							
				except requests.exceptions.ConnectionError as e:
					print(f'**DNS resolution error: Failed to resolve {url}. Skipping...')
					dnsFail = dnsFail +1
					if dnsFail > 1:
						print (f'\n**Failed to resolve {target_website}, please check website spelling..\n')
						break
				except Exception as e:
					print(f'**Error: {e} at directory listing:{line}')
					continue
			print('\n========== END OF LISTINGS ==========\n')	
					
		except KeyboardInterrupt:
			print("\n\nKeyboard interrupt received, exitting...\n")


if __name__ == "__main__":
	
	if len(sys.argv) >= 4:
		print('\nPlease ONLY specify 1 flag (-a, -s ,-ne) and an optional website url!\n')
		sys.exit()

	if len(sys.argv) == 2:
		
		if sys.argv[1] == '-a':
			directory_bruteforce(target_website,3)
		elif sys.argv[1] == '-s':
			directory_bruteforce(target_website,1)
		elif sys.argv[1] == '-ne':
			directory_bruteforce(target_website,2)
		else:
			print(f'\nFlag \"{sys.argv[1]}\" not valid. please try again!\n')
	
	elif len(sys.argv) == 3:
		
		if sys.argv[1] == '-a':
			directory_bruteforce(str(sys.argv[2]).strip(),3)
		elif sys.argv[1] == '-s':
			directory_bruteforce(str(sys.argv[2]).strip(),1)
		elif sys.argv[1] == '-ne':
			directory_bruteforce(str(sys.argv[2]).strip(),2)
		else:
			print(f'option {sys.argv[1]} not valid. please try again!')
	
	else:
		directory_bruteforce(target_website)
