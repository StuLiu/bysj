"""
===================================
     初始化emoji dict文件
===================================
"""

print(__doc__)

if __name__ == '__main__':

    sample_list = ['\u00AE','\U0001f6bb','\U0001F192','\u00a9','\u2139', '\u231B', '\u26A0', '\u2712', '\u2764', '\U0001F004', '\U0001F21A', '\U0001f436', ]
    for emoji in sample_list:
        print(emoji,emoji.encode('utf-8'),type(emoji))


    # with open('./dict/emoji_dict.txt', 'w', encoding='utf8') as f:
    #     f.writelines([emoji+' 65535 emoji\n' for emoji in sample_list])