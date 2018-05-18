
import numpy as np
import matplotlib.pyplot as plt
import tensorflow as tf
from textProcessing.load_data import load_vectorized_data_forRNN

sess = tf.Session()
epochs = 20         # 20批
batch_size = 200    # 批量大小
max_sequence_len = 25   # 最多词语数量
rnn_size = 10
embedding_size = 25
learning_rate = 0.0005
dropout_keep_prob = tf.placeholder(tf.float32)

data = load_vectorized_data_forRNN()
print(data.X,data.y)

# 随机shuffle文本数据
text_processed = data.X
text_data_target = data.y
shuffled_ix = np.random.permutation(np.arange(len(text_data_target)))
x_shuffled = text_processed[shuffled_ix]
y_shuffled = text_data_target[shuffled_ix]

# 分割数据集
ix_cutoff = int(len(y_shuffled)*0.8)
x_train, x_test = x_shuffled[:ix_cutoff], x_shuffled[ix_cutoff:]
y_train, y_test = y_shuffled[:ix_cutoff], y_shuffled[ix_cutoff:]

# 声明计算图
x_data = tf.placeholder(tf.int32, [None, max_sequence_len])
y_output = tf.placeholder(tf.int32, [None])

embedding_mat = tf.Variable(tf.random_uniform([data.vocabularyLen, embedding_size],-1.0,1.0))
embedding_output = tf.nn.embedding_lookup(embedding_mat, x_data)

cell = tf.nn.rnn_cell.BasicRNNCell(num_units=rnn_size)
output, state = tf.nn.dynamic_rnn(cell, embedding_output, dtype=tf.float32)
output = tf.nn.dropout(output, dropout_keep_prob)

output = tf.transpose(output,[1,0,2])
last = tf.gather(output, int(output.get_shape()[0]) - 1)

weight = tf.Variable(tf.truncated_normal([rnn_size, 2],stddev=0.1))
bias = tf.Variable(tf.constant(0.1, shape=[2]))
logits_out = tf.nn.softmax(tf.matmul(last, weight)+bias)

losses = tf.nn.sparse_softmax_cross_entropy_with_logits(logits=logits_out, labels=y_output)
loss = tf.reduce_mean(losses)

accuracy = tf.reduce_mean(
    tf.cast(
        tf.equal(tf.argmax(logits_out,1),
        tf.cast(y_output, tf.int64)),
        tf.float32
    )
)

optimizer = tf.train.RMSPropOptimizer(learning_rate)
train_step = optimizer.minimize(loss)
sess.run(tf.initialize_all_variables())

train_loss =[]
test_loss = []
train_accuracy = []
test_accuracy = []
# start train
for epoch in range(epochs):
    # shuffle train data
    shuffled_ix = np.random.permutation(np.arange(len(x_train)))
    x_tarin = x_train[shuffled_ix]
    y_train = y_train[shuffled_ix]
    num_batches = int(len(x_train)/batch_size)+1
    for i in range(num_batches):
        # select train data
        min_ix = i *batch_size
        max_ix = np.min([len(x_train), ((i+1)*batch_size)])
        x_train_batch = x_train[min_ix:max_ix]
        y_train_batch = y_train[min_ix:max_ix]
        # run train step
        train_dict_temp={x_data:x_train_batch,y_output:y_train_batch, dropout_keep_prob:0.5}
        sess.run(train_step, feed_dict=train_dict_temp)

    # run lose and accuracy for training
    train_dict = {x_data:x_train,y_output:y_train, dropout_keep_prob:0.5}
    temp_tarin_loss, temp_train_acc = sess.run([loss, accuracy], feed_dict=train_dict)
    train_loss.append(temp_tarin_loss)
    train_accuracy.append(temp_train_acc)

    test_dict = {x_data:x_test, y_output:y_test, dropout_keep_prob:1.0}
    temp_test_loss, temp_test_acc = sess.run([loss,accuracy],feed_dict=test_dict)
    test_loss.append(temp_test_loss)
    test_accuracy.append(temp_test_acc)
    print('Epoch:{}, test loss:{:.2}, test acc:{:.2}'
          .format(epoch+1, temp_test_loss,temp_test_acc))

epoach_seq = np.arange(1, epochs+1)
plt.figure(1) # 创建第一个画板（figure）
plt.plot(epoach_seq, train_loss, 'k--', label='Train Set')
plt.plot(epoach_seq, test_loss, 'r-', label='Test Set')
plt.title("Softmax Loss")
plt.xlabel("Epochs")
plt.ylabel('softmax loss')
plt.legend(loc='upper left')

plt.figure(2) #创建第二个画板
plt.plot(epoach_seq, train_accuracy, 'k--', label='train set')
plt.plot(epoach_seq, test_accuracy, 'r-', label='test set')
plt.title('Test Accuracy')
plt.xlabel('epochs')
plt.ylabel('accuracy')
plt.legend(loc='upper left')
plt.show()