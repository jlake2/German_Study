#Flash Cards Program
#John F. Lake, Jr. 
#5 Feb 2016




def store_word(word):


	file = open('words.txt','a+'); 
	
	file.write(word); 
	file.write("\n"); 

	file.close(); 


def options(): 

	print "Options go here."



def main():
		

	print "\n\n"
	print "WELCOME to the Deutsch Flash Card Simulator!  Please Enter Your option for study today!"
	print "\n\n"
	options(); 



	word = raw_input("Enter a word for testing purposes.")

	store_word(word); 





	
	



main(); 
