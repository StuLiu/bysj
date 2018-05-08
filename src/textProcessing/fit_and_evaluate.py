from sklearn.metrics import classification_report
from sklearn.cross_validation import cross_val_score
import numpy as np
def fit_evalueate(classifier, X, y):
    """
    :param classifier:classifier object
    :param X:特征向量集合（ndarray）
    :param y:X特征向量对应的所属类型集合（ndarray）
    :todo:用机器学习分类器classifier进行训练，打印评分
    :return: 交叉验证得分均值
    """
    # 训练样本和测试样本的总数据量
    dataLen = len(y)
    print("样本量:",dataLen)
    try:
        classifier.fit(X[:int(0.8*dataLen)], y[:int(0.8*dataLen)])
    except Warning as e:
        print(e)
    print(classification_report(y[int(0.8*dataLen):], classifier.predict(X[int(0.8*dataLen):])))

    cross_val_score_list = cross_val_score(classifier, X, y, n_jobs=1, cv=3)
    print('cross_val_score:',cross_val_score_list)
    print("平均得分:",np.mean(cross_val_score_list))
    print('-'*80,end='\n')

    return np.mean(cross_val_score_list)