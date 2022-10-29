from selenium import webdriver
import time
import fake_useragent

url = "https://www.avito.ru/sankt-peterburg/telefony/mobilnye_telefony/samsung-ASgBAgICAkS0wA2crzmwwQ2I_Dc?cd=1&q=samsung"
driver = webdriver.Chrome(executable_path="C:\\Users\\madan\\PycharmProjects\\AvitoParser\\ChromeDriver\\chromedriver.exe")

try:
    driver.get(url=url)
    time.sleep(5)
except Exception as ex:
    print(ex)
finally:
    driver.close()
    driver.quit()
