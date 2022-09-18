import pandas as pd
import matplotlib.pyplot as plt
from matplotlib import font_manager

plt.rcParams['font.sans-serif'] = ['SimHei']
my_font = font_manager.FontProperties(fname="C:/WINDOWS/Fonts/STSONG.TTF")


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
    print("successful")


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
    print("successful")


if __name__ == '__main__':
    # make_mainland_newly_infected()
    make_mainland_newly_infected_n()
