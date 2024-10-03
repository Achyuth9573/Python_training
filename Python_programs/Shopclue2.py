from selenium import webdriver
import time
import os
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys

chrome_option = Options()
chrome_option.add_argument("--disable-notification")

driver = webdriver.Chrome(service=Service("C:\\Driver\\chromedriver.exe"), options=chrome_option)
driver.maximize_window()
dic2="shopclue_new2"
os.chdir('C:\\Users\\91863\\Desktop\\Python classes\\Automation')
if not os.path.exists(dic2):
    os.makedirs(dic2)

url="https://www.shopclues.com/"
driver.get(url)
time.sleep(5)

try:
    driver.find_element_by_xpath("/html/body/div[1]/div/div/div[3]/div[1]/button[1]").click()

except:
    pass
def shopclue(i):
    driver.find_element_by_id("autocomplete").send_keys(i)
    driver.find_element_by_xpath('//*[@id="search"]/a').click()
    driver.implicitly_wait(5)
    driver.find_element_by_id("det_img_153513023").click()

    tabs=driver.window_handles
    driver.implicitly_wait(5)
    driver.switch_to.window(tabs[1])
    #driver.execute_script('window.scrollTo(0,400)')
    driver.execute_script('window.scroll(0,400)')
    driver.find_element_by_id("add_cart").click()
    driver.find_element_by_xpath('/html/body/div[3]/div/div/div[4]/ul/li[4]/div/div/div[3]/a[1]').click()
    s2= dic2 + '//' + i + 'cart.png'
    driver.save_screenshot(s2)
    driver.implicitly_wait(5)


items=["Laptop"]
for i in items:
    print(i)
    shopclue(i)

driver.implicitly_wait(5)
driver.close()