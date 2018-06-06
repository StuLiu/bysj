
import tensorflow as tf
import numpy as np


""" 构建图 """
# 创建一个常量 op, 产生一个 1x2 矩阵. 这个 op 被作为一个节点
matrix1 = tf.constant([[3.,3.]])

# 创建另外一个常量 op, 产生一个 2x1 矩阵.
matrix2 = tf.constant([[2.],[1.]])

# 创建一个矩阵乘法 matmul op , 把 'matrix1' 和 'matrix2' 作为输入.
# 返回值 'product' 代表矩阵乘法的结果tensor.
product = tf.matmul(matrix1, matrix2) 

""" 会话中启动图 """
# 启动默认图.
with tf.Session() as sess:
    with tf.device("/gpu:0"):
    # 调用 sess 的 'run()' 方法来执行矩阵乘法 op, 传入 'product' 作为该方法的参数.
    # 上面提到, 'product' 代表了矩阵乘法 op 的输出, 传入它是向方法表明, 我们希望取回
    # 矩阵乘法 op 的输出.
    #
    # 整个执行过程是自动化的, 会话负责传递 op 所需的全部输入. op 通常是并发执行的.
    #
    # 函数调用 'run(product)' 触发了图中三个 op (两个常量 op 和一个矩阵乘法 op) 的执行.
    #
    # 返回值 'result' 是一个 numpy `ndarray` 对象.
        result = sess.run(product)
        print(result)

# 任务完成, 关闭会话.
# sess.close()


# x = np.array([[1, 2, 3], [4, 5, 6]], np.float32)
# print(x,type(x),x.shape,x.dtype,x.size)

# x = np.array([[1,2,3,4,5],[6,7,8,9,10]])
# w = np.array([[1,1,1],[1,1,1],[1,1,1],[1,1,1],[1,1,1]])
# print(np.matmul(x,w)+np.array([2,2,2]))

# if __name__ == "__main__":
#     # 使用 NumPy 生成假数据(phony data), 总共 100 个点.
#     x_data = np.float32(np.random.rand(2, 100))  # 随机输入
#     y_data = np.dot([0.100, 0.200], x_data) + 0.300
#     print(x_data.shape,y_data.shape)
#
#     # 构造一个线性模型
#     #
#     b = tf.Variable(tf.zeros([1]))
#     W = tf.Variable(tf.random_uniform([1, 2], -1.0, 1.0))
#     y = tf.matmul(W, x_data) + b
#
#     # 最小化方差
#     loss = tf.reduce_mean(tf.square(y - y_data))
#     optimizer = tf.train.GradientDescentOptimizer(0.5)
#     train = optimizer.minimize(loss)
#
#     # 初始化变量
#     init = tf.initialize_all_variables()
#
#     # 启动图 (graph)
#     sess = tf.Session()
#     sess.run(init)
#
#     # 拟合平面
#     for step in range(0, 201):
#         sess.run(train)
#         if step % 20 == 0:
#             print(step, sess.run(W), sess.run(b))
#
#             # 得到最佳拟合结果 W: [[0.100  0.200]], b: [0.300]