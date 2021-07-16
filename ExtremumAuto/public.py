
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common import keys
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.window import WindowTypes
from selenium.webdriver.support import expected_conditions as EC
import time 


options = Options()

options.binary_location = "C:\Program Files (x86)\Google\Chrome Beta\Application\chrome.exe"
options.add_experimental_option("excludeSwitches", ['enable-logging'])


driver = webdriver.Chrome(chrome_options=options)

### STEAM SESSION

u = (input("Enter SteamID: "))
p = (input("Enter Password: "))
driver.get('https://store.steampowered.com/')
login = driver.find_element(By.XPATH, '//*[@id="global_action_menu"]/a')
login.click()

username = driver.find_element(By.XPATH, '//*[@id="input_username"]')
username.send_keys(u)

password = driver.find_element(By.XPATH, '//*[@id="input_password"]')
password.send_keys(p)

signin = driver.find_element(By.XPATH, '//*[@id="login_btn_signin"]/button')
signin.click()
a = (input("Enter 2fa: "))
twofa = driver.find_element(By.XPATH, '//*[@id="twofactorcode_entry"]')
twofa.send_keys(a.upper())
submit = driver.find_element(By.XPATH, '//*[@id="login_twofactorauth_buttonset_entercode"]/div[1]')
submit.click()

### EXTREMUM SESSION

driver.switch_to.new_window(WindowTypes.TAB)

driver.get('https://pass.extremum.gg/')

acceptcookies = driver.find_element(By.XPATH, '//*[@id="__layout"]/div/div/div[2]/button')
acceptcookies.click()

join = driver.find_element(By.XPATH, '//*[@id="__layout"]/div/main/div/header/div/button')
join.click()

steam = driver.find_element(By.XPATH, '/html/body/div[2]/div[1]/div/div/div/div/div/div[2]/div[3]/div[3]')
steam.click()
driver.implicitly_wait(8)
verify = driver.find_element(By.XPATH, '/html/body/div[1]/div[7]/div[2]/div/div[2]/div[2]/div/form/input[5]')
verify.click()

### PROMOCODE AUTOMATION

driver.implicitly_wait(15)
code = driver.find_element(By.XPATH, '//*[@id="__layout"]/div/aside/div/nav/div[2]/div[1]/button')
code.click()

'''activation = driver.find_element(By.XPATH, '//*[@id="__layout"]/div/aside/div/div[1]/section[1]/div[1]/div/div/form/div[2]/div/span')'''
'''activation = driver.find_element(By.CLASS_NAME, '_2XSegYKb _3vgUEpYt _2duksfor')'''
promocode = driver.find_element(By.XPATH, '//*[@id="__layout"]/div/aside/div/div[1]/section[1]/div[1]/div/div/form/div/input')
activatecode = driver.find_element(By.XPATH, '//*[@id="__layout"]/div/aside/div/div[1]/section[1]/div[1]/div/div/form/button')

x = 0

list = open("list2.txt", "r")
list = list.read().split('\n')
text = "Activation is blocked. Too many requests"

for x in range(len(list)):
    promocode.send_keys(list[x])
    activatecode.click()
    promocode.send_keys(Keys.LEFT_CONTROL + 'a')
    errorreason = "Activation is blocked. Too many requests"
    print (list[x])
    time.sleep(2)
    if driver.find_element(By.XPATH, '/html/body/div[1]/div/div/aside/div/div[1]/section[1]/div[1]/div/div/form/div[2]/div/span').is_displayed() and errorreason in driver.page_source:
        print (list[x] + ' was blocked')
        time.sleep(180)
        x = x - 1
    else:
        promocode.click()
        promocode.send_keys(Keys.LEFT_CONTROL + 'a')
        time.sleep(5)
        x = x + 1