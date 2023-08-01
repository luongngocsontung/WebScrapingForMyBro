import tkinter as tk
from handleCrawlWeb import handleCrawlWeb

def handleClickCrawlButton():
    pageUrl = pageUrlInput.get()
    productListQuery = productListQueryInput.get()
    productsQuery = productsQueryInput.get()
    handleCrawlWeb(pageUrl, productListQuery, productsQuery)

# Create the main application window
app = tk.Tk()
app.title("Web Crawler Panel")
app.geometry("800x800")

# Input field for URL
tk.Label(app, text="Enter Page URL").pack()
pageUrlInput = tk.Entry(app, width=50)
pageUrlInput.pack(pady=5)

# Product List Input
tk.Label(app, text="Enter Product List Query").pack()
productListQueryInput = tk.Entry(app, width=30)
productListQueryInput.pack(pady=5)

# Products Query Input
tk.Label(app, text="Enter Products Query").pack()
productsQueryInput = tk.Entry(app, width=30)
productsQueryInput.pack(pady=5)

# Fields
# fields = app.tk()

# Crawl button
crawlButton = tk.Button(app, text="Crawl", command=handleClickCrawlButton)
crawlButton.pack(pady=10)

# Start the application main loop
app.mainloop()