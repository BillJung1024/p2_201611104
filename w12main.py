﻿import os
mydir=os.getcwd()

def f1():
    mydir=os.getcwd()
    filename='python.txt'
    myfilename=os.path.join(mydir,filename)
    myfile=open(myfilename,'w')
    try:
        for line in myfile:
            if line.find('Python')>=0:
                print line
        myfile.close()  
    except IOError as e :
        print e

def f2():
    file2=open('output.txt','n')
    line1='first line\n'
    file2.write(line1)
    line2='\tsecond line \n'
    file2.write(line2)
    line3='third'
    file2.write(line3)
    file2.close()
    myfile2=open('output.txt','r')
    contentstwo=myfile2.readlines()
    for a in range(0,len(contentstwo)):
        if contentstwo[a].find('line') >= 0:
                result = contentstwo[a]
                print result.upper()
        myfile2.close()

def lab12():
    print "Homework1"
    dataone()
    print "Homework2"
    datatwo()

def main():
    lab12()
    



main()
raw_input("")