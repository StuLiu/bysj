
from spamDetect.commentVectorizer import CommentVectorizer
from textProcessing.load_data import load_vectorized_data
from sklearn.ensemble import ExtraTreesClassifier, GradientBoostingClassifier
import numpy as np
import time,random
from database.signed_comments_dbHandler import SignedCommentsDbHandler


class SpamDetecter(object):
    """
    实时垃圾评论检测器
    """
    def __init__(self):
        fr = time.time()
        self.__vectorizer = CommentVectorizer()
        self.__classifier = GradientBoostingClassifier()
        dataset = load_vectorized_data()
        self.__classifier.fit(dataset.X, dataset.y)
        to = time.time()
        print('init SpamDetecter using {}s'.format(to-fr))

    def doDetection(self, comment_id, title, content, rating, user_name, app_id):
        featuresVector = self.__vectorizer.doVectoring(
            comment_id, title, content, rating, user_name, app_id
        )
        r = self.__classifier.predict(np.array(featuresVector, dtype=np.float32).reshape(1, -1))
        p = self.__classifier.predict_proba(np.array(featuresVector, dtype=np.float32).reshape(1, -1))
        # print(r,p)
        return r,p


if __name__ == '__main__':

    spamDetecter = SpamDetecter()
    dbHandler = SignedCommentsDbHandler()
    # spamDetecter.doDetection('1111', '我是标题', '很好用啊，就是有点小卡。', 5, '绿的可能', '333206289')
    spamComments = dbHandler.querySpam()
    notSpamComments = dbHandler.queryNotSpam()
    comments = list(spamComments[:100]+notSpamComments[:100])
    random.shuffle(comments)
    for comment in comments:
        print('*'*60,'\n1.评论标题:{}\n2.评论内容:{}\n3.评分等级:{}\n4.评论者昵称:{}\n5.是否是垃圾评论:{}'.format(
            comment[2], comment[3], comment[6], comment[8], comment[10]
        ))
        predict_class,predict_proba = spamDetecter.doDetection(
            comment[1], comment[2], comment[3], comment[6], comment[8], comment[9]
        )
        print('6.预测是否是垃圾评论:{}\n7.是垃圾评论的概率{}'.format(
            predict_class, predict_proba[0][1]
        ))