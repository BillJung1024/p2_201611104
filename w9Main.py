import matplotlib
import matplotlib.pyplot as plt
import turtle
wn=turtle.Screen()

def charCount():
    d=dict()
    word=raw_input("Write a word :")
    for c in word:
        if c not in d:
            d[c]=1
        else:
            d[c]+=1
    plt.bar(range(len(d)),d.values(), align='center')
    plt.xticks(range(len(d)), list(d.keys()))
    plt.show()

def countDigitsLetter(word):
    d=dict()
    d={"number":0, "word":0}
    for c in word:
        if c.isdigit()==True:
            d["number"]+=1
        elif c.isdigit()==False:
            d["word"]+=1
    

    plt.bar(range(len(d)),d.values(), align='center')
    plt.xticks(range(len(d)), list(d.keys()))
    plt.show()

def finddifference():
    myh=set()
    friendh=set()
    myh{'TV', 'phone', 'camera', 'fridger', 'mixer', 'audio', 'cd player', 'light', 'computer', 'notebook', 'recorder'}
    friendhouse={'coffee machine', 'radio', 'camera', 'running machine', 'ramp', 'computer', 'notebook', 'recorder'}
    print myh
    print friendh
    difference=myh.difference(friendh)
    print difference
    difference2=friendh.difference(myh)
    print difference2
    intersection=myh.intersection(friendh)
    print intersection
    union=myh.union(friendh)
    print union
     d=dict()
    for c in myh:
        if c not in d:
            d[c]=1
        else:
            d[c]+=1
    for c in friendh:
        if c not in d:
            d[c]=1
        else:
            d[c]+=1
    print d

def lab9():
    charCount()
    word=raw_input("Write a word :")
    countDigitsLetter(word)
    finddifference()

def main():
    lab9()

if __name__=="__main__":
    main()
