


from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfVectorizer

countVectorizer = CountVectorizer(min_df=1)
tfidfVectorizer = TfidfVectorizer()

contents = [
    'This is the first document.',
    'This is the second second document.',
    'And the third one.',
    'Is this the first document?',
]

# 特征提取
count_features = countVectorizer.fit_transform(contents).toarray()
tfidf_features = tfidfVectorizer.fit_transform(contents).toarray()
print(count_features)
print(tfidf_features)



