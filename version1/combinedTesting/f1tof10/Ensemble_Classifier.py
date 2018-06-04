import numpy as np
import csv
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import OneHotEncoder
from sklearn.ensemble import RandomForestClassifier, AdaBoostClassifier, BaggingClassifier, ExtraTreesClassifier, GradientBoostingClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import cross_val_score

x = []
y = []

with open('f1tof10.csv') as csvfile:
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

#print(str(X[0]) + "\n")
#print(str(X[0])  + "     " + str(Y[4000]) + "\n")

X = np.asarray(X)
Y = np.asarray(Y)

#Random Forest Classifier
x_train, x_test, y_train, y_test = train_test_split(X, Y, test_size = 0.1, random_state = 42)

clf = RandomForestClassifier()
clf.fit(x_train, y_train)

print("Random Forest classifier")
print(clf.score(x_test, y_test))
print("\n")
scores = cross_val_score(clf, X, Y, cv=10)
print (scores)
print("Accuracy: %0.2f (+/- %0.2f)" % (scores.mean(), scores.std() * 2))

#Adaboost Classifier
x_train, x_test, y_train, y_test = train_test_split(X, Y, test_size = 0.1, random_state = 42)

clf = AdaBoostClassifier()
clf.fit(x_train, y_train)

print("AdaBoost classifier")
print(clf.score(x_test, y_test))
print("\n")

scores = cross_val_score(clf, X, Y, cv=10)
print (scores)
print("Accuracy: %0.2f (+/- %0.2f)" % (scores.mean(), scores.std() * 2))


#BaggingClassifier

x_train, x_test, y_train, y_test = train_test_split(X, Y, test_size = 0.1, random_state = 42)

clf = BaggingClassifier()
clf.fit(x_train, y_train)

print("Bagging classifier")
print(clf.score(x_test, y_test))
print("\n")



scores = cross_val_score(clf, X, Y, cv=10)
print (scores)
print("Accuracy: %0.2f (+/- %0.2f)" % (scores.mean(), scores.std() * 2))

#ExtraTreesClassifier

x_train, x_test, y_train, y_test = train_test_split(X, Y, test_size = 0.1, random_state = 42)

clf = ExtraTreesClassifier()
clf.fit(x_train, y_train)

print("ExtraTrees classifier")
print(clf.score(x_test, y_test))
print("\n")


scores = cross_val_score(clf, X, Y, cv=10)
print (scores)
print("Accuracy: %0.2f (+/- %0.2f)" % (scores.mean(), scores.std() * 2))


#GradientBoostingClassifier

x_train, x_test, y_train, y_test = train_test_split(X, Y, test_size = 0.1, random_state = 42)

clf = GradientBoostingClassifier()
clf.fit(x_train, y_train)

print("GradientBoostingClassifier")
print(clf.score(x_test, y_test))
print("\n")


scores = cross_val_score(clf, X, Y, cv=10)
print (scores)
print("Accuracy: %0.2f (+/- %0.2f)" % (scores.mean(), scores.std() * 2))

'''
#Just Something

x_train, x_test, y_train, y_test = train_test_split(X, Y, test_size = 0.1, random_state = 42)

bagging = BaggingClassifier(KNeighborsClassifier(), max_samples=0.5, max_features=0.5)
bagging.fit(x_train, y_train)

print("Just trying something")
print(bagging.score(x_test, y_test))
print("\n")

#KneighboursClassifier

x_train, x_test, y_train, y_test = train_test_split(X, Y, test_size = 0.1, random_state = 42)

clf = KNeighborsClassifier()
clf.fit(x_train, y_train)

print("KNeighborsClassifier")
print(clf.score(x_test, y_test))
print("\n")
'''