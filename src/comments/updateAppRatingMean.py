

from database.apple_app_dbHandler import AppleAppDbHandler
from database.signed_comments_dbHandler import SignedCommentsDbHandler

def doUpdate():

    sHandler = SignedCommentsDbHandler()
    aHandler = AppleAppDbHandler()

    appList = aHandler.queryAll()
    for appId, appName in appList:
        print(appId, appName)
        commentsList = sHandler.queryCommentsByAppId(appId)
        commentsCount = len(commentsList)
        if commentsCount == 0:
            aHandler.updateRatingMean(appId, 0.)
        else:
            totalRating = 0.
            for comment in commentsList:
                totalRating += comment[7]
            ratingMean = float(totalRating/commentsCount)
            aHandler.updateRatingMean(appId,ratingMean)

if __name__ == '__main__':
    doUpdate()