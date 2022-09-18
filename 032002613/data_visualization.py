import pandas as pd
import matplotlib.pyplot as plt
from matplotlib import font_manager

plt.rcParams['font.sans-serif'] = ['SimHei']
my_font = font_manager.FontProperties(fname="C:/WINDOWS/Fonts/STSONG.TTF")

provinces = ['河北', '山西', '辽宁', '吉林', '黑龙江', '江苏', '浙江', '安徽', '福建', '江西', '山东', '河南', '湖北', '湖南', '广东', '海南',
             '四川', '贵州', '云南', '陕西', '甘肃', '青海', '内蒙古', '广西', '西藏', '宁夏', '新疆', '北京', '天津', '上海', '重庆']


def make_mainland_newly_infected():
    # 生成大陆本土新增确诊数据图
    plt.figure(figsize=(24, 10), dpi=300)
    data = pd.read_excel('中国大陆本土数据总表.xlsx')
    # print(data)

    # 中国大陆本土新增确诊病例
    infected = data[data['type'] == '新增确诊病例']
    infected_count = infected['count']
    print(infected_count)

    date = infected['date']
    print(date)

    plt.plot(date, infected_count)

    plt.xticks(range(0, 978, 80))
    plt.yticks(range(0, 20001, 300))
    plt.ylim(0, 15500)
    plt.xlabel("日期", fontproperties=my_font, fontsize=18)
    plt.ylabel("新增确诊病例数量", fontproperties=my_font, fontsize=18)

    plt.title("中国大陆本土新增确诊病例")
    plt.show()


def make_mainland_newly_infected_n():
    # 生成大陆本土新增无症状感染者数据图
    plt.figure(figsize=(24, 10), dpi=300)
    data = pd.read_excel('中国大陆本土数据总表.xlsx')
    # print(data)

    # 中国大陆本土新增无症状病例
    infected_n = data[data['type'] == '新增无症状感染者']
    infected_count_n = infected_n['count']
    print(infected_count_n)

    date = infected_n['date']
    print(date)

    plt.plot(date, infected_count_n)

    plt.xticks(range(0, 978, 80))
    plt.yticks(range(0, 28000, 500))
    plt.ylim(0, 28000)
    plt.xlabel("日期", fontproperties=my_font, fontsize=18)
    plt.ylabel("新增无症状感染者数量", fontproperties=my_font, fontsize=18)

    plt.title("中国大陆本土新增无症状感染者")
    plt.show()


def make_province_newly_infected(date):
    # 各省份某日本土新增确诊病例
    plt.figure(figsize=(24, 10), dpi=300)
    data = pd.read_excel('各省份新增确诊数据总表.xlsx')
    # print(data)

    # 各省份某日本土新增确诊病例，同时判断输入的日期是否合法
    infected = data[data['date'] == date]
    if infected.empty == True:
        print("输入的日期错误！")
        return
    print(infected)

    count = infected['count']
    # print(count)

    plt.bar(provinces, count)

    plt.xlabel("省份", fontproperties=my_font, fontsize=15)
    plt.ylabel("新增确诊数量", fontproperties=my_font, fontsize=15)
    for a, b in zip(provinces, count):
        plt.text(a, b, format(b, ','), ha='center', fontsize=16)
    plt.title("各省份" + date + "本土新增确诊病例")
    plt.show()


def make_province_newly_infected_n(date):
    # 各省份某日本土新增无症状感染者
    plt.figure(figsize=(24, 10), dpi=300)
    data = pd.read_excel('各省份新增无症状感染者数据总表.xlsx')
    # print(data)

    # 各省份某日本土新增无症状感染者病例，同时判断输入的日期是否合法
    infected_n = data[data['date'] == date]
    if infected_n.empty == True:
        print("输入的日期错误！")
        return
    # print(infected_n)

    count = infected_n['count']
    # print(count)

    plt.bar(provinces, count)

    plt.xlabel("省份", fontproperties=my_font, fontsize=15)
    plt.ylabel("新增无症状感染者数量", fontproperties=my_font, fontsize=15)
    for a, b in zip(provinces, count):
        plt.text(a, b, format(b, ','), ha='center', fontsize=16)
    plt.title("各省份" + date + "本土新增无症状感染者")
    plt.show()

def make_special_area_infected(select_area):
    # 生成港澳台新增确诊数据图
    plt.figure(figsize=(24, 10), dpi=300)
    data = pd.read_excel('港澳台数据总表.xlsx')
    # print(data)

    # 港澳台累计确诊病例
    infected_g = data[data['area'] == '香港特别行政区']
    infected_a = data[data['area'] == '澳门特别行政区']
    infected_t = data[data['area'] == '台湾地区']
    # print(infected_g)
    infected_count_g = infected_g['count']
    infected_count_a = infected_a['count']
    infected_count_t = infected_t['count']
    # print(infected_count)

    date = infected_g['date']
    # print(date)

    if select_area == '香港':
        plt.plot(date, infected_count_g)
        plt.xticks(range(0, 978, 80))
        plt.yticks(range(0, 450000, 10000))
        plt.ylim(0, 450000)
        plt.xlabel("日期", fontproperties=my_font, fontsize=18)
        plt.ylabel("累计确诊病例数量", fontproperties=my_font, fontsize=18)
        plt.title("香港特别行政区累计确诊病例")
        plt.show()

    if select_area == '澳门':
        plt.plot(date, infected_count_a)
        plt.plot(date, infected_count_a)
        plt.xticks(range(0, 978, 80))
        plt.yticks(range(0, 800, 40))
        plt.ylim(0, 800)
        plt.xlabel("日期", fontproperties=my_font, fontsize=18)
        plt.ylabel("累计确诊病例数量", fontproperties=my_font, fontsize=18)
        plt.title("澳门特别行政区累计确诊病例")
        plt.show()

    if select_area == '台湾':
        plt.plot(date, infected_count_t)
        plt.plot(date, infected_count_t)
        plt.xticks(range(0, 978, 80))
        plt.yticks(range(0, 6000000, 300000))
        plt.ylim(0, 6000000)
        plt.xlabel("日期", fontproperties=my_font, fontsize=18)
        plt.ylabel("累计确诊病例数量", fontproperties=my_font, fontsize=18)
        plt.title("台湾地区累计确诊病例")
        plt.show()


if __name__ == '__main__':
    mode = int(input("""请输入想要生成的数据类型：
1.中国大陆本土新增确诊病例
2.中国大陆本土新增无症状感染者
3.各省份某日本土新增确诊病例
4.各省份某日本土新增无症状感染者
5.港澳台累计确诊病例
（输入1-5的某个数字，输入0退出）：
"""))

    if mode == 1:
        make_mainland_newly_infected()
    if mode == 2:
        make_mainland_newly_infected_n()
    if mode == 3:
        date = input("输入某个日期（例：2021年7月9日）：")
        make_province_newly_infected(date)
    if mode == 4:
        date = input("输入某个日期（例：2021年7月9日）：")
        make_province_newly_infected_n(date)
    if mode == 5:
        select_area = input("请输入想要生成的地区（香港，澳门，台湾）：")
        make_special_area_infected(select_area)
    if mode == 0:
        pass
