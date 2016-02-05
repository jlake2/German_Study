#Flash Cards Program
#John F. Lake, Jr. 
#5 Feb 2016




def store_vocab_word(word):
	file = open('fcData/words.txt','a+'); 
	file.write(word); 
	file.write("\n"); 
	file.close(); 


def options(): 
	print "Options go here."
	print "Enter 1 to add a word.\n"
	print "Enter 2 to study.\n"
	print "Enter 3 to delete a word.\n"
		
	return int(raw_input(""))
	




def main():
		

	print "\n\n"
	print "WELCOME to the Deutsch Flash Card Simulator!  Please Enter Your option for study today!"
	print "\n\n"
	opt = options(); 


	if opt is 1: 
		print "Enter your vocabulary word for adding to the word list."
		word = raw_input("Format: word,definition\n")
		store_vocab_word(word); 
	elif opt is 2: 
		print "Study time!"
		end = 0
		words = {}

		try: 
			with open('fcData/words.txt','r') as file:
				for line in file: 
					wordDef = line.split(",")
					word = wordDef[0]
					d = wordDef[1]
					words[word] = d
			file.close()
		except: 
			print "There's a problem with your word list...shit."
		for key in words: 
			print words[key]
			resp = raw_input("")
			if resp.lower() in key.lower(): 
				print "RIGHT!"
			else: 
				print "WRONG!"
				

				










	
	



main(); 
