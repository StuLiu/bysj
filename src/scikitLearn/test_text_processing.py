
## 获取训练文本
from sklearn.datasets import fetch_20newsgroups
import numpy as np
categories = ['alt.atheism', 'soc.religion.christian','comp.graphics', 'sci.med']
twenty_train = fetch_20newsgroups(subset='train',categories=categories,
                                  shuffle=True, random_state=42)
print(type(twenty_train),type(twenty_train.data))
print(len(twenty_train.data),len(twenty_train.target))
print(type(twenty_train.data))
print(twenty_train.target,twenty_train.target.shape)
print(twenty_train.target_names)



## 文本预处理——特征提取
from sklearn.feature_extraction.text import CountVectorizer,TfidfTransformer
# 基于词语频数(count)的词袋模型
count_vect = CountVectorizer()
X_train_counts = count_vect.fit_transform(twenty_train.data)
print(X_train_counts.shape)
# 基于词频(tf)的词袋模型
tf_transformer = TfidfTransformer(use_idf=False).fit(X_train_counts)
X_train_tf = tf_transformer.transform(X_train_counts)
print(X_train_tf.shape)
# 基于tf-idf的词袋模型
tfidf_transformer = TfidfTransformer()
X_train_tfidf = tfidf_transformer.fit_transform(X_train_counts)
print(X_train_tfidf.shape)



## 训练预评估
from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import classification_report
clf = MultinomialNB()
clf.fit(X_train_tfidf[:-200], twenty_train.target[:-200])
print(classification_report(twenty_train.target[-200:], clf.predict(X_train_tfidf[-200:])))