def Multiplesof3and5(size):
    sum=0
    for i in range(size):
        if (i%3==0 or i%5==0):
            sum=sum+i
        print sum
Multiplesof3and5(1001)