import pandas as pd
import requests
from bs4 import BeautifulSoup

Product_name = [] 
Specifications = [] 
Ratings = [] 
Selling_Price = [] 
Original_Price = [] 

for i in range(1,12):
    url = "https://www.flipkart.com/search?q=mobiles&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=on&as=off&page=" + str(i)

    r = requests.get(url)
    # print(r) <Responce[200]>

    soup = BeautifulSoup(r.text, "lxml")
    box = soup.find("div", class_="DOjaWF gdgoEp")
    # print(soup)

    names = box.find_all("div", class_="KzDlHZ")
    for a in names:
        name = a.text
        Product_name.append(name)

    specifications = box.find_all("li", class_="J+igdf")
    for a in specifications:
        specification = a.text
        Specifications.append(specification)

    ratings = box.find_all("ul", class_="XQDdHH")
    for a in ratings:
        rating = a.text
        Ratings.append(rating)

    selling_prices = box.find_all("div", class_="Nx9bqj _4b5DiR")
    for a in selling_prices:
        selling_price = a.text
        Selling_Price.append(selling_price)

    original_prices = box.find_all("div", class_="yRaY8j ZYYwLA")
    for a in original_prices:
        original_price = a.text
        Selling_Price.append(selling_price)   

    df = pd.DataFrame({"Product Name":Product_name,"Specifications":Specifications,"Ratings":Ratings,"Selling Prices":Selling_Price, "Original Price":Original_Price})
    print(df)

    df.to_csv("Flipkart_Mobiles_Data.csv")