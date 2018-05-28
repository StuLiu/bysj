
from database.signed_comments_dbHandler import SignedCommentsDbHandler
from database.apple_app_dbHandler import AppleAppDbHandler
import numpy as np
import jieba.posseg,os,config,re
class CommentVectorizer(object):

    def __init__(self):
        jieba.load_userdict(os.path.join(config.DICT_PATH, "user_defined_dict.txt"))
        jieba.load_userdict(os.path.join(config.DICT_PATH, "sogoupinyin_dict.txt"))

        signedCommentsDbHandler = SignedCommentsDbHandler()
        appleAppDbHandler = AppleAppDbHandler()

        self.__appId_rating_mean_dict = {}
        appList = appleAppDbHandler.queryAll()
        for app in appList:
            # print(app)
            self.__appId_rating_mean_dict[app[0]] = app[2]

        signedComments = signedCommentsDbHandler.queryAll()
        self.__commentId_comment_dict = {}    # {comment_id:signedComment}
        self.__userName_commentIds_dict = {}  # {user_name:[comment_id,comment_id,...]}
        self.__content_count_dict = {}        # {content:count}
        for signedComment in signedComments:
            self.__commentId_comment_dict[signedComment[1]] = signedComment
            if signedComment[8] in self.__userName_commentIds_dict.keys():
                self.__userName_commentIds_dict[signedComment[8]].append(signedComment[1])
            else:
                self.__userName_commentIds_dict[signedComment[8]] = [signedComment[1]]
            if signedComment[3] in self.__content_count_dict.keys():
                self.__content_count_dict[signedComment[3]] += 1
            else:
                self.__content_count_dict[signedComment[3]] = 1
        # print('commentId_comment_dict len',len(self.__commentId_comment_dict.keys()))
        # print('userName_commentIds_dict len',len(self.__userName_commentIds_dict.keys()))
        # print('content_count_dict len',len(self.__content_count_dict.keys()))
        # print('init finish')


    def doVectoring(self, comment_id, title, content, rating, user_name, app_id):
        """
        :param comment_id : 评论id
        :param title: 评论标题
        :param content: 评论主要内容
        :param rating : 评分等级
        :param user_name : 用户名
        :param app_id : 应用的id
        :return vectorizedComment : 向量化后的评论向量
        """
        self.__commentId_comment_dict[comment_id] = ['', comment_id, title, content,
                                                     0,0,rating,'',user_name,app_id,'0']
        if user_name in self.__userName_commentIds_dict.keys():
            self.__userName_commentIds_dict[user_name].append(comment_id)
        else:
            self.__userName_commentIds_dict[user_name] = [comment_id]

        if content in self.__content_count_dict.keys():
            self.__content_count_dict[content] += 1
        else:
            self.__content_count_dict[content] = 1


        title_len = len(title)
        content_len = len(content)
        content_isUnique = int(self.__content_count_dict[content] == 1)
        comment_rating = rating

        commentsIdOfTheReviewer = self.__userName_commentIds_dict[user_name]  #list

        comment_count_of_the_reviewer = len(commentsIdOfTheReviewer)

        ratingList = []
        for commentId in commentsIdOfTheReviewer:
            ratingList.append(self.__commentId_comment_dict[commentId][6])

        comment_rating_mean_of_the_reviewer = float(np.average(ratingList))
        comment_rating_offset_of_the_reviewer = abs(rating - comment_rating_mean_of_the_reviewer)/5
        comment_rating_std_dev_of_the_reviewer = float(np.std(ratingList))

        comment_rating_isSame_of_the_reviewer = int(len(ratingList)>1 and len(set(ratingList))==1)

        comment_rating_mean_of_app = self.__appId_rating_mean_dict[app_id]
        comment_rating_offset_of_the_app = abs(rating-comment_rating_mean_of_app)/5

        contentDict = {}
        keys = ['Ag', 'a', 'ad', 'an', 'b', 'c', 'dg', 'd', 'e', 'f', 'g', 'h',
                'i', 'j', 'k', 'l', 'm', 'Ng', 'n', 'nr', 'ns', 'nt' , 'nz',
                'o', 'p', 'q', 'r', 's', 'tg', 't', 'u', 'vg', 'v', 'vd', 'vn',
                'w', 'x', 'y', 'z', 'un', 'pl']
        for key in keys:
            contentDict[key] = 0.0
        wordAndFlag_list = jieba.posseg.lcut(re.sub(r'[\s]','', content,0))
        wordsCount = len(wordAndFlag_list)
        for word, flag in wordAndFlag_list:
            # print(word, flag)
            try:
                contentDict[flag] += 1.0
            except Exception:
                pass
        content_word_rate_list = []
        for key in keys:
            content_word_rate_list.append(contentDict[key]/wordsCount)

        vectorizedComment = [
            title_len,
            content_len,
            content_isUnique,
            comment_rating,
            comment_count_of_the_reviewer,
            comment_rating_mean_of_the_reviewer,
            comment_rating_offset_of_the_reviewer,
            comment_rating_std_dev_of_the_reviewer,
            comment_rating_isSame_of_the_reviewer,
            comment_rating_mean_of_app,
            comment_rating_offset_of_the_app
        ] + content_word_rate_list

        # print(vectorizedComment,len(vectorizedComment))
        return vectorizedComment
