
Webcrawler for subdirectories
-----------------------------

Note: ensure directories text file 'dirs'txt' is in the same directory as the program 'crawler.py'. Ensure that it is spelt correctly , or change the hardcoded 'filePath' variable to match


usage: 

	python3 crawler.py <OPTIONAL: flag> <optional: website)

flags: 

-s   SUCCESS ONLY -- Only prints urls that return 200 code 
-ne  NO ERROR ------ Prints ALL urls that do NOT return 404 code
-a   ALL ----------- Prints all urls 

when ran as default:

	python3 crawler.py

the program will use the hardcoded variables (in this case MY metasploitable's mutillidae) to form the target website to crawl. 


Keyboard interrupt 'Ctrl + C' may be used at anytime to stop the program

When specifying a website, eg https://example.com, a flag MUST be specified, along with the proper scheme ('http://', 'https://') 



