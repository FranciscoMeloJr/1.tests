#import for random
import random as rd

# Import for svm:
from sklearn import svm
X = [[19, 0], [21, 0]] #an array X of size [n_samples, n_features] holding the training samples
y = ["OPT","NOPT"] # of class labels (strings or integers)
clf = svm.SVC()
clf.fit(X, y)

i = 15
j = 5
while(i<=25):
    #a = rd.uniform(-10, 10)
    print(i,j)
    print(clf.predict([[i, j]]))
    i+=0.1
    
