

import re
import jieba.posseg
import config
import os

from sklearn.feature_extraction.text import CountVectorizer,TfidfTransformer
# 使用scikit-learn自带的向量化操作向量化评论内容
def tf_idf_vectoring(content_array):
    """
    :param content_array: 评论文本数组
    :return: 根据tf-idf方法向量化后的矩阵
    """
    countVectorizer = CountVectorizer()
    x_counts = countVectorizer.fit_transform(content_array)
    tfidf_transformer = TfidfTransformer()
    x_tfidf = tfidf_transformer.fit_transform(x_counts)
    print("TfidfTransform finished,result shape:",x_tfidf.shape)
    return x_tfidf


#     根据数据总结出：评论id长度、评论长度、‘评论词’比例、英文所占比例、
# 名词所占比例、动词所占比例、形容词所占比例、emoji和特殊字符所占比例、
# 感叹词所占比例、数字和量词所占比例、评分等级等数据为评论文本特征。
from database.signed_comments_dbHandler import SignedCommentsDbHandler
from database.apple_app_dbHandler import AppleAppDbHandler
import numpy as np
class Vectorizer(object):

    def __init__(self):
        jieba.load_userdict(os.path.join(config.DICT_PATH, "user_defined_dict.txt"))
        jieba.load_userdict(os.path.join(config.DICT_PATH, "sogoupinyin_dict.txt"))

        signedCommentsDbHandler = SignedCommentsDbHandler()
        appleAppDbHandler = AppleAppDbHandler()

        self.appId_rating_mean_dict = {}
        appList = appleAppDbHandler.queryAll()
        for app in appList:
            print(app)
            self.appId_rating_mean_dict[app[0]] = app[2]

        signedComments = signedCommentsDbHandler.queryAll()
        self.commentId_comment_dict = {}    # {comment_id:signedComment}
        self.userName_commentIds_dict = {}  # {user_name:[comment_id,comment_id,...]}
        self.content_count_dict = {}        # {content:count}
        for signedComment in signedComments:
            self.commentId_comment_dict[signedComment[1]] = signedComment
            if signedComment[8] in self.userName_commentIds_dict.keys():
                self.userName_commentIds_dict[signedComment[8]].append(signedComment[1])
            else:
                self.userName_commentIds_dict[signedComment[8]] = [signedComment[1]]
            if signedComment[3] in self.content_count_dict.keys():
                self.content_count_dict[signedComment[3]] += 1
            else:
                self.content_count_dict[signedComment[3]] = 1
        print('commentId_comment_dict len',len(self.commentId_comment_dict.keys()))
        print('userName_commentIds_dict len',len(self.userName_commentIds_dict.keys()))
        print('content_count_dict len',len(self.content_count_dict.keys()))
        print('init finish')


    def vectoringOneComment(self, comment_id, title, content, rating, user_name, app_id):
        """
        :param comment_id : 评论id
        :param title: 评论标题
        :param content: 评论主要内容
        :param rating : 评分等级
        :param user_name : 用户名
        :param app_id : 应用的id
        :return vectorizedComment : 向量化后的评论向量
        """

        title_len = len(title)
        content_len = len(content)
        content_isUnique = int(self.content_count_dict[content] == 1)
        comment_rating = rating

        commentsIdOfTheReviewer = self.userName_commentIds_dict[user_name]  #list

        comment_count_of_the_reviewer = len(commentsIdOfTheReviewer)

        ratingList = []
        for commentId in commentsIdOfTheReviewer:
            ratingList.append(self.commentId_comment_dict[commentId][6])

        comment_rating_mean_of_the_reviewer = float(np.average(ratingList))
        comment_rating_offset_of_the_reviewer = abs(rating - comment_rating_mean_of_the_reviewer)/5
        comment_rating_std_dev_of_the_reviewer = float(np.std(ratingList))

        comment_rating_isSame_of_the_reviewer = int(len(ratingList)>1 and len(set(ratingList))==1)

        comment_rating_mean_of_app = self.appId_rating_mean_dict[app_id]
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
            comment_id,
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

