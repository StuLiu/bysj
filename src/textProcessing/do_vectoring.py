"""
============================================
    将标注好的评论文本向量化，并存入数据库
 1. 从signedcomments表中查询标注好的评论
 2. 向量化评论
 3. 将向量化的评论插入vectorizedcomments表中
============================================
"""
print(__doc__)

import time

from database.signed_comments_dbHandler import SignedCommentsDbHandler
from database.vectorized_comments_dbHandler import VectorizedCommentsDbHandler
from textProcessing.vectorizer import Vectorizer

if __name__ == "__main__":
    fr = time.time()
    # 已标注评论数据库表的操作对象
    signedCommentsHandler = SignedCommentsDbHandler()
    # 向量化评论数据库表的操作对象
    vectorizedCommentsDbHandler = VectorizedCommentsDbHandler()
    # 用于向量化的类
    vectorizer = Vectorizer()
    # 标注好的评论元组
    signedComments = signedCommentsHandler.queryAll()
    for signedComment in signedComments:
        vectorizedComment = vectorizer.vectoring(signedComment[1],
                                                 signedComment[2],
                                                 signedComment[3],
                                                 signedComment[6])
        print(signedComment,'\n',vectorizedComment)
        vectorizedCommentsDbHandler.insertVectorizedComment(vectorizedComment)
    to = time.time()
    print("用时:%f"%(to-fr))