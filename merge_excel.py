import os
import re
import pandas as pd

dfs = []

lst = os.scandir("D:/CoronaVirus/data/special_area_excels") # 疫情通报数据本地位置
for file in lst:
    name = file.name
    print(name)
    df = pd.read_excel("D:/CoronaVirus/data/special_area_excels/" + name)
    dfs.append(df)
result = pd.concat(dfs)
result.to_excel("港澳台数据总表.xlsx",index=False)

# lst = os.scandir("D:/CoronaVirus/data/province_excels") # 疫情通报数据本地位置
# for file in lst:
#     name = file.name
#     if(name.endswith("新增感染者数据.xlsx")):
#         print(name)
#         df = pd.read_excel("D:/CoronaVirus/data/province_excels/" + name)
#         dfs.append(df)
# result = pd.concat(dfs)
# result.to_excel("各省份新增感染者数据总表.xlsx",index=False)