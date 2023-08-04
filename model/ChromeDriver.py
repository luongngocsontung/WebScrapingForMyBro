from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement
from selenium.common.exceptions import NoSuchElementException, ElementNotInteractableException
import time

class ChromeDriver: 
    driver = webdriver.Chrome()
    products = []
    data = []

    def __init__(self, pageUrl: str, productListQuery: str, productsQuery: str, viewMoreQuery: str, fields: dict) -> None:
        self.driver.get(pageUrl)
        self.productListQuery = productListQuery
        self.productsQuery = productsQuery
        self.viewMoreQuery = viewMoreQuery
        self.fields = fields
        pass

    def findProductList(self):
        try:
            productList = self.driver.find_element(by=By.CSS_SELECTOR, value=self.productListQuery)
            return productList
        except NoSuchElementException:
            print(">>> Product List not found")
            return 
    
    def getProducts(self, productList: WebElement):
        if(not productList): return

        try:
            self.products = productList.find_elements(by=By.CSS_SELECTOR, value=self.productsQuery)
            return self.products
        except NoSuchElementException:
            print(">>> Products not found")
            return 

    def clickViewMoreButton(self):
        try:
            viewMoreButton = self.driver.find_element(by=By.CSS_SELECTOR, value=self.viewMoreQuery)
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
        except:
            print(">>> Unknown Errors")
        
    def getData(self, productList: WebElement):
        if(not productList): return
        try:
            products = self.getProducts(productList)
            data = []
            for product in products:
                values = []
                for label, query in self.fields.items():
                    fieldElement = product.find_elements(by=By.CSS_SELECTOR, value=query)
                    fieldValue = fieldElement[0].text.strip() if len(fieldElement) > 0 else ""
                    values.append(fieldValue)
                data.append(values)
            return data
        except:
            print("Error: Cannot get full data")
            return None

    def closeBrowser(self):
        self.driver.close()