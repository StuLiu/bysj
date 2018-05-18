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
    print("examples count:",dataLen)
    try:
        classifier.fit(X[:int(0.8*dataLen)], y[:int(0.8*dataLen)])
        predict_result = classifier.predict(X[int(0.8*dataLen):])
        for i in range(0,int(len(predict_result))):
            predict_result[i] = predict_result[i] > 0.5 and 1 or 0
        target = y[int(0.8*dataLen):]
        accuracy_count,TP_count,FP_count,FN_count = 0., 0., 0., 0.
        for i in range(0,int(len(predict_result))):
            if predict_result[i] == target[i]:
                accuracy_count += 1
            if predict_result[i] == 1 and target[i] == 1:
                TP_count += 1
            if predict_result[i] == 0 and target[i] == 1:
                FN_count += 1
            if predict_result[i] == 1 and target[i] == 0:
                FP_count += 1
        accuracy = accuracy_count/len(target)
        precision = (TP_count+FP_count)!=0 and TP_count/(TP_count+FP_count) or 1
        recall = (TP_count+FN_count)!=0 and TP_count/(TP_count+FN_count) or 1
        F1 = (2 * precision * recall) /  (precision + recall)
        print("accuracy:",accuracy)
        print('precision:',precision)
        print('recall:',recall)
        print('F1 score:',F1)
    except Exception as e:
        print(e)
    # print(classification_report(y[int(0.8*dataLen):], classifier.predict(X[int(0.8*dataLen):])))

    # cross_val_score_list = cross_val_score(classifier, X, y, n_jobs=1, cv=3)
    # print('cross_val_score:',cross_val_score_list)
    # print("average score:",np.mean(cross_val_score_list))
    print('-'*80,end='\n')

    # return np.mean(cross_val_score_list)