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

def get_province_data(file):
    # 获取每个省份的数据
    # 初始化，防止报错
    newly_infected = 0
    newly_infected_n = 0
    context_newly_infected = ""
    context_newly_infected_n = ""
    by_province = {}
    by_province_n = {}
    # 建立包含所有省份的list，以便后续分类使用
    provinces = ['河北', '山西', '辽宁', '吉林', '黑龙江', '江苏', '浙江', '安徽', '福建', '江西', '山东', '河南', '湖北', '湖南', '广东', '海南',
                 '四川', '贵州', '云南', '陕西', '甘肃', '青海', '内蒙古', '广西', '西藏', '宁夏', '新疆', '北京', '天津', '上海', '重庆']

    for province in provinces:
        by_province[province] = 0
        by_province_n[province] = 0

    # 获取日期
    with open(file, 'r', encoding='utf-8') as fp:
        title = file.name
        date = re.findall("(.*?)疫情通报", title)[0]  # 得到日期
        print(date)
        text = fp.read()

    # 提取本土新增病例相关内容和本土新增无症状感染者相关内容
    try:
        context_newly_infected = re.findall("本土病例.*?例(.*?)）", text, re.DOTALL)[0] # 本土新增病例
        context_newly_infected_n = re.findall("新增无症状感染者.*本土.*?例(.*)）", text, re.DOTALL)[0] # 本土新增无症状感染者
    except IndexError:
        pass

    # 提取各省份本土新增病例数据
    try:
        province_name = re.findall("([\u4E00-\u9FA5]+?)[0-9]*?例", context_newly_infected, re.DOTALL)
        province_count = re.findall('[\u4E00-\u9FA5]+?([0-9]*?)例', context_newly_infected, re.DOTALL)
        i = 0
        for province in province_name:
            if(province in provinces):
                by_province[province] = province_count[i]
                i = i + 1
    except IndexError:
        pass

    # 提取各省份本土新增无症状感染者数据
    try:
        province_name = re.findall("([\u4E00-\u9FA5]+?)[0-9]*?例", context_newly_infected_n, re.DOTALL)
        province_count = re.findall('[\u4E00-\u9FA5]+?([0-9]*?)例', context_newly_infected_n, re.DOTALL)
        i = 0
        for province in province_name:
            if(province in provinces):
                by_province_n[province] = province_count[i]
                i = i + 1
    except IndexError:
        pass

    # 写入excel表格
    to_excel('D:/CoronaVirus/data/province_excels/', by_province, date,
             'date', 'province', 'count', date + '各省份本土新增感染者数据.xlsx')
    to_excel('D:/CoronaVirus/data/province_excels/', by_province_n, date,
             'date', 'province', 'count', date + '各省份本土新增无症状感染者数据.xlsx')

def get_special_area_data(file):
    # 获取港澳台数据
    total_infected = ""
    total_infected_g = 0
    total_infected_a = 0
    total_infected_t = 0

    special_area = ['香港特别行政区','澳门特别行政区','台湾地区']

    with open(file, 'r', encoding='utf-8') as fp:
        title = file.name
        date = re.findall("(.*?)疫情通报", title)[0]  # 得到日期
        print(date)
        text = fp.read()

    try:
        total_infected = re.findall("累计收到港澳台地区通报确诊病例(.*)", text, re.DOTALL)[0]
    except IndexError:
        pass

    try:
        total_infected_g = re.findall('香港特别行政区(.*?)例', total_infected, re.DOTALL)[0]
        total_infected_a = re.findall('澳门特别行政区(.*?)例', total_infected, re.DOTALL)[0]
        total_infected_t = re.findall('(台湾地区|中国台湾)(.*?)例', total_infected, re.DOTALL)[0][1]
    except IndexError:
        pass

    special_area_data = {}
    special_area_data['香港特别行政区'] = total_infected_g
    special_area_data['澳门特别行政区'] = total_infected_a
    special_area_data['台湾地区'] = total_infected_t
    to_excel('D:/CoronaVirus/data/special_area_excels/', special_area_data, date, 'date', 'area', 'count', date + '港澳台累计确诊数据.xlsx')

if __name__ == '__main__':
    for file in lst:
        # get_main_land_data(file)
        # get_province_data(file)
        get_special_area_data(file)