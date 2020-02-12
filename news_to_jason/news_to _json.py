from selenium import webdriver
import time
import json

driverPath = 'D:/geckodriver/chromedriver.exe'
browser = webdriver.Chrome(executable_path=driverPath)
url = 'https://news.cnyes.com/news/cat/headline?exp=a'
browser.get(url)                # 網頁下載至瀏覽器

n1s = browser.find_elements_by_class_name('_1xc2')#抓焦點新聞


i=1
contents=[]
for n1 in range(len(n1s)):
     contents.append(str(i)+' '+n1s[n1].text)
     print(i, n1s[n1].text)   # 列印元素內容
     i=i+1

for content in contents:
        print(content)

fn = 'out1_9_2.json'
with open(fn, 'w', encoding='utf-8') as fnObj:
    json.dump(contents, fnObj, indent=2, ensure_ascii=False)



time.sleep(500)
