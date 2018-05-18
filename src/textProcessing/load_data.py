
import numpy as np
import random
import sys
from database.signed_comments_dbHandler import SignedCommentsDbHandler
from database.vectorized_comments_dbHandler import VectorizedCommentsDbHandler
from database.vectorized_contents_dbHandler import VectorizedContentsDbHandler

class UsefulData(object):
    content_array = np.array([])
    isSpam_array = np.array([])

def load_useful_data():

    signedCommentDbHandler = SignedCommentsDbHandler()

    spamCommentsList = list(signedCommentDbHandler.querySpam())
    notSpamCommentsList = list(signedCommentDbHandler.queryNotSpam())
    random.shuffle(spamCommentsList)
    random.shuffle(notSpamCommentsList)

    minLen = (len(spamCommentsList) <= len(notSpamCommentsList) and len(spamCommentsList)
              or len(notSpamCommentsList))
    usedDataList = spamCommentsList[:minLen] + notSpamCommentsList[:minLen]
    random.shuffle(usedDataList)

    contentList, isSpamList = [], []
    for usedData in usedDataList:
        contentList.append(usedData[3])
        isSpamList.append(usedData[10])
    result = UsefulData()
    result.content_array = np.array(contentList)
    result.isSpam_array = np.array(isSpamList)

    print(result.content_array.shape,result.isSpam_array.shape)
    print("load %d useful data."%(minLen*2))
    return result

MAX_INT = sys.maxsize
np.set_printoptions(threshold=1000)

class MLData(object):
    X = np.array([])
    y = np.array([])

def load_vectorized_data():
    ml_data = MLData()
    vcDbHandler = VectorizedCommentsDbHandler()
    notSpamData = list(vcDbHandler.queryNotSpam())
    spamData = list(vcDbHandler.querySpam())
    random.shuffle(notSpamData)
    random.shuffle(spamData)

    minLen = (len(notSpamData)<=len(spamData) and len(notSpamData) or len(spamData))
    vectorizedDataList = notSpamData[:minLen] + spamData[:minLen]
    random.shuffle(vectorizedDataList)

    X, y = [], []
    for vectorizedData in vectorizedDataList:
        # X.append(list(vectorizedData[1:12]))
        # X.append(list(vectorizedData[12:-1]))
        X.append(vectorizedData[1:-1])
        y.append(vectorizedData[-1])
    ml_data.X = np.array(X,np.float32)
    ml_data.y = np.array(y,np.int32)
    print(ml_data.X.shape,ml_data.y.shape)
    return ml_data

# def load_vectorized_data():
#     ml_data = MLData()
#     vcDbHandler = VectorizedCommentsDbHandler()
#     notSpamData = list(vcDbHandler.queryNotSpam(MAX_INT))
#     spamData = list(vcDbHandler.querySpam(MAX_INT))
#     random.shuffle(notSpamData)
#     random.shuffle(spamData)
#
#     minLen = (len(notSpamData)<=len(spamData) and len(notSpamData) or len(spamData))
#     vectorizedDataList = notSpamData[:minLen] + spamData[:minLen]
#     random.shuffle(vectorizedDataList)
#
#     X, y = [], []
#     for vectorizedData in vectorizedDataList:
#         X.append(vectorizedData[1:-1])
#         y.append(vectorizedData[-1])
#     ml_data.X = np.array(X)
#     ml_data.y = np.array(y)
#     print(ml_data.X.shape,ml_data.y.shape)
#     return ml_data


class DataForRNN(object):
    X = np.array([],np.int64)
    y = np.array([],np.int64)
    vocabularyLen = 0

def load_vectorized_data_forRNN():
    ml_data = DataForRNN()
    vcDbHandler = VectorizedContentsDbHandler()
    notSpamData = list(vcDbHandler.queryNotSpam(MAX_INT))
    spamData = list(vcDbHandler.querySpam(MAX_INT))
    random.shuffle(notSpamData)
    random.shuffle(spamData)

    minLen = (len(notSpamData) <= len(spamData) and len(notSpamData) or len(spamData))
    vectorizedDataList = notSpamData[:minLen] + spamData[:minLen]
    random.shuffle(vectorizedDataList)

    X, y = [], []
    maxIndex = 0
    for vectorizedData in vectorizedDataList:
        strList = vectorizedData[1].split()
        tempList = []
        for str in strList:
            tempList.append(int(str))
            maxIndex = maxIndex < int(str) and int(str) or maxIndex
        X.append(tempList)
        y.append(vectorizedData[-1])
    ml_data.X = np.array(X)
    ml_data.y = np.array(y)
    ml_data.vocabularyLen = maxIndex+1
    print(ml_data.X.shape, ml_data.y.shape, ml_data.vocabularyLen)
    return ml_data

if __name__ == "__main__":
    load_vectorized_data()