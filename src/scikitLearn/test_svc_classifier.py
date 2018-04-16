"""
================================
Digits Classification Exercise
================================

A tutorial exercise regarding the use of CSVM classification techniques on
the Digits dataset.

This exercise is used in the :ref:`clf_tut` part of the

"""
print(__doc__)

import numpy as np
from sklearn import datasets
from sklearn import svm
from sklearn.svm import SVC
# np.set_printoptions(threshold=10000)

iris = datasets.load_iris()
digits = datasets.load_digits()

# print(iris.data)
print(digits.data)
print(digits.target)
# print(digits.images)

clf = svm.SVC(gamma=0.001, C=100.)  # classifier
# clf.fit(digits.data[:-101],digits.target[:-101])
SVC(C=100.0, cache_size=200, class_weight=None, coef0=0.0,
  decision_function_shape='ovr', degree=3, gamma=0.001, kernel='sigmoid',
  max_iter=-1, probability=False, random_state=None, shrinking=True,
  tol=0.001, verbose=False)
print('svm score: %f' % clf.fit(digits.data[:-100],digits.target[:-100])
    .score(digits.data[-100:],digits.target[-100:]))

