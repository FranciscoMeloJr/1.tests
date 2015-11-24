import numpy as np
from sklearn.ensemble import ExtraTreesClassifier

data_train = np.loadtxt('data_train.csv', delimiter=',')
X = data_train[:, 1:]
y = data_train[:, 0].astype(np.int)
clf = ExtraTreesClassifier(n_estimators=100).fit(X, y)
