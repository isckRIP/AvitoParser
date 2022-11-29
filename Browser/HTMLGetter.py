from selenium import webdriver
from fake_useragent import UserAgent
from Browser.PageParser import PageParser
import time
from selenium.webdriver.common.by import By


class HtmlGetter:
    """Получение исходного кода страницы"""

    def __init__(self, url):
        self.url = url
        self.source = ""

    def html_getting(self):
        # Create options
        options = webdriver.ChromeOptions()
        # Create user-agent
        useragent = UserAgent()
        # Add arguments for options, proxy
        options.add_argument(f"user-agent={useragent.random}")
        # options.add_argument("--proxy-server=80.78.248.167:3128")
        driver = webdriver.Chrome(
            executable_path=r"C:\Users\madan\PycharmProjects\AvitoParser\ChromeDriver\chromedriver.exe",
            options=options
        )
        #Create parser
        parser = PageParser()

        try:
            driver.get(url=self.url)

            # Logging
            logging_button = driver.find_element(By.XPATH, "/html/body/div[1]/header/div[1]/div/div[3]/a[2]")
            logging_button.click()
            mail = driver.find_element(By.XPATH, "/html/body/div[1]/div[1]/div/div/div[2]/div[2]/form/div[1]/input")
            mail.send_keys("ma.danilovv@yandex.ru")
            password = driver.find_element(By.XPATH, "/html/body/div[1]/div[1]/div/div/div[2]/div[2]/form/div[2]/input")
            password.send_keys("makson67D")
            logging_button = driver.find_element(By.XPATH, "/html/body/div[1]/div[1]/div/div/div[2]/div[2]/form/button")
            logging_button.click()
            time.sleep(100)

            print(f"Currently URL is: {driver.current_url}")

            # Finding links
            items = driver.find_elements(By.XPATH, "//a[@class='snippet__title-link link']")
            for item in items:
                item.click()
                time.sleep(5)
                contact_button = driver.find_elements(By.XPATH, "/html/body/div[1]/main/div/div[2]/div/div/div[4]/div[1]/ul/li[1]/a")
                print(contact_button)
                print(f"Currently URL is: {driver.current_url}")
                parser.BS(driver.page_source)

            print(f"Currently URL is: {driver.current_url}")
            print(items)
        except Exception as ex:
            print(ex)
        finally:
            driver.close()
            driver.quit()
