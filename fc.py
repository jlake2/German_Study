#Flash Cards Program
#John F. Lake, Jr. 
#5 Feb 2016


import json
import os.path



#Stores a vocabulary word in a dictionary and saves it to a json file: 
def store_vocab_word(word,definition):
	wordDict = {}

	#if the json file exists, add to it.
	if os.path.isfile('fcData/words.json'):
		with open('fcData/words.json','r') as inFile:
			wordDict = json.load(inFile)
		wordDict[word] = definition

	#Otherwise, make a new json file
	else:
		wordDict[word] = definition
	with open('fcData/words.json','w') as file: 
		json.dump(wordDict,file)
		file.close(); 


#delete a particular vocabulary word; good for mistakes
def remove_vocab_word(word):
	wordDict = {}

	#if the json file exists, remove from it.
	if os.path.isfile('fcData/words.json'):
		with open('fcData/words.json','r') as file:
			wordDict = json.load(file)
			del wordDict[word]
		file.close(); 
		with open('fcData/words.json','w') as file: 
			json.dump(wordDict,file)
			file.close(); 


	#Otherwise, print an error
	else:
		print "Error.  There is no json file to delete from."

def show_wordList():
	if os.path.isfile('fcData/words.json'):
		with open('fcData/words.json','r') as inFile:
			wordDict = json.load(inFile)
			print wordDict

	else:
		print "No wordlist."

#Prints options for the user. 
def options(): 
	print "Options go here."
	print "Enter 1 to add a word.\n"
	print "Enter 2 to study.\n"
	print "Enter 3 to delete a word.\n"
	print "Enter 4 to see list.\n"
	print "Enter 5 to quit.\n"

	return int(raw_input(""))

#welcome "screen" or message or whatever: 
def welcome():
	print "\n\n"
	print "WELCOME to the Deutsch Flash Card Simulator!  Please Enter Your option for study today!"
	print "\n\n"

#Main function
def main():
	welcome();
	end = 0

	while not end:
		opt = options(); 

		#If the user wants to add a word to the json file: 
		if opt is 1: 
			print "Enter your vocabulary word for adding to the word list."
			inp = raw_input("Format: word,definition\n")
			inp = inp.split(",")
			store_vocab_word(inp[0],inp[1]); 

		#Study
		elif opt is 2: 
			print "Study time!"
			end = 0
			words = {}

			try: 
				with open('fcData/words.json','r') as file:
					words = json.load(file)
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

		#Remove a word from json file: 
		elif opt is 3:
			print "Enter your vocabulary word for removing from the word list."
			inp = raw_input("")
			remove_vocab_word(inp); 

		elif opt is 4:
			show_wordList()
			

		elif opt is 5:
			end = 1

					

				










	
	



main(); 
