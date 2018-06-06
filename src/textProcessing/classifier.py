
from sklearn.naive_bayes import MultinomialNB
from sklearn.tree import DecisionTreeClassifier
from sklearn.neural_network import MLPClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.svm import SVC
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import AdaBoostClassifier, BaggingClassifier, \
     ExtraTreesClassifier, GradientBoostingClassifier, RandomForestClassifier


def get_classifiers():
    """
    :todo:定义分类器对象
    :return: {"classifier name':classifier object,...}
    """
    return {
        'MultinomialNB': MultinomialNB(),
        'DecisionTreeClassifier': DecisionTreeClassifier(),
        'MLPClassifier': MLPClassifier(),
        'KNeighborsClassifier': KNeighborsClassifier(),
        'SVC': SVC(),
        'LogisticRegression': LogisticRegression(),
        'AdaBoostClassifier': AdaBoostClassifier(),
        'BaggingClassifier': BaggingClassifier(),
        'ExtraTreesClassifier':ExtraTreesClassifier(),
        'GradientBoostingClassifier':GradientBoostingClassifier(),
        'RandomForestClassifier':RandomForestClassifier()
    }