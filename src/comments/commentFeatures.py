

from database.signed_comments_dbHandler import SignedCommentsDbHandler
import matplotlib.pyplot as plt

# 返回评论内容长度的最大值
def getMaxLengthOfContentLength():
    commentsList = SignedCommentsDbHandler().queryAll()
    maxLen = 0
    for comment in commentsList:
        if len(comment[3]) > maxLen:
            maxLen = len(comment[3])
    return maxLen

# 展示垃圾评论和非垃圾评论的分布
def showPersentOfSpamAndNotSpam():
    commentsList = SignedCommentsDbHandler().queryAll()
    countSpam, countNotSpam = 0., 0.
    for comment in commentsList:
        if comment[-1] == 1:
            countSpam += 1
        else:
            countNotSpam += 1
    x = [0]
    xx = [1]
    y = [countNotSpam/(countNotSpam+countSpam)*100]
    yy = [countSpam/(countNotSpam+countSpam)*100]
    print(y,yy)
    plt.bar(x, y, 0.4, color="#43CD80", label='not spam comment')
    plt.bar(xx, yy, 0.4, color="#FF4040", label='spam comment')
    plt.legend(loc='upper right')
    plt.xticks([0,1], ['spam', 'notSpam'])
    plt.ylabel("persent/%")
    plt.xlabel("isOrNotSpam")
    plt.title("persent of spam and notspam comments")
    plt.axis([-1, 2, 0, 100])
    # 使用text显示数值
    for a, b in zip(x, y):
        plt.text(a, b + 1, '%.2f' % b, ha='center', va='bottom', fontsize=11)
    for a, b in zip(xx, yy):
        plt.text(a, b + 1, '%.2f' % b, ha='center', va='bottom', fontsize=11)
    plt.grid(color='b', linewidth='0.2', linestyle='--', axis='y')
    plt.show()


# 展示评论长度对应评论数量的分布
def showDistributionOfContentLength():
    commentsList = SignedCommentsDbHandler().queryAll()
    MaxLen = 6100
    lengthList = range(0,MaxLen)
    contentLengthOfSpam, contentLengthOfNotSpam = [0]*MaxLen, [0]*MaxLen
    for comment in commentsList:
        tempLength = len(comment[3]) < MaxLen and len(comment[3]) or MaxLen-1
        if comment[-1] == 1:
            contentLengthOfSpam[tempLength] += 1
        else:
            contentLengthOfNotSpam[tempLength] += 1
    plt.figure(1)  # 创建第一个画板（figure）
    plt.plot(lengthList, contentLengthOfSpam, 'r-',  label='spam comment')
    plt.plot(lengthList, contentLengthOfNotSpam, 'g-', label='not spam comment')
    plt.legend(loc='upper right')
    plt.title("length of comment")
    plt.xlabel("length")
    plt.ylabel('count')
    plt.grid(color='b', linewidth='0.2', linestyle='--')
    plt.show()

# 展示不同评分等级下评论的分布
def showDistributionOfRating():
    commentsList = SignedCommentsDbHandler().queryAll()
    countSpam, countNotSpam = 0., 0.
    countRatingSpam, countRatingNotSpam = [0]*5, [0]*5
    for comment in commentsList:
        if comment[-1] == 1:
            countSpam += 1
            countRatingSpam[comment[6] - 1] += 1
        else:
            countNotSpam += 1
            countRatingNotSpam[comment[6] - 1] += 1
    for i in range(0,5):
        countRatingSpam[i] /= countSpam
        countRatingNotSpam[i] /= countNotSpam

    plt.figure(1)  # 创建第一个画板（figure）
    x1 = [0.8, 1.8, 2.8, 3.8, 4.8]
    plt.bar(x1, countRatingSpam, 0.4, color="#FF4040", label='spam comment')

    x2 = [1.2, 2.2, 3.2, 4.2, 5.2]
    plt.bar(x2, countRatingNotSpam, 0.4, color="#43CD80", label='not spam comment')
    plt.legend(loc='upper left')
    plt.title("rating distribution")
    plt.xlabel("rating")
    plt.ylabel('persent/%')
    plt.grid(color='b', linewidth='0.2', linestyle='--', axis='y')
    plt.show()

if __name__ == '__main__':
    # print(getMaxLengthOfContentLength())
    # showPersentOfSpamAndNotSpam()
    # showDistributionOfContentLength()
    showDistributionOfRating()
