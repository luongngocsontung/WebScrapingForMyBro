import tkinter as tk
from handleCrawlWeb import handleCrawlWeb

def handleAddField():
    newFieldEntry = tk.Frame(fieldListEntry)
    fieldEntry.append(newFieldEntry)
    newFieldEntry.pack()
    tk.Label(newFieldEntry, text="Fields").pack(side='left')
    newFieldLabel = tk.Entry(newFieldEntry, width=15)
    newFieldLabel.pack(pady=5, side='left')
    fieldsLabelInput.append(newFieldLabel)
    tk.Label(newFieldEntry, text="Enter Field Query").pack(side='left')
    newFieldQuery = tk.Entry(newFieldEntry, width=15)
    newFieldQuery.pack(pady=5, side='left')
    fieldsQueryInput.append(newFieldQuery)

    # Update the scroll region to make the canvas scrollable
    scrollable_frame.update_idletasks()
    canvas.config(scrollregion=canvas.bbox("all"))

def handleRemoveField():
    if(len(fieldEntry) == 1): return
    
    fieldEntry.pop().destroy()    
    fieldsLabelInput.pop()
    fieldsQueryInput.pop()

def handleClickCrawlButton():
    pageUrl = pageUrlInput.get()
    productListQuery = productListQueryInput.get()
    productsQuery = productsQueryInput.get()
    viewMoreQuery = viewMoreInput.get()
    fields = {}
    for fieldLabel, fieldQuery in zip(fieldsLabelInput, fieldsQueryInput):
        label = fieldLabel.get()
        query = fieldQuery.get()
        if(label and query):
            fields[label] = query
    handleCrawlWeb(pageUrl, productListQuery, productsQuery, viewMoreQuery, fields)

# Create the main application window
app = tk.Tk()
app.title("Web Crawler Panel")
app.geometry("800x800")

def on_mousewheel(event):
    if event.num == 5 or event.delta == -120:
        canvas.yview_scroll(1, "units")
    if event.num == 4 or event.delta == 120:
        canvas.yview_scroll(-1, "units")


def on_touchpad_scroll_up(event):
    canvas.yview_scroll(-1, "units")

def on_touchpad_scroll_down(event):
    canvas.yview_scroll(1, "units")

# Create a Canvas widget and configure it for scrolling
canvas = tk.Canvas(app)
canvas.pack(side=tk.LEFT, fill=tk.BOTH, expand=True, padx=50)

# Create a Vertical Scrollbar and attach it to the Canvas
scrollbar = tk.Scrollbar(app, command=canvas.yview)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

canvas.config(yscrollcommand=scrollbar.set)

# Create a Frame to hold the widgets that will be scrollable
scrollable_frame = tk.Frame(canvas)
canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")

# Input field for URL
tk.Label(scrollable_frame, text="Enter Page URL").pack()
pageUrlInput = tk.Entry(scrollable_frame, width=50)
pageUrlInput.pack(pady=5)

# Product List Input
tk.Label(scrollable_frame, text="Enter Product List Query").pack()
productListQueryInput = tk.Entry(scrollable_frame, width=30)
productListQueryInput.pack(pady=5)

# Products Query Input
tk.Label(scrollable_frame, text="Enter Products Query").pack()
productsQueryInput = tk.Entry(scrollable_frame, width=30)
productsQueryInput.pack(pady=5)

# View More Button Query Input
tk.Label(scrollable_frame, text="Enter View More Button Query if have").pack()
viewMoreInput = tk.Entry(scrollable_frame, width=30)
viewMoreInput.pack(pady=5)

# Fields
fieldListEntry = tk.Frame(scrollable_frame)
fieldListEntry.pack()
fieldEntry = [tk.Frame(fieldListEntry)]
# Create default Field
fieldsLabelInput = [tk.Entry(fieldEntry[0], width=15)]
fieldsQueryInput = [tk.Entry(fieldEntry[0], width=15)]
# Show Fields inputs
for index, label in enumerate(fieldsLabelInput):
    newFieldEntry = fieldEntry[index]
    newFieldEntry.pack()
    tk.Label(newFieldEntry, text="Fields").pack(side='left')
    label.pack(pady=5, side='left')
    tk.Label(newFieldEntry, text="Enter Field Query").pack(side='left')
    fieldsQueryInput[index].pack(pady=5, side='left')

# Add Field Button
addFieldButton = tk.Button(scrollable_frame, text="Add Field", command=handleAddField)
addFieldButton.pack(pady=10)

# Add Field Button
addFieldButton = tk.Button(scrollable_frame, text="Remove Field", command=handleRemoveField)
addFieldButton.pack(pady=10)

# Crawl button
crawlButton = tk.Button(scrollable_frame, text="Crawl", command=handleClickCrawlButton)
crawlButton.pack(pady=10)

# Bind mousewheel and touchpad scrolling events to enable scrolling
canvas.bind_all("<MouseWheel>", on_mousewheel)
canvas.bind_all("<Button-4>", on_touchpad_scroll_up)
canvas.bind_all("<Button-5>", on_touchpad_scroll_down)

# Start the application main loop
app.mainloop()