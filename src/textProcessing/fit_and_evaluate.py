from sklearn.metrics import classification_report
from sklearn.cross_validation import cross_val_score
import numpy as np
def fit_evalueate(classifiers, X, y):
    """
    :param classifiers:字典类型{"classifier name':classifier object,...}
    :param data:
    :todo:用不同的机器学习分类器对传入的data训练数据进行训练，然后用data测试数据进行评估
    :return: None
    """
    dataLen = len(y)
    for key in classifiers.keys():
        print('classifier:', key)
        classifiers[key].fit(X[:int(0.9*dataLen)], y[:int(0.9*dataLen)])
        print(classification_report(y[int(0.9*dataLen):], classifiers[key].predict(X[int(0.9*dataLen):])))
        cross_val_score_list = cross_val_score(classifiers[key], X, y, n_jobs=1, cv=5)
        print('cross_val_score:',cross_val_score_list)
        print("平均得分:",np.mean(cross_val_score_list))
        print('-'*80,end='\n')