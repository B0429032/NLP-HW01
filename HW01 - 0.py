import jieba
import jieba.analyse
import numpy as np
import csv
from collections import Counter
text = open('hw1-dataset.txt', "r",encoding="utf-8").read()  #讀文字資料
n = 0
jieba.set_dictionary('dict.txt.big.txt')
with open('dictionary/stopWord_cloudmod.txt', 'r', encoding='utf-8-sig') as f:#設定停用詞
    stops = f.read().split('\n')
terms = []  #儲存字詞
for t in jieba.cut(text, cut_all=False):  #拆解句子為字詞
    if t not in stops:  #不是停用詞
        terms.append(t)
        n=n+1
diction = Counter(terms)
# 可列印詞的統計數
print(n)
print(t)
print(diction)
