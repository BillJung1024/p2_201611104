def lab9():
	import math
	Locations=tuple()
	myList=list()

	(x1,y1)=(37.575869, 126.976637)
	Locations=[(37.576549, 126.98552), (37.571618, 126.976551), (37.574577, 	126.957754)]
	for i in Locations:
	    myList.append(math.sqrt((x1-i[0])**2+(y1-i[1])**2))
	print min(myList)

def main():
	lab9()




	