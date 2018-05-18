import numpy as np
import csv
from sklearn import svm
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import OneHotEncoder
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score
from sklearn.discriminant_analysis import LinearDiscriminantAnalysis
from sklearn.discriminant_analysis import QuadraticDiscriminantAnalysis
import random
from sklearn.metrics import precision_recall_fscore_support

x = []
y = []

with open('f1tof6.csv') as csvfile:
	reader = csv.reader(csvfile, delimiter = ' ')
	for row in reader:
		x.append(row[0: (len(row))])

for i in x:
	i[0] = i[0].split(',')
	y.append(i[0][-1])
	del i[0][-1]

X = []
for i in x:
	X.append(i[0])
Y = []
for i in y:
	Y.append(i)

'''for j in range(72, 78):
	temp0 = []
	for i in X:
		temp0.append(i[j])
	temp0 = list(set(temp0))
	temp0.sort()
#	print(temp0)

	tempdict0 = {}
	for i in range(0, len(temp0)):
		tempdict0[temp0[i]] = i
#	print(tempdict0)

	for i in X:
		i[j] = tempdict0[i[j]]
'''
#print(str(X[0]) + "\n")
#print(str(X[0])  + "     " + str(Y[4000]) + "\n")

X = np.asarray(X)
Y = np.asarray(Y)

for i in X:
	for j in i:
		j = float(j)

for i in Y:
	for j in i:
		j = float(j)

np.array(X).astype(np.float)
np.array(Y).astype(np.float)

x_train, x_test, y_train, y_test = train_test_split(X, Y, test_size = 0.1, random_state = 42)


neigh = KNeighborsClassifier(algorithm='auto', leaf_size=30, metric='minkowski', metric_params=None, n_jobs=1, n_neighbors=3, p=2,weights='uniform')
neigh.fit(x_train, y_train )
y_pred = neigh.predict(x_test)
print("KNeighbours Classifier's  : "+str(neigh.score(x_test, y_test)))
'''
precision, recall, f1_score, _ = precision_recall_fscore_support(y_test ,y_pred, average='binary')
print("Accuracy : "+str(accuracy_score(y_test,y_pred)))
print ("Precision score : " + precision)
print ("Recall score : " + recall)

'''

#*********************************************************************************


lda = LinearDiscriminantAnalysis(solver="svd", store_covariance=True)
y_pred = lda.fit(x_train, y_train).predict(x_test)
print("LDA Classifier's  : "+str(lda.score(x_test, y_test)))
'''
precision, recall, f1_score, _ = precision_recall_fscore_support(y_test ,y_pred, average='binary')
print("Accuracy : "+str(accuracy_score(y_test,y_pred)))
print ("Precision score : " + precision)
print ("Recall score : " + recall)
'''


#**********************************************************************************

qda = QuadraticDiscriminantAnalysis(store_covariance=True)
y_pred = qda.fit(x_train, y_train).predict(x_test)
print("QDA Classifier's  : "+str(qda.score(x_test, y_test)))
'''
precision, recall, f1_score, _ = precision_recall_fscore_support(y_test ,y_pred, average='binary')
print("Accuracy : "+str(accuracy_score(y_test,y_pred)))
print ("Precision score : " + precision)
print ("Recall score : " + recall)
'''

