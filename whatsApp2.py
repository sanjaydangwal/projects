import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

# jokes = ["You don't need a parachute to go skydiving. You need a parachute to go skydiving twice.",
#         "Women call me ugly until they find out how much money I make. They they call me ugly and poor."]

lines = None

with open("jokes2.txt","r",encoding="utf8") as file:
    lines = tuple(file.readlines())

options = Options()
options.add_argument("--user-data-dir=chrome-data")
options.add_experimental_option("excludeSwitches", ["enable-automation"])
options.add_experimental_option('useAutomationExtension', False)

# driver = webdriver.Chrome('C:\\Users\\sanja\\Downloads\\chromedriver_win32\\chromedriver.exe', options=options)
# driver.maximize_window()
driver = webdriver.Chrome(executable_path='C:\\Users\\sanja\\Downloads\\chromedriver_win32\\chromedriver.exe')
driver.get('https://web.whatsapp.com')  # Already authenticated

time.sleep(20)
# print(lines)
##################### Provide Recepient Name Here ###############################
driver.find_element_by_xpath("//*[@title='Abhishek Semwal']").click()

for i in lines:
    i = i.replace("\n", "")
    driver.find_element_by_xpath('//*[@id="main"]/footer/div[1]/div[2]/div/div[2]').send_keys(i)
    driver.find_element_by_xpath('//*[@id="main"]/footer/div[1]/div[3]/button/span').click()
    time.sleep(3)

# for i in range(100):
#     driver.find_element_by_xpath('//*[@id="main"]/footer/div[1]/div[2]/div/div[2]').send_keys(f"{i+1} message out of 100")
#     driver.find_element_by_xpath('//*[@id="main"]/footer/div[1]/div[3]/button/span').click()
#     time.sleep(3)

time.sleep(30)
driver.close()