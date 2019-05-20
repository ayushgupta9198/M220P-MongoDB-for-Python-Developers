# ==========================PANDAS===================
import pandas as pd
# import numpy as np
# import urllib.request
# import requests
# import _ssl
# pat='https://raw.githubusercontent.com/justmarkham/DAT8master/data/chipotle.tsv'
# path=urllib.request.urlopen(pat)

res=r'C:\Users\Prince\Downloads\chipotle.tsv.txt'
z = pd.read_csv(res,sep='\t')

# z=pd.read_csv(path)
# # print(z.dtypes)
# print(z)

chipo=pd.DataFrame(z)
# print(chipo.head(10))
# '''for name of columns'''
# column_name=pd.DataFrame(z.columns)
# '''for number of columns'''
# column_name=pd.DataFrame(z.columns).count()
# column_name=pd.DataFrame(z.index)'''for number of rows'''
df=pd.DataFrame(z)
# q=df['item_price'].apply(lambda S:S.strip('$')).astype(float)
# df['item_price']=df['item_price'].astype(float)
# print(p.sum())

# p=df['order_id']
# print(p.max())
# print(q.sum()/p.max())
p=df.groupby('choice_description').sum().sort_values(['quantity'],ascending=False)
# for i in p:
print(p)


# =====================================================
# s1=pd.Series(['A','B','C','D'],index=['p1','p2','p3','p4'])
# print(s1)
# print(s1[1:3])

# dict1={'name':['A','B','C','D'],'age':[10,20,30,40]}
# dict2=[{'name':'A','age':10},
#        {'name':'B','age':20},
#        {'name':'C','age':30}]
# df1=pd.DataFrame(dict1)
# print(df1)
# df2=pd.DataFrame(dict2,index=['name','age'])
# print(df2)

