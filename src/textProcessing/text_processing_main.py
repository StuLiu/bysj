
from textProcessing import classifier, fit_and_evaluate, load_data, vectorizer

if __name__ == "__main__":

    classifierDict = classifier.get_classifiers()
    X, y= None, None
    inputed = input("type '1' to run default vectorizing,\n'2' to run userdefined vectorizing:")
    if(inputed == '1'):
        print("run default vectorizing")
        usefulData = load_data.load_useful_data()
        X = vectorizer.tf_idf_vectoring(usefulData.content_array)
        y = usefulData.isSpam_array
    else:
        print("run userdefined vectorizing")
        ml_data = load_data.load_vectorized_data()
        X = ml_data.X
        y = ml_data.y

    fit_and_evaluate.fit_evalueate(classifierDict, X, y)