# def vectoringComment(comment_id, comment_title, comment_content, comment_rating):
#     """
#     :param comment_id: 评论id
#     :param comment_title: 评论标题
#     :param comment_content: 评论主要内容
#     :param comment_rating:  评分等级
#     :return vectorizedComment: 向量化后的评论向量
#     """
#     jieba.load_userdict(os.path.join(config.DICT_PATH, "user_defined_dict.txt"))
#     jieba.load_userdict(os.path.join(config.DICT_PATH, "sogoupinyin_dict.txt"))
#
#     punctuation = r'[！!、，,。：:；;？?‘\'’“\"”——（）\(\)【】\[\]\{\}……\-~`·》《<>]'
#     content_w_counter = len(re.findall(punctuation, comment_content))   # 标点符号数量
#     space = r'[\s]'
#     words = jieba.posseg.lcut(re.sub(space,'',comment_content,0))   # 去处空白字符再分词
#     words_len = len(words)
#     content_pl_counter = 0      # 评论词数量
#     content_eng_counter = 0     # 英文数量
#     content_n_counter = 0       # 名词数量
#     content_v_counter = 0       # 动词数量
#     content_a_counter = 0       # 形容词数量
#     content_x_counter = 0 - content_w_counter   # jieba视标点符号为x类字符，'.'除外
#     content_y_counter = 0       # 语气词数量
#     content_m_counter = 0       # 数词数量
#     for word, flag in words:
#         # print('%s %s' % (word, flag))
#         if flag == 'pl':
#             content_pl_counter += 1
#         elif flag == 'eng':
#             content_eng_counter += 1
#         elif flag == 'n' or flag == 'nr' or flag == 'ns' or flag == 'nt' or flag == 'nz':
#             content_n_counter += 1
#         elif flag == 'vg' or flag == 'v' or flag == 'vd' or flag == 'vn':
#             content_v_counter += 1
#         elif flag == 'Ag' or flag == 'a' or flag == 'ad' or flag == 'an':
#             content_a_counter += 1
#         elif flag == 'x':
#             content_x_counter += 1
#         elif flag == 'y':
#             content_y_counter += 1
#         elif flag == 'm':
#             content_m_counter += 1
#         else:
#             pass
#     vectorizedComment = [
#         comment_id,
#         len(comment_title),
#         len(comment_content),
#         float(content_pl_counter) / words_len,
#         float(content_eng_counter) / words_len,
#         float(content_n_counter) / words_len,
#         float(content_v_counter) / words_len,
#         float(content_a_counter) / words_len,
#         float(content_x_counter) / words_len,
#         float(content_w_counter) / words_len,
#         float(content_y_counter) / words_len,
#         float(content_m_counter) / words_len,
#         comment_rating
#     ]
#     # print(vectorizedComment)
#     return vectorizedComment


# 建立词汇表并将将评论内容向量化
def vectoringContent(max_sequence_len, contentMatrix):
    """
    :param max_sequence_len: 单个评论最大词语数，评论词语数大于此值时截去多余词语，反之则填充
    :param contentMatrix:[[comment_id,comment_content],...]
    :return:[[comment_id,vectorString],...]
    """
    jieba.load_userdict(os.path.join(config.DICT_PATH, "user_defined_dict.txt"))
    jieba.load_userdict(os.path.join(config.DICT_PATH, "sogoupinyin_dict.txt"))
    result = []
    index = 1
    vocabulary = {"PADDING_WORD" : 0}  # {word:index,word:index,...}
    for pair in contentMatrix:
        vectorString = ''
        wordsList = list(jieba.cut(re.sub(r'[^\u4e00-\u9fa5]', '', pair[1], 0),cut_all=False))
        wordsListLen = len(wordsList)
        for num in range(0,max_sequence_len):
            if num < wordsListLen:
                if wordsList[num] in vocabulary:
                    vectorString += ' ' + str(vocabulary[wordsList[num]])
                else:
                    vocabulary[wordsList[num]] = index
                    vectorString += ' ' + str(index)
                    index += 1
            if num >= wordsListLen:
                vectorString += ' 0'
        result.append([pair[0],vectorString])
    for key in vocabulary.keys():
        print(key,vocabulary[key])
    print("vocabulary length:",len(vocabulary))
    print(result)
    return result

if __name__ == '__main__':

    contents = [
        "iPhone X蚂蚁花呗打开后一片空白",
        "👍👍【付临门】【联刷钱包】0.28%秒到！0.28%秒到！分享商机，共享未来！分享支付！改变未来！分润万16+2秒结秒结！总部咨询185-1652-4888微信同号",
        "每次打开就是提示更新烦不烦？不是每个用户都需要啥双十二优惠，不屑懂不？",
        "棋牌游戏开发：L492078507",
        "只要一部手机📱，躺在家里也能zuan0🌸💰➕为❤615912134",
        "支付宝推荐！关注VX共众號【swapp321】手木几转RM￥，当天进口袋贰佰圆！",
        "rt 无力吐槽sb马云",
        "    s  膜拜单车摩拜单车❤❤ ",
        "Very useful!thanks a lot",
        "啊啊啊啊啊啊啊啊啊啊啊啊哦啊啊啊啊呀呀呀呃呃呃哦哦哦咦55555555咦",
        "!?？。、\'\"{}[]【】.啊"
    ]
    # contentMatrix = [
    #     ["123456", "iPhone X蚂蚁花呗打开后一片空白"],
    #     ["123457", "👍👍【付临门】【联刷钱包】0.28%秒到！0.28%秒到！分享商机，共享未来！分享支付！改变未来！分润万16+2秒结秒结！总部咨询185-1652-4888微信同号"],
    #     ["123458", "每次打开就是提示更新烦不烦？不是每个用户都需要啥双十二优惠，不屑懂不？   "]
    # ]
    # vectoringContent(25, contentMatrix)

    v = Vectorizer()