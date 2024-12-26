import pandas as pd
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.edge.service import Service

driver = webdriver.Edge(service=Service('C:/Users/Rschel/Downloads/edgedriver_win64/msedgedriver.exe'))

driver.get("https://www.yearupalumni.org/s/1841/interior.aspx?sid=1841&gid=2&pgid=440")

results = []

content = driver.page_source
soup = BeautifulSoup(content, features="html.parser")


driver.quit()

for element in soup.find_all('div', class_='title'):
    name_tag = element.find('a')
    if name_tag:
        name = name_tag.text.strip()
        if name and name not in results:
            results.append(name)


df = pd.DataFrame({'Names': results})
df.to_csv('title.csv', index=False, encoding='utf-8')


