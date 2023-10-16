from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium import webdriver
from bs4 import BeautifulSoup
import time
import pyautogui
import csv


tp_area = ["中山區",]
key = '壽司'

driver = webdriver.Firefox()
url = "https://www.google.com/maps/place/%E7%B7%AF%E8%82%B2TibaMe%E9%99%84%E8%A8%AD%E5%8F%B0%E5%8C%97%E8%81%B7%E8%A8%93%E4%B8%AD%E5%BF%83/@25.0521328,121.540678,17z/data=!3m2!4b1!5s0x3442abddfc0bc85f:0x547998e4a2421286!4m6!3m5!1s0x3442abe6b0446815:0xf006dde8c27afcc7!8m2!3d25.052128!4d121.5432529!16s%2Fg%2F11qm1fb7m_?authuser=0&entry=ttu"
driver.get(url)
driver.implicitly_wait(10)  # 添加隱式等待
searchbox = driver.find_element(By.ID, "searchboxinput")  # 直接使用find_element方法
searchbox.clear()


for tp in tp_area:
    searchbox = driver.find_element(By.ID, "searchboxinput")  # 直接使用find_element方法
    searchbox.clear()

    searchbox.send_keys(key+" "+tp)
    searchbox.send_keys(Keys.ENTER)
    driver.implicitly_wait(3000)  # 再次添加隱式等待
    time.sleep(3)
    pyautogui.moveTo(711, 1060)
    time.sleep(2)
    
    while True:
        pyautogui.click(clicks=2, interval=0.5)
        time.sleep(2)
        if pyautogui.pixelMatchesColor(711, 1065, (105, 105, 105), tolerance=50):
            pyautogui.scroll(-200)
            time.sleep(3)
            if pyautogui.pixelMatchesColor(711, 1065, (105, 105, 105), tolerance=50):
                break


    data = driver.page_source  # 直接獲取頁面數據
    soup = BeautifulSoup(data, 'html.parser')  # 指定解析器

# 找到包含店家名稱的標籤

    store_tags = soup.find_all('div', {'class': 'qBF1Pd fontHeadlineSmall'})

    # If the list of elements is not empty, get the text from each element and print it
    if store_tags is not None:
        store_list = []
        for store_tag in store_tags:
            store_name = store_tag.text.strip()
            store_list.append(store_name)
        # print(store_list)
    store_all_data = []
    for i in range(len(store_list)):
        store_all_data.append([key, store_list[i],])  
            # store_list.append(",".join([key,store_name,tp]))
    with open(f'{key}_{tp}.csv', 'w', newline='', encoding='utf-8') as csvfile:
        writer = csv.writer(csvfile)
        for store in store_all_data:
            writer.writerow(store)
    csvfile.close()

driver.quit()




