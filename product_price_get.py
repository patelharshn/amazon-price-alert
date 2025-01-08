import requests
from bs4 import BeautifulSoup

import smtplib
from email.message import EmailMessage

URL = input("Enter product link : ")
taget_price = int(input("Enter target price : "))
new_price = 0

email_add = "hp004086@gmail.com"
psw = "YOUR_APP_PASSWORD" # App Password


headers = {
    "user-Agent" : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:133.0) Gecko/20100101 Firefox/133.0'
}

def get_price():
    global new_price 
    try:
        page = requests.get(URL,headers=headers)
        if page.status_code == 200:
            soup = BeautifulSoup(page.content,'html.parser')

            title = soup.find(class_ = "a-size-large product-title-word-break").get_text().strip()
            price = int(soup.find(class_="a-price-whole").get_text().replace(",","").replace(".",""))

            print("Title is : ",title)
            print("Price : ",price)
            new_price = price

            if(price <= taget_price):
                send_email()
                print("Mail sent success")
        else:
            print("Failed to retrieve the webpage. Status code:", page.status_code)
    except TypeError:
        print("Please enter valid input...")

def send_email():
    msg = EmailMessage()
    msg['Subject'] = "Product Price fell down"
    msg['From'] = email_add
    msg['To'] = "extraharsh7788@gmail.com"
    msg.set_content(f"Hey, \nTarget Price : {taget_price} \nNew Price : {new_price} \n Check : {URL}")

    with smtplib.SMTP_SSL('smtp.gmail.com',465) as smtp:
        smtp.login(email_add,psw)
        smtp.send_message(msg)

if __name__ == "__main__":
    get_price()
