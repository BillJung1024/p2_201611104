def sumList(aList):
    y=list()
    for i in range(0,aList):
        if i%4==0 and i%5!=0:
            y.append(i)
    sum=0
    for i in range(0,len(y)):
        sum+=y[i]
    mysum=sum
    return mysum
def lab6():
    "**** Programing"
    aList=1000
    labsum=sumList(aList)
    print labsum   
def main():
    lab6()
main()