import os
import re
import pandas as pd

dfs = []

def merging(path,filename):
    dfs.clear()
    lst = os.scandir(path) # 疫情通报数据本地位置
    for file in lst:
        name = file.name
        df = pd.read_excel(path + name)
        dfs.append(df)
    result = pd.concat(dfs)
    result.to_excel(filename,index=False)

if __name__ == '__main__':
    merging("D:/CoronaVirus/data/special_area_excels/", "港澳台数据总表.xlsx")
    merging("D:/CoronaVirus/data/province_excels/", "各省份新增确诊数据总表.xlsx")
    merging("D:/CoronaVirus/data/province_excels/", "各省份新增无症状感染者数据总表.xlsx")
    merging("D:/CoronaVirus/data/main_land_excels/", "中国大陆本土数据总表.xlsx")