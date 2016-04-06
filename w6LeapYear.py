def LeapYear(size):
    if (size%4==0) and (size%100!=0 or size%400==0):
        print "It's LeapYear!"
    else:
        print "Nooooaaah~"
