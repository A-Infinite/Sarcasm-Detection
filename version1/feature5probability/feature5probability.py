import csv
import os

pwd = os.getcwd()
norm_input = pwd + "/../dataset/normal_with_past_PP"
sarc_input = pwd + "/../dataset/sarcastic_with_past_PP"
csvfile = open("feature5probability.csv","a")
f5 = csv.writer(csvfile,delimiter=",")

ctr =1
for f in sorted(os.listdir(norm_input)):
	print(ctr)
	input_file = open(os.path.join(norm_input, f), "r")
	reader = csv.reader(input_file)
	reader = list(reader)
	required = reader[1][2]
	letters = required.split(" ")
	let = "".join(letters)
	letters = []
	for c in let:
		letters.append(c)
	tot_letts = len(letters)
	letters = list(set(letters))
	if(tot_letts != 0):
		prob = len(letters)/tot_letts
	temp = []
	temp.append(prob)
	temp.append(tot_letts)
	temp.append(0)
	f5.writerow(temp)
	input_file.close()
	ctr=ctr+1

for f in sorted(os.listdir(sarc_input)):
	print(ctr)
	input_file = open(os.path.join(sarc_input, f), "r")
	reader = csv.reader(input_file)
	reader = list(reader)
	required = reader[1][2]
	letters = required.split(" ")
	letters = "".join(letters)
	let = "".join(letters)
	letters = []
	for c in let:
		letters.append(c)
	tot_letts = len(letters)
	letters = list(set(letters))
	if(tot_letts != 0):
		prob = len(letters)/tot_letts
	temp = []
	temp.append(prob)
	temp.append(tot_letts)
	temp.append(1)
	f5.writerow(temp)
	input_file.close()
	ctr=ctr+1

csvfile.close()
