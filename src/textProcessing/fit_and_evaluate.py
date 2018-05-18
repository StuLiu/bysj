# from sklearn.metrics import classification_report
# from sklearn.cross_validation import cross_val_score
# import numpy as np


import copy
import numpy as np

def fit_evalueate_tf_idf(classifier, X, y):
    # 训练样本和测试样本的总数据量
    dataLen = len(y)
    print("examples count:", dataLen)

    # 训练计算过程
    try:
        X_train = X[:int(0.8 * len(y))]
        y_train = y[:int(0.8 * len(y))]
        X_test = X[int(0.8 * len(y)):]
        y_test = y[int(0.8 * len(y)):]
        classifierTemp = copy.deepcopy(classifier)
        classifierTemp.fit(X_train, y_train)
        predict_result = classifierTemp.predict(X_test)
        for i in range(0, int(len(predict_result))):
            predict_result[i] = predict_result[i] > 0.5 and 1 or 0
        target = y_test
        accuracy_count, TP_count, FP_count, FN_count = 0., 0., 0., 0.
        for i in range(0, int(len(predict_result))):
            if predict_result[i] == target[i]:
                accuracy_count += 1
            if predict_result[i] == 1 and target[i] == 1:
                TP_count += 1
            if predict_result[i] == 0 and target[i] == 1:
                FN_count += 1
            if predict_result[i] == 1 and target[i] == 0:
                FP_count += 1
        accuracy = accuracy_count / len(target)
        precision = (TP_count + FP_count) != 0 and TP_count / (TP_count + FP_count) or 1
        recall = (TP_count + FN_count) != 0 and TP_count / (TP_count + FN_count) or 1
        F1 = (2 * precision * recall) / (precision + recall)
        print("accuracy:", accuracy)
        print('precision:', precision)
        print('recall:', recall)
        print('F1 score:', F1)

    except Exception as e:
        print(e)




def fit_evalueate(classifier, X, y):
    """
    :param classifier:classifier object
    :param X:特征向量集合（ndarray）
    :param y:X特征向量对应的所属类型集合（ndarray）
    :todo:用机器学习分类器classifier进行5折交叉验证
    :return: [accuracy, precision, recall, F1]
    """
    # 训练样本和测试样本的总数据量
    dataLen = len(y)
    print("examples count:",dataLen)

    # 5折交叉验证
    cutLen = int(dataLen/5)
    X_train = [ X[:4*cutLen],
                X[cutLen:],
                np.concatenate((X[:cutLen], X[2*cutLen:])),
                np.concatenate((X[:2*cutLen], X[3*cutLen:])),
                np.concatenate((X[:3*cutLen], X[4*cutLen:]))
            ]
    y_train = [ y[:4*cutLen],
                y[cutLen:],
                np.concatenate((y[:cutLen], y[2 * cutLen:])),
                np.concatenate((y[:2 * cutLen], y[3 * cutLen:])),
                np.concatenate((y[:3 * cutLen], y[4 * cutLen:]))
            ]
    X_test = [ X[4*cutLen:], X[:cutLen], X[cutLen:2*cutLen], X[2*cutLen:3*cutLen], X[3*cutLen:4*cutLen] ]
    y_test = [ y[4*cutLen:], y[:cutLen], y[cutLen:2*cutLen], y[2*cutLen:3*cutLen], y[3*cutLen:4*cutLen] ]

    # 存储结果列表
    accuracyList,precisionList,recallList,F1List = [],[],[],[]

    # 训练计算过程
    try:
        for j in range(0,len(X_train)):
            classifierTemp = copy.deepcopy(classifier)
            classifierTemp.fit(X_train[j], y_train[j])
            predict_result = classifierTemp.predict(X_test[j])
            for i in range(0,int(len(predict_result))):
                predict_result[i] = predict_result[i] > 0.5 and 1 or 0
            target = y_test[j]
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
            F1= (2 * precision * recall) /  (precision + recall)
            accuracyList.append(accuracy)
            precisionList.append(precision)
            recallList.append(recall)
            F1List.append(F1)
    except Exception as e:
        print(e)

    print("accuracy:", accuracyList)
    print('precision:', precisionList)
    print('recall:', recallList)
    print('F1 score:', F1List)

    return [sum(accuracyList)/len(accuracyList), sum(precisionList)/len(precisionList),
            sum(recallList) / len(recallList), sum(F1List)/len(F1List)]