from matplotlib import pyplot as plt 
import numpy as np 
import csv 

def create_graph(x,y,x_names,Algorithm,bar_width=0.25,opacity=0.75):
	 
	plt.ylabel('Bigram Scores')
	plt.title(Algorithm)
	plt.xticks(x,tuple(x_names),rotation='vertical')   # index + bar_width
	plt.legend()
	plt.tight_layout()
	plt.bar(x, y, bar_width,alpha=opacity,color='blue',label='Old Model',align='center')
	plt.show()

def main():
	fname = 'Sheet 1-Table 1.csv'
	algo = []
	with open(fname) as f:
		reader = csv.reader(f)
		data = list(reader)
	x_names = data[0][1:]	
	
	x = np.arange(len(x_names))

	for i in range(len(data)):
		if i==0:
			continue
		else:
			Algorithm = data[i][0]
			y = data[i][1:]	
			create_graph(x,y,x_names,Algorithm)

if __name__=='__main__':
	main()		

