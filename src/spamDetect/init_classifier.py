
from sklearn.externals import joblib
from sklearn.ensemble import GradientBoostingClassifier
from textProcessing.load_data import load_vectorized_data
import os

if __name__ == '__main__':
    os.chdir("model_save")
    dataset = load_vectorized_data()
    clf = GradientBoostingClassifier()
    clf.fit(dataset.X, dataset.y)
    joblib.dump(clf, "GBclf.m")
