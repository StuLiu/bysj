

from sklearn.tree import DecisionTreeRegressor
from sklearn.ensemble import RandomForestRegressor, ExtraTreesRegressor, \
    GradientBoostingRegressor
from sklearn.cross_decomposition import PLSRegression
from sklearn.linear_model import LinearRegression,LogisticRegression,\
    ElasticNet, BayesianRidge, PassiveAggressiveRegressor, HuberRegressor, \
    TheilSenRegressor, RANSACRegressor
from sklearn.kernel_ridge import KernelRidge
from sklearn.neighbors import KNeighborsClassifier,KNeighborsRegressor
from sklearn.neural_network import MLPClassifier
from sklearn.naive_bayes import MultinomialNB
from sklearn.svm import SVC, SVR

def get_classifiers():
    """
    :todo:定义分类器对象
    :return: {"classifier name':classifier object,...}
    """
    return {
        'Decision tree' : DecisionTreeRegressor(criterion='mse', splitter='best',
            max_depth=None, min_samples_split=2, min_samples_leaf=1,
            min_weight_fraction_leaf=0.0, max_features=None, random_state=None,
            max_leaf_nodes=None, min_impurity_decrease=0.0,
            min_impurity_split=None, presort=False),
        'Ramdom forest' : RandomForestRegressor(n_estimators=10, criterion='mse',
            max_depth=None, min_samples_split=2, min_samples_leaf=1,
            min_weight_fraction_leaf=0.0, max_features='auto', max_leaf_nodes=None,
            min_impurity_decrease=0.0, min_impurity_split=None, bootstrap=True,
            oob_score=False, n_jobs=1, random_state=49, verbose=0, warm_start=False),
        'ExtraTreesRegressor' : ExtraTreesRegressor(n_estimators=34, criterion='mse',
            max_depth=None, min_samples_split=3, min_samples_leaf=1,
            min_weight_fraction_leaf=0.0, max_features='auto', max_leaf_nodes=None,
            min_impurity_decrease=0.0, min_impurity_split=None, bootstrap=False,
            oob_score=False, n_jobs=1, random_state=1427, verbose=0, warm_start=False),
        'PLSRegression' : PLSRegression(n_components=2, scale=True, max_iter=500,
            tol=1e-06, copy=True),
        'KNeighborsRegressor(weights=uniform, n_neighbors=16)' : KNeighborsRegressor(
            algorithm='auto', leaf_size=30, metric='minkowski',
            metric_params=None, n_jobs=1, n_neighbors=16, p=2, weights='uniform'),
        'KNeighborsRegressor(weights=distance, n_neighbors=16)' : KNeighborsRegressor(
            algorithm='auto', leaf_size=30, metric='minkowski',
            metric_params=None, n_jobs=1, n_neighbors=16, p=2, weights='distance'),
        'GradientBoostingRegressor' : GradientBoostingRegressor(),
        'LinearRegression' : LinearRegression(),
        'ElasticNet' : ElasticNet(),
        'BayesianRidge' : BayesianRidge(n_iter=300, tol=0.001, alpha_1=1e-06,
            alpha_2=1e-06, lambda_1=1e-06, lambda_2=1e-06, compute_score=False,
            fit_intercept=True, normalize=False, copy_X=True, verbose=False),
        # 'KernelRidge' : KernelRidge(alpha=1, kernel='linear', gamma=None, degree=3, coef0=1, kernel_params=None),
        'PassiveAggressiveRegressor' : PassiveAggressiveRegressor(),
        'HuberRegressor' : HuberRegressor(),
        'TheilSenRegressor' : TheilSenRegressor(),
        'MLP': MLPClassifier(activation='relu', alpha=0.0001, batch_size='auto', beta_1=0.9,
            beta_2=0.999, early_stopping=False, epsilon=1e-08,
            hidden_layer_sizes=(10, 10, 10), learning_rate='constant',
            learning_rate_init=0.001, max_iter=50000, momentum=0.9,
            nesterovs_momentum=True, power_t=0.5, random_state=None,
            shuffle=True, solver='adam', tol=0.0001, validation_fraction=0.1,
            verbose=False, warm_start=False),
        'SVR(kernel=linear)' : SVR(kernel='linear'),
        'SVR(kernel=rbf)' : SVR(kernel='rbf'),
        'SVC': SVC(C=100.0, cache_size=200, class_weight=None, coef0=0.0,
            decision_function_shape='ovr', degree=3, gamma=0.001, kernel='rbf',
            max_iter=-1, probability=False, random_state=None, shrinking=True,
            tol=0.001, verbose=False),
        'LR': LogisticRegression(C=1.0, class_weight=None, dual=False, fit_intercept=True,
            intercept_scaling=1, max_iter=100, multi_class='ovr', n_jobs=1,
            penalty='l2', random_state=None, solver='liblinear', tol=0.0001,
            verbose=0, warm_start=False),
        'MultinomialNB':MultinomialNB()
    }