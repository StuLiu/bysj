
from sklearn.linear_model import LogisticRegression
from sklearn.neighbors import KNeighborsClassifier
from sklearn.neural_network import MLPClassifier
from sklearn.naive_bayes import MultinomialNB
from sklearn.svm import SVC

def get_classifiers():
    """
    :todo:定义分类器对象
    :return: {"classifier name':classifier object,...}
    """
    return {
        'NB' : MultinomialNB(),
        'MLP': MLPClassifier(activation='relu', alpha=0.0001, batch_size='auto', beta_1=0.9,
                             beta_2=0.999, early_stopping=False, epsilon=1e-08,
                             hidden_layer_sizes=(10, 10, 10), learning_rate='constant',
                             learning_rate_init=0.001, max_iter=50000, momentum=0.9,
                             nesterovs_momentum=True, power_t=0.5, random_state=None,
                             shuffle=True, solver='adam', tol=0.0001, validation_fraction=0.1,
                             verbose=False, warm_start=False),
        'KNN': KNeighborsClassifier(algorithm='auto', leaf_size=30, metric='minkowski',
                                    metric_params=None, n_jobs=1, n_neighbors=5, p=2,
                                    weights='uniform'),
        'LR': LogisticRegression(C=1.0, class_weight=None, dual=False, fit_intercept=True,
                                 intercept_scaling=1, max_iter=100, multi_class='ovr', n_jobs=1,
                                 penalty='l2', random_state=None, solver='liblinear', tol=0.0001,
                                 verbose=0, warm_start=False),
        'SVC': SVC(C=100.0, cache_size=200, class_weight=None, coef0=0.0,
                   decision_function_shape='ovr', degree=3, gamma=0.001, kernel='rbf',
                   max_iter=-1, probability=False, random_state=None, shrinking=True,
                   tol=0.001, verbose=False),
    }