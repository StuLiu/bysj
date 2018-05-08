
from textProcessing import classifier, fit_and_evaluate, load_data, vectorizer
import matplotlib.pyplot as plt

if __name__ == "__main__":

    classifierDict = classifier.get_classifiers()
    print("run default vectorizing")
    usefulData = load_data.load_useful_data()
    X = vectorizer.tf_idf_vectoring(usefulData.content_array)
    y = usefulData.isSpam_array
    print("run userdefined vectorizing")
    ml_data = load_data.load_vectorized_data()
    X_data = ml_data.X
    y_data = ml_data.y
    for key in classifierDict.keys():
        print('classifier:', key)
        fit_and_evaluate.fit_evalueate(classifierDict[key], X_data, y_data)
    # N = 50
    # totelNum = y_data.size
    #
    # plotxList = [0]
    # scoreDict = {}
    # for key in classifierDict.keys():
    #     scoreDict[key] = [0.5]
    # for index in range(1, N + 1):
    #     plotx = int(index / N * totelNum)
    #     plotxList.append(plotx)
    #     tempX = X_data[0 : plotx + 1]
    #     tempy = y_data[0 : plotx + 1]
    #     print(tempX.shape,tempy.shape)
    #     for key in classifierDict.keys():
    #         print('classifier:', key)
    #         score = fit_and_evaluate.fit_evalueate(classifierDict[key], tempX, tempy)
    #         scoreDict[key].append(score)
    #
    # for key in classifierDict.keys():
    #     plt.plot(plotxList, scoreDict[key], 'r', linewidth=2)
    # plt.axis([100, totelNum, 0.45, 1])
    # plt.xlabel(u"sample num")
    # plt.ylabel("avg score")
    # plt.show()