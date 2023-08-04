import pandas as pd

USER_AGENT = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36'

def handleCrawlWeb(pageUrl: str, productListQuery: str, productsQuery: str, viewMoreQuery: str, fields: dict):
    from model.ChromeDriver import ChromeDriver
    # chromeBrowser = ChromeDriver('https://www.dienmayxanh.com/tivi', '.listproduct', '.item.__cate_1942', '.view-more', fields)
    chromeBrowser = ChromeDriver(pageUrl, productListQuery, productsQuery, viewMoreQuery, fields)
    productList = chromeBrowser.findProductList()
    # if(viewMoreQuery):
    chromeBrowser.clickViewMoreButton()
    data = chromeBrowser.getData(productList)
    columnName = list(fields.keys())
    dataPd = pd.DataFrame(data, columns=columnName)
    print(">>>>> First 5 Products")
    print(dataPd.head())
    dataPd.to_csv('output.csv', index=False)
    chromeBrowser.closeBrowser()