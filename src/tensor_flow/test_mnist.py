"""
    tensorflow 入门教程：手写数字识别
    用梯度下降模型最小化交叉熵的方法训练参数w和b
"""

from tensorflow.examples.tutorials.mnist import input_data
import tensorflow as tf

# 加载数据集
# mnist是一个轻量级的类。它以Numpy数组的形式存储着训练、校验和测试数据集。
# 同时提供了一个函数，用于在迭代中获得minibatch，后面我们将会用到
mnist = input_data.read_data_sets("MNIST_data/",one_hot=True)

# 创建交互式session
sess = tf.InteractiveSession()

# x不是一个特定的值，而是一个占位符placeholder，我们在TensorFlow运行计算时输入这个值(字典类型输入)
# x表示图片特征值
# 这里的None表示此张量的第一个维度可以是任何长度的（任意数量的图片）
x = tf.placeholder(tf.float32,[None,784])   # 28*28像素

# 一个Variable代表一个可修改的张量，存在在TensorFlow的用于描述交互性操作的图中
# w每一项表示每一个特征值（像素点）会影响结果的权重
# 训练就是为了得到这个最佳权重值
# 因为有10类，所以每一类对应一个784维的向量
w = tf.Variable(tf.zeros([784,10]))

# 偏移量,输入往往会带有一些无关的干扰量
# 初始化为[ 0.  0.  0.  0.  0.  0.  0.  0.  0.  0.] , b.shape=(10,)
b = tf.Variable(tf.zeros([10]))

# 建立一个拥有一个线性层的softmax回归模型
# 这里的softmax可以看成是一个激励（activation）函数或者链接（link）函数
# softmax(xi)=exp(xi)/∑j(xj)
# 把我们定义的线性函数的输出转换成我们想要的格式，也就是关于10个数字类的概率分布
y = tf.nn.softmax(tf.matmul(x,w) + b)

# y_是图片实际对应的值
y_ = tf.placeholder(tf.float32,[None,10])

# 交叉熵用来衡量模型与真实概率分布之间的差异情况。交叉熵越小越接近真是分布
cross_entropy = tf.reduce_mean(-tf.reduce_sum(y_ * tf.log(y),reduction_indices=[1]))

# TensorFlow用梯度下降算法（gradient descent algorithm）以0.5的学习速率最小化交叉熵。
# 梯度下降算法（gradient descent algorithm）是一个简单的学习过程，
# TensorFlow只需将每个变量一点点地往使成本不断降低的方向移动
train_step = tf.train.GradientDescentOptimizer(0.5).minimize(cross_entropy)

# 初始化变量
tf.global_variables_initializer().run()

# 让模型循环训练1000次
for i in range(1000):
    # 该循环的每个步骤中，我们都会随机抓取训练数据中的100个批处理数据点，1次输入为100组
    # 然后我们用这些数据点作为参数替换之前的占位符来运行train_step
    batch_xs, batch_ys = mnist.train.next_batch(100)
    train_step.run({x: batch_xs, y_:batch_ys})

# tf.argmax给出某个tensor对象在某一维上的其数据最大值所在的索引值
# tf.argmax(y,1)返回的是模型对于任一输入x预测到的标签值
# tf.argmax(y_,1) 代表正确的标签
# 用 tf.equal 来检测我们的预测是否真实标签匹配(索引位置一样表示匹配)
correct_prediction = tf.equal(tf.argmax(y,1),tf.argmax(y_,1))

# tf.cast将correct_prediction(bool类型)数据格式转化成tf.float32类型
# tf.reduce_mean求匹配结果[0.,1.,0., ...]的平均值
accuracy = tf.reduce_mean(tf.cast(correct_prediction,tf.float32))

# tf.Tensor.eval():当默认的会话被指定之后可以通过其计算一个张量的取值。
print(accuracy.eval({x: mnist.test.images, y_: mnist.test.labels}))