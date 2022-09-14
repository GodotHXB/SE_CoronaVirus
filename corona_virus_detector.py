import asyncio
import re
import os
from bs4 import BeautifulSoup
from pyppeteer import launch
from tqdm import tqdm

Year = 2022 # 设置全局变量，给爬取到的文件命名

def Year_Change(date):
    # 命名使用，更改年份
    global Year
    if (date == "12月31日"):
        Year = Year - 1

async def pyppteer_fetchUrl(url):
    browser = await launch({'headless': True, 'dumpio': True, 'autoClose': True})
    page = await browser.newPage()
    # 绕过浏览器检测
    await page.evaluateOnNewDocument('() =>{ Object.defineProperties(navigator,'
                                     '{ webdriver:{ get: () => false } }) }')
    await page.setUserAgent(
        'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/'
        '537.36 Edg/105.0.1343.33')
    await page.goto(url)
    await asyncio.wait([page.waitForNavigation()],timeout=5)
    str = await page.content()
    await browser.close()
    return str


# 获取某一页面源代码
def Get_Pagesouce(url):
    return asyncio.get_event_loop().run_until_complete(pyppteer_fetchUrl(url))

def Get_url_in_page(page):
    # 获取列表里所有通报的不完整URL
    half_urls = {}
    if page == 1:
        script = Get_Pagesouce('http://www.nhc.gov.cn/xcs/yqtb/list_gzbd.shtml')
    else:
        script = Get_Pagesouce('http://www.nhc.gov.cn/xcs/yqtb/list_gzbd_'+str(page)+'.shtml')
    # 得到不完整的URL
    urls_in_page = re.findall('<ul class="zxxx_list">.*?</ul>',script,re.DOTALL)
    half_urls = re.findall('href="(.*?)" target', urls_in_page[0], re.DOTALL)
    print(str(page) + '/42 is done')
    return half_urls

def saveFile(data,filename,path):
    # 用于保存文件
    if not os.path.exists(path):
        os.makedirs(path)
    with open(path + filename + '.txt', 'w', encoding='utf-8') as f:
        f.write(data)


def Get_text(half_urls,page):
    # 获取疫情通报
    count = 120 # 特判计数用，防重名
    for half_url in half_urls:
        page_script = Get_Pagesouce('http://www.nhc.gov.cn' + half_url)
        soup = BeautifulSoup(page_script,'lxml')
        title_script = soup.find(attrs={"class":"tit"})
        title_script = title_script.text # 标题，用于获取时间
        page_script = soup.find(attrs={"class":"con"})
        text = page_script.text # 疫情通报正文
        if(page == 41):
                # 特判，爬取最后一页特殊标题的疫情通报，后期再对文件名进行修改。
                title = title_script
                print(title)
                if(title == "武汉市卫生健康委员会关于新型冠状病毒感染的肺炎情况通报"):
                    saveFile(text, str(count)+title, 'data/txts/')
                    count = count - 1
                else:
                    saveFile(text, title, 'data/txts/')
        else:
            # 通用爬取疫情通报
            try:
                date = re.findall(r'截至(.+)24时', title_script, re.DOTALL)[0]
            except IndexError:
                continue
            Year_Change(date)
            saveFile(text, str(Year)+"年"+str(date)+"疫情通报", 'data/txts/')

if __name__ == '__main__':
    # 主函数
    for page in range(1,42):
        urls = Get_url_in_page(page)
        Get_text(urls,page)