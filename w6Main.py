def HighLow():
	import random
	guessesTaken = 0
	print('Hello! What is your name?')
	myName = input()
	number = random.randint(1,100)
	print('Well, ' + myName + ', I am thinking of a number between 1 and 100.')
	while guessesTaken < 6:
	    print('Take a guess.')
	    guess = input()
	    guess = int(guess)
    
	    guessesTaken = guessesTaken + 1

	    if guess < number:
        	print ("Your guess is too low.")
	    if guess > number:
	        print ("yout guess is too high.")
	    if guess == number:
	        break
def LeapYear(size):
	 if (size%4==0) and (size%100!=0 or size%400==0):
	        print "It's LeapYear!"
	 else:
	        print "Nooooaaah~"




	def lab6():
	        HighLow()
	        LeapYear()  

	def main():
	        lab6()
	
	
	if __name__=="__main__":
	    main()