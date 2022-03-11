
# -*- coding: utf-8 -*-
import jieba
import numpy as np
import pandas as pd
import jieba
import jieba.analyse
import codecs
import jieba.posseg as psg
data="C:\\Users\\lenovo\\Desktop\\test\\whwtmp1.txt"
segments = []
eleseg=[]
with open("C:\\Users\\lenovo\\Desktop\\test\\processed_data.txt", "r", encoding='utf-8') as f1:
    text = f1.read()
    seg_list = jieba.cut(text)
    seg=psg.cut(text)
    f2 = open("C:\\Users\\lenovo\\Desktop\\test\\result.txt", "a", encoding='utf-8')
    for word in seg_list:
        f2.write(word + " ")
        segments.append({'word':word, 'count':1})
    f2.close()
    f3 = open("C:\\Users\\lenovo\\Desktop\\test\\cixingbiaozhu.txt", "a", encoding='utf-8')
    for word1 in seg:
      #  print(word1.flag)
        f3.write(str(word1) + " ")
        eleseg.append({'word':word1.word,'flag':word1.flag,'count':1})
    f3.close()
dfSg = pd.DataFrame(segments)
dfWord = dfSg.groupby('word')['count'].sum()
dfWord.to_csv('C:\\Users\\lenovo\\Desktop\\test\\keywords.csv',encoding='utf-8')
df=pd.DataFrame(eleseg)
dfWord2=df.groupby(['word','flag'])['count'].sum()
dfWord2.to_csv('C:\\Users\\lenovo\\Desktop\\test\\keyword2s.csv',encoding='utf-8')


