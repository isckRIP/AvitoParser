from selenium import webdriver
from selenium.webdriver.common.by import By
from fake_useragent import UserAgent
import time

# Create options
options = webdriver.ChromeOptions()
# Create user-agent
useragent = UserAgent()

# Add arguments for options, proxy
options.add_argument(f"user-agent={useragent.random}")
# options.add_argument("--proxy-server=80.78.248.167:3128")

# Set url
url = "https://www.avito.ru/sankt-peterburg/telefony/mobilnye_telefony/samsung-ASgBAgICAkS0wA2crzmwwQ2I_Dc?cd=1&q=samsung"

driver = webdriver.Chrome(
    executable_path=r"C:\Users\madan\PycharmProjects\AvitoParser\ChromeDriver\chromedriver.exe",
    options=options
)

try:
    driver.get(url=url)
    print(f"Currently URL is: {driver.current_url}")
    time.sleep(5)

# Finding links
    items = driver.find_elements(By.XPATH, "//h3[@itemprop='name']")
    print(items)

    items[0].click()
    time.sleep(5)
except Exception as ex:
    print(ex)
finally:
    driver.close()
    driver.quit()
