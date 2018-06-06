

import matplotlib.pyplot as plt
import math
def F1socreCompare():
    x = [0]*11
    for i in range(0,11):
        x[i] = i-0.2
    y1 = [0.7238,0.7742,0.7852,0.7119,0.5000,0.6953,0.6643,0.7756,0.7806,0.6622,0.7784]
    plt.bar(x, y1, 0.4, color="#666666", label='vector space model')

    for i in range(0,11):
        x[i] = i+0.2
    y2 = [0.5698,0.8500,0.8312,0.8680,0.7718,0.7558,0.8741,0.8807,0.8783,0.8911,0.8853]
    plt.bar(x, y2, 0.4, color="#009ACD", label='user defined model')
    plt.legend(loc='upper right')
    x_name = ['NB','DT','MLP','KNN','SVM','LR','AB','Bagging','ET','GB','RF']
    plt.xticks(range(0,11), x_name)
    plt.ylabel("F1-score")
    plt.xlabel("machine learning model")
    plt.title("F1-score from two deffrent model")

    plt.axis([-1, 11, 0, 1.1])
    plt.show()

def runTimeCompare():
    x = [0]*11
    y1 = [0.31,517.40,11407.73,20.93,375.94,1.95,454.49,3033.82,417.76,948.41,244.03,]
    y2 = [0.25,5.27,20.56,9.39,594.4,7.62,34.5,27.61,2.77,41.85,2.8]
    for i in range(0,11):
        x[i] = i-0.2
        y1[i] = math.log(y1[i]+2, 2)
        y2[i] = math.log(y2[i]+2, 2)
    plt.bar(x, y1, 0.4, color="#666666", label='vector space model')
    for i in range(0,11):
        x[i] = i + 0.2
    plt.bar(x, y2, 0.4, color="#009ACD", label='user defined model')
    plt.legend(loc='upper right')
    x_name = ['NB','DT','MLP','KNN','SVM','LR','AB','Bagging','ET','GB','RF']
    plt.xticks(range(0,11), x_name)
    plt.ylabel("log(runtime+2)")
    plt.xlabel("machine learning model")
    plt.title("runtime from two deffrent model")

    # plt.axis([-1, 15, 0, 1])
    plt.show()

def classifierCompare():
    x = [0,1,2,3]
    x_name = ['acc', 'p', 'r', 'F1-score']
    plt.xticks(range(0, 11), x_name)

    ys=[ [0.6945,	0.9625,	0.4047,	0.5698],
[0.8500,	0.8501,	0.8499,	0.8500],
[0.8378,	0.8656,	0.8004,	0.8312],
[0.7799,	0.8123,	0.7284,	0.7680],
[0.7992,	0.8937,	0.6793,	0.7718],
[0.7834,	0.8594,	0.6770,	0.7558],
[0.8757,	0.8851,	0.8634,	0.8741],
[0.8839,	0.9055,	0.8573,	0.8807],
[0.8827,	0.9122,	0.8469,	0.8783],
[0.8924,	0.9017,	0.8808,	0.8911],
[0.8889,	0.9153,	0.8572,	0.8853]
    ]
    colors = ['#FF34B3', '#E0E0E0', '#F5DEB3', '#76EE00', '#436EEE', '#00EEEE', '#CD00CD',
              '#EEEE00', '#000000', '#FF8C69', '#FF0000']
    lables = ['NB','DT','MLP','KNN','SVM','LR','AB','Bagging','ET','GB','RF']
    for i in range(0,11):
        plt.plot(x, ys[i], color=colors[i], label=lables[i])
    plt.legend(loc='upper right')
    plt.ylabel("value")
    plt.title("acc,p,r,f1-score from defferent classifier")

    plt.axis([-0.2, 4.2, 0.4, 1])
    plt.show()


if __name__ == '__main__':
    # F1socreCompare()
    # runTimeCompare()
    classifierCompare()