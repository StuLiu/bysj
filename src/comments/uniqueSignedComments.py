
from database.signed_comments_dbHandler import SignedCommentsDbHandler

if __name__ == "__main__":
    dbHandler = SignedCommentsDbHandler()
    commentList = dbHandler.queryAll()
    print(commentList)
    uniqueCommentList = []
    for comment in commentList:
        if uniqueCommentList.count(comment[3]) == 0:
            uniqueCommentList.append(comment[3])
            dbHandler.insertSignedComment(comment)