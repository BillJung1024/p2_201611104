import turtle  
wn=turtle.Screen()  
t1=turtle.Turtle()  
print "Let's start Rock Sissor Paper"  
 
 B=raw_input("What boy show?? :") 
G=raw_input("What girl show?? :") 
 def winner((B), (G)):  
  	if(B==G):  
 		print "Draw"  
	elif(B=="Rock"):  
		if(G=="Sissor"):  
			print "B Win!!"  
 		elif(G=="Paper"):  
 			print "G Win!!"  
	elif(B=="Sissor"):  
 		if(G=="Rock"):  
 			print "G Win!!"  
 		elif(G=="Paper"):  
 			print "B Win!!"  
	elif(B=="Paper"):  
		if(G=="Rock"):  
			print "B Win!!"  
 		elif(G=="Sissor"):  
			print "G Win!!"  
  	else:  
  		print "Do it again"  


 winner(B,G)
 print "Game Over" 
  wn.exitonclick() 
