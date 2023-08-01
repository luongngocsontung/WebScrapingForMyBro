from model.ChromeDriver import ChromeDriver
from scrapy.crawler import CrawlerProcess

USER_AGENT = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36'

def handleCrawlWeb(pageUrl = 'https://www.dienmayxanh.com/tivi', productListQuery = '', productsQuery = ''):
    chromeBrowser = ChromeDriver('https://www.dienmayxanh.com/tivi')
    productList = chromeBrowser.findProductList()
    chromeBrowser.clickViewMoreButton()
    data = chromeBrowser.getData(productList)

handleCrawlWeb('', '', '')