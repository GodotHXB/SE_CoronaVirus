import os
import re
import pandas

lst = os.scandir("D:/CoronaVirus/data/txts") # 疫情通报数据本地位置

def to_excel(path,data,date,cn1,cn2,cn3,name):
    # 导出excel表格
    excel = pandas.DataFrame(data,index=list(range(1,len(data.keys())+1)),columns=[cn1,cn2,cn3])
    excel[cn1] = date
    excel[cn2] = data.keys()
    excel[cn3] = data.values()
    excel.to_excel(path + name,index=False)

def get_main_land_data(file):
    # 获取大陆数据
    newly_infected = 0
    newly_infected_n = 0

    with open(file, 'r', encoding='utf-8') as fp:
        title = file.name
        date = re.findall("(.*?)疫情通报", title)[0]  # 得到日期
        print(date)
        text = fp.read()
    try:
        newly_infected = re.findall("新增确诊病例(.*?)例", text, re.DOTALL)[0]
    except IndexError:
        pass
    try:
        newly_infected_n = re.findall('新增无症状感染者(.*?)例', text, re.DOTALL)[0]
    except IndexError:
        pass

    whole_nation = {}
    whole_nation['新增确诊病例'] = newly_infected
    whole_nation['新增无症状感染者'] = newly_infected_n
    print(newly_infected)
    print(newly_infected_n)
    to_excel('D:/CoronaVirus/data/main_land_excels/', whole_nation, date, 'date', 'type', 'count', date + '中国大陆新增数据.xlsx')

if __name__ == '__main__':
    for file in lst:
        get_main_land_data(file)