import jieba
import wordcloud
import cv2


def stopwordslist(filepath):
    stopwords = [line.strip() for line in open(filepath, 'r', encoding='utf-8').readlines()]
    return stopwords

f = open("./daily/日报.txt", 'r+', encoding='gbk')
ftxt = f.read()
f.close()

# 添加用户自定义词汇
# jieba.load_userdict('自定义词汇表.txt')

# 添加停用词
stopwords = stopwordslist("./stopwords/停用词.txt")

lx = jieba.lcut(ftxt)
# txt = " ".join(lx)
txt = ''
for word in lx:
    if word not in stopwords:
        if word != '\t':
            txt += word
            txt += " "

w = wordcloud.WordCloud(font_path="./font/pzh.ttf", width=1024, height=768, background_color='white', max_words=40,)

'''
    w= word_cloud.WordCloud(font_path=font_path, # 设置字体
                           background_color=color, # 背景颜色
                           max_words=top_k, # 词云显示的最多词数
                           max_font_size=100, # 字体最大
                           mask=bg_img, # 背景图
                           )
'''

w.generate(txt)
w.to_file('word_cloud.png')
src = cv2.imread("./word_cloud.png")
cv2.imshow("word_cloud", src)
cv2.waitKey(0)
