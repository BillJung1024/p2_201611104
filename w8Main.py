def charCount():
	sentence='sangmyung university'
	d=dict()
	for c in word:
	    if c not in d:
	        d[c]=1
	    else:
	        d[c]=d[c]+1
        

	import matplotlib
	import matplotlib.pyplot as plt

	plt.bar( range(len(d)),d.values(), align='center')
	plt.xticks(range(len(d)), list(d.keys()))
	plt.show()

def lab8():
	charCount()

def main():
	lab8()

if__name__=="__main__":
	main()