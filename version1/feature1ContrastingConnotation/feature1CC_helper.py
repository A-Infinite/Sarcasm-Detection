import io
import sys
from PreProcV1 import *
import csv
import re
from nltk import bigrams, ngrams
from collections import Counter
#reload(sys)
#sys.setdefaultencoding('utf-8')

trigram_list = []
bigram_list = []

def get_bigrams(inputFile, neg, pos):
	print("inside get_bigrams code")
	df = csv.reader(inputFile)
	neg_biwords_file = csv.writer(neg)
	pos_biwords_file = csv.writer(pos) 
	#m=0
	for row in df:
		# print row[3]
		row[1] = preprocess(row[1])
		row[1] = re.sub('\s+', ' ', row[1]).strip()
		if(row[0] == '0'):
			# negative
			neg_biwords = bigrams(row[1].split(" "))
			for w in neg_biwords:
				a = str(w[0] + w[1])
				bigram_list.append(a)
				neg_biwords_file.writerow([a]) 


		elif(row[0] == '1'):
			# positive
			pos_biwords = bigrams(row[1].split(" "))
			for w in pos_biwords:
				a = str(w[0] + w[1])
				if a not in bigram_list:
					bigram_list.append(a)
				pos_biwords_file.writerow([a])
		#m=m+1
		#if(m==10):
		#	return
	# print bigram_list
	print("exiting bigram code")

	return 

def generate_scores(output_file,neg_file, pos_file, wlist, str):
	writer = csv.writer(output_file)
	neg = csv.reader(io.open("negative_"+str+"s.csv", "r",encoding="utf-8"))
	pos = csv.reader(io.open("positive_"+str+"s.csv", "r",encoding="utf-8"))
	negative_Set = []
	for r in neg: 
		negative_Set.append(r[0])
	
	neg_counts = Counter(negative_Set)

	positive_Set = []
	for r in pos:
		positive_Set.append(r[0])
	
	pos_counts = Counter(positive_Set)

	p = 0.0
	n = 0.0
	score = 0.0

	for w in wlist:	
		try:
			p = pos_counts[w]
			n = neg_counts[w]
			score = (p-n)/(p+n)
		except:
			score = 0
		#print('writing')
		writer.writerow([w,score])

def get_trigrams(inputFile, neg, pos):
	df = csv.reader(inputFile)
	neg_triwords_file = csv.writer(neg)
	pos_triwords_file = csv.writer(pos) 
	#m=0
	for row in df:
		# print row[3]
		#rint(row[1])
		row[1] = preprocess(row[1])
		row[1] = re.sub('\s+', ' ', row[1]).strip()
		if(row[0] == '0'):
			# negative
			neg_triwords = ngrams(row[1].split(" "), 3)
			for w in neg_triwords:
				a = str(w[0] + w[1] + w[2])
				trigram_list.append(a)
				neg_triwords_file.writerow([a]) 

		elif(row[0] == '1'):
			# positive
			pos_triwords = ngrams(row[1].split(" "),3)
			print(pos_triwords)
			for w in pos_triwords:
				# print w
				a = str(w[0] + w[1] + w[2])
				if a not in trigram_list:
					trigram_list.append(a)
				pos_triwords_file.writerow([a]) 
		#m=m+1
		#if(m==10):
		#	return

	return 

input_file = open("sentiment_analysis.csv", "r")
# input_file2 = open("SentimentAnalysisDataset.csv", "r")

pos_bigram_data = open("positive_bigrams.csv", "w")
neg_bigram_data = open("negative_bigrams.csv", "w")
output_bigram_file = open("bigramscores.csv", "w")
get_bigrams(input_file, neg_bigram_data, pos_bigram_data)
print("pos-neg bigrams file generated")



pos_trigram_data = open("positive_trigrams.csv", "w")
neg_trigram_data = open("negative_trigrams.csv", "w")
output_trigram_file = open("trigramscores.csv", "w")
get_trigrams(input_file, neg_trigram_data, pos_trigram_data)
print("pos -neg trigrams file generated")



generate_scores(output_bigram_file, "positive_bigrams.csv", "negative_bigrams.csv", bigram_list, 'bigram')
print("bigram scores file generated")

generate_scores(output_trigram_file, "positive_trigrams.csv", "negative_trigrams.csv", trigram_list, 'trigram')
print("trigram scores file generated")
#print (trigram_list)



# pos_trigram_data = open("positive_trigrams.csv", "w")
# neg_trigram_data = open("negative_trigrams.csv", "w")
# output_trigram_file = open("trigramscores.csv", "w")
# get_trigrams(input_file2, neg_trigram_data, pos_trigram_data)
# generate_scores(output_trigram_file, "negative_trigrams.csv", "positive_trigrams.csv", trigram_list)
