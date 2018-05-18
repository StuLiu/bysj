
from textProcessing import classifier, fit_and_evaluate, load_data, vectorizer
import matplotlib.pyplot as plt
import time
if __name__ == "__main__":

    classifierDict = classifier.get_classifiers()

    print("run userdefined vectorizing")
    ml_data = load_data.load_vectorized_data()
    X_data = ml_data.X
    y_data = ml_data.y

    for key in classifierDict.keys():
        fr = time.time()
        print('classifier:', key)
        print(fit_and_evaluate.fit_evalueate(classifierDict[key], X_data, y_data))
        to = time.time()
        print('using time:{}s'.format(to - fr))
        print(80 * '-')

    # print("run with user-defined bag-of-word model")
    # data = load_data.load_vectorized_data_forRNN()
    # X_data = data.X
    # y_data = data.y

    # print("run with scikit-learn countVectorizer and tf-idf transformer")
    # usefulData = load_data.load_useful_data()
    # X_data = vectorizer.tf_idf_vectoring(usefulData.content_array)
    # y_data = usefulData.isSpam_array
    # for key in classifierDict.keys():
    #     fr = time.time()
    #     print('classifier:', key)
    #     fit_and_evaluate.fit_evalueate_tf_idf(classifierDict[key], X_data, y_data)
    #     to = time.time()
    #     print('using time:{}s'.format(to - fr))
    #     print(80 * '-')


