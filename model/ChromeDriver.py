from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement
from selenium.common.exceptions import NoSuchElementException, ElementNotInteractableException
import time

class ChromeDriver: 
    driver = webdriver.Chrome()
    products = []
    data = []

    def __init__(self, url: str) -> None:
        self.driver.get(url)
        pass

    def findProductList(self):
        try:
            productList = self.driver.find_element(by=By.CSS_SELECTOR, value="ul.listproduct")
            return productList
        except NoSuchElementException:
            print(">>> Product List not found")
            return 
    
    def getProducts(self, productList: WebElement):
        if(not productList): return

        try:
            self.products = productList.find_elements(by=By.CSS_SELECTOR, value='li.item.__cate_1942')
            return self.products
        except NoSuchElementException:
            print(">>> Products not found")
            return 

    def clickViewMoreButton(self):
        try:
            viewMoreButton = self.driver.find_element(by=By.CSS_SELECTOR, value="div.view-more a")
            print("WHaT: ", viewMoreButton.text)

            viewMoreButton.click()
            time.sleep(0.5)
            self.clickViewMoreButton()
        except NoSuchElementException:
            print(">>> View More button not found")
            return
        except  ElementNotInteractableException:
            print(">>> Cant click view more button")
            return
        
    def getData(self, productList: WebElement):
        if(not productList): return
        try:
            products = self.getProducts(productList)
            for product in products:
                nameElement = product.find_elements(by=By.CSS_SELECTOR, value="h3")
                priceElement = product.find_elements(by=By.CSS_SELECTOR, value=".price")
                name = nameElement[0].text.strip() if len(nameElement) > 0 else ""
                price = priceElement[0].text.strip() if len(priceElement) > 0 else ""
                print(">>>>> name: ", name)
                print(">>>>> price: ", price)
            print(">>> Total products: ", len(products))
            return
        except:
            print("Error: Cannot get full data")
            return None