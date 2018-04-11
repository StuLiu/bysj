
import re

import jieba.posseg

import config
import os

class Vectorizer(object):
    """
    向量化评论文本数据
    """
    def __init__(self):
        # jieba导入自定义词典
        jieba.load_userdict(os.path.join(config.DICT_PATH,"user_defined_dict.txt"))
        jieba.load_userdict(os.path.join(config.DICT_PATH,"sogoupinyin_dict.txt"))


    def vectoring(self, comment_id, comment_title, comment_content, comment_rating):
        """
        :param comment_id: 评论id
        :param comment_title: 评论标题
        :param comment_content: 评论主要内容
        :param comment_rating:  评分等级
        :return vectorizedComment: 向量化后的评论向量
        """
        punctuation = r'[！!、，,。：:；;？?‘\'’“\"”——（）\(\)【】\[\]\{\}……\-~`·》《<>]'
        content_w_counter = len(re.findall(punctuation, comment_content))   #计算标点符号数量
        space = r'[\s]'
        words = jieba.posseg.lcut(re.sub(space,'',comment_content,0))   # 去处空白字符再分词
        words_len = len(words)
        content_pl_counter = 0
        content_eng_counter = 0
        content_n_counter = 0
        content_v_counter = 0
        content_a_counter = 0
        content_x_counter = 0 - content_w_counter   # jieba视标点符号为x类字符，'.'除外
        content_y_counter = 0
        content_m_counter = 0
        # print("=" * 30)
        for word, flag in words:
            print('%s %s' % (word, flag))
            if flag == 'pl':
                content_pl_counter += 1
            elif flag == 'eng':
                content_eng_counter += 1
            elif flag == 'n' or flag == 'nr' or flag == 'ns' or flag == 'nt' or flag == 'nz':
                content_n_counter += 1
            elif flag == 'vg' or flag == 'v' or flag == 'vd' or flag == 'vn':
                content_v_counter += 1
            elif flag == 'Ag' or flag == 'a' or flag == 'ad' or flag == 'an':
                content_a_counter += 1
            elif flag == 'x':
                content_x_counter += 1
            elif flag == 'y':
                content_y_counter += 1
            elif flag == 'm':
                content_m_counter += 1
            else:
                pass
        # print("wordlen", words_len)
        # print("content_pl_counter", content_pl_counter)
        # print("content_eng_counter", content_eng_counter)
        # print("content_n_counter", content_n_counter)
        # print("content_v_counter", content_v_counter)
        # print("content_a_counter", content_a_counter)
        # print("content_x_counter", content_x_counter)
        # print("content_w_counter", content_w_counter)
        # print("content_y_counter", content_y_counter)
        # print("content_m_counter", content_m_counter)
        vectorizedComment = [
            comment_id,
            len(comment_title),
            len(comment_content),
            float(content_pl_counter) / words_len,
            float(content_eng_counter) / words_len,
            float(content_n_counter) / words_len,
            float(content_v_counter) / words_len,
            float(content_a_counter) / words_len,
            float(content_x_counter) / words_len,
            float(content_w_counter) / words_len,
            float(content_y_counter) / words_len,
            float(content_m_counter) / words_len,
            comment_rating
        ]
        # print(vectorizedComment)
        return vectorizedComment

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
    sign = []
    vectorizer = Vectorizer()
    for content in contents:
        vectorizer.vectoring("comment_id","comment_title",content,0)



