def bmi():
    height=input("height: ")
    weight=input("weight: ")
    print "%.1f"%height, "%.1f" % weight
    bmi=weight/(height*height)
    print "%.1f" %bmi
    if bmi <=18.5:
        print 'underweight'
    elif bmi>=18.5 and bmi<=23:
        print 'normalweight'
    elif bmi>=23 and bmi<=25:
        print 'overweight'
    elif bmi>=25 and bmi<=30:
        print 'obesity'
     