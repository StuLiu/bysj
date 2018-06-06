

import time

from database.signed_comments_dbHandler import SignedCommentsDbHandler
from database.vectorized_comments_dbHandler import VectorizedCommentsDbHandler
from database.vectorized_contents_dbHandler import VectorizedContentsDbHandler

import numpy as np

# 特征向量归一化
# arr:二维ndarray
def normalizing(arr):
    """
    在机器学习的算法训练中，有很多数据的特征值不止一个，特征值中有些属性的数字过大，
    从而对计算结果的影响太大，但是实际情况是每个属性都同等重要，
    这时候就要处理这种不同取值范围的特征值，
    通常采用数值归一化，将取值范围处理为0-1或者-1-1之间。
    """
    # print(arr.shape)
    # print(arr.max())
    result = []
    arrmax = np.max(arr,0)
    arrmin = np.min(arr,0)
    arrdeta = arrmax - arrmin
    # print(arrmax, arrmin, arrdeta)
    for i in range(0, arr.shape[0]):
        temp = [str(arr[i][0])]
        for j in range(1, arr.shape[1]):
            # arr[i][j] = (arr[i][j] - arrmin[j]) / arrdeta[j]
            if arrdeta[j] != 0:
                temp.append(float((arr[i][j] - arrmin[j]) / arrdeta[j]))
            else:
                temp.append(.0)
            # print(arr[i][j], end=' ')
        result.append(temp)
        # print("\n")
    return result

from textProcessing.vectorizer import Vectorizer
def doVectoringComments():
    """
    将标注好的评论文本向量化，并存入数据库
    1. 从signedcomments表中查询标注好的评论
    2. 向量化评论
    3. 向量归一化
    3. 将归一化的向量插入vectorizedcomments表中
    """
    fr = time.time()
    # 已标注评论数据库表的操作对象
    signedCommentsHandler = SignedCommentsDbHandler()
    # 向量化评论数据库表的操作对象
    vectorizedCommentsDbHandler = VectorizedCommentsDbHandler()
    # 标注好的评论元组
    signedComments = signedCommentsHandler.queryAll()
    vectorizer = Vectorizer()
    vectorizedCommentsList = []
    # 评论向量化
    count = 0
    for signedComment in signedComments:
        count += 1
        print(count)
        vectorizedComment = vectorizer.vectoringOneComment(
            signedComment[1], signedComment[2], signedComment[3],
            signedComment[6], signedComment[8], signedComment[9])
        vectorizedCommentsList.append(vectorizedComment)
        vectorizedCommentsDbHandler.insertVectorizedComment(vectorizedComment)
    # 归一化特征向量
    # arr = normalizing(np.array(vectorizedCommentsList, float))
    # for vc in arr:
    #     vectorizedCommentsDbHandler.insertVectorizedComment(vc)
    to = time.time()
    print("用时:%f" % (to - fr))

from textProcessing.vectorizer import vectoringContent
def doVectoringContent():
    signedCommentsDbHandler = SignedCommentsDbHandler()
    vectorizedContentsDbHandler = VectorizedContentsDbHandler()
    commentMatrix = np.array(signedCommentsDbHandler.queryAll())
    contentMatrix = commentMatrix[:,(1,3)]
    print(contentMatrix,contentMatrix.shape)
    result = vectoringContent(25, contentMatrix)
    for vectorizedContent in result:
        vectorizedContentsDbHandler.insertVectorizedContent(vectorizedContent)

if __name__ == "__main__":
    doVectoringComments()