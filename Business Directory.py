# url http://businessdirectory.pk

import requests
import pandas as pd
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import os

from selenium.webdriver.support.ui import WebDriverWait
weburl = "http://businessdirectory.pk/"


driver = webdriver.Chrome("chromedriver.exe")
driver.minimize_window()
driver.get(weburl)
# soup = BeautifulSoup(htmlcontent, 'html.parser')

Main_Fields = ["Advertising & Marketing", "Agriculture", "Heating, Ventilation & Air Conditioning",
                     "Animals, Birds, Pets & Live stocks", "Clothing & Fashion", "Architects & Planners",
                     "Associations and NGOs", "Automobiles & Vehicles", "Banking & Financing",
                     "Books, Publications & Libraries",
                     "Building Materials", "Business Services Provider", "Business Services Provider", "Call Centre's",
                     "Dyes & Chemicals",
                     "Dyes & Chemicals", "Commodities & Merchandiser", "Computers & IT", "Construction & Real Estate",
                     "Consultants & Advisers",
                     "Retail Shops & Departmental Stores", "Designers & Decorators", "Detergents & Soaps",
                     "Education & Training Centre", "Electronics & Electrical Products",
                     "Energy & Utilities Products", "Engineering Section", "Fun, Entertainment & Hobbies",
                     "Environmental Services", "Events Planner", "Personal Care & Fitness Centre",
                     "Personal Care & Fitness Centre",
                     "Food & Beverage Products", "Food Processing Machinery", "Footwear Products & Services",
                     "Fruits & Vegetable Products", "Geo Equipment & Services", "Gifts Shops & Toys",
                     "Glass, Earthenware & Clay", "Government Sector", "Handicrafts", "Handicrafts", "Hardware & Tools",
                     "Health and Medical", "Home Appliances & Accessories",
                     "Home Supplies", "Horticulture & Gardening", "Hotels, Clubs & Food Parlors",
                     "Industrial Machinery & Equipments", "Insurance Companies", "Jewelers", "Leather and Tanneries",
                     "Metals, Minerals & Mining", "Miscellaneous", "Office Equipments & Supplies", "Oil, Gas & Fuel",
                     "Packaging & Paper",
                     "Pipes & Fittings", "Plastics & Polymers", "Postal & Courier Services", "Power & Generators",
                     "Printing & Publishing", "Professional Services", "Radio, TV & Multimedia",
                     "Religion & Belief", "Road Safety & Traffic", "Security & Safety", "Shares & Stock Brokers",
                     "Shipping Companies",
                     "Social Services", "Sports & Games", "Stone & Marble", "Telecommunication", "Textiles",
                     "Tourism & Travel Agent", "Transport & Logistics", "Watches & Clocks",
                     "Water & Water Purification", "Poultry", "Baby Products", "Rice", "Hair Products & Services",
                     "Herbs & Others", "Bakers, Sweets & Confectioners", "Embroidery & Crafts Textile", "Batteries",
                     "Chains", "Industrial Safety Equipment", "Sugar Mill Machinery & Parts", "Photocopy",
                     "Petroleum & Products", "Mobile Phones", "Mobile Phones", "Knitting", "Wool",
                     "Packing and Crating"]
print("before",driver.current_url)
# print("after",driver.current_url)
url_list =[]
internal_pages_url_list =[]
ind = 0
url_list_company =[]
for index,fld in enumerate(Main_Fields):

    driver.find_element(By.LINK_TEXT, Main_Fields[ind]).click()
    # finding the internal data in site

    r = requests.get(driver.current_url)
    htmlcontent = r.content
    soup=BeautifulSoup(htmlcontent,"html.parser")

    for a in soup.find_all('a', class_="link10"):
        url_list.append(weburl+a['href'])


    # finding links in links above stored
    for i,curr_page in enumerate(url_list):
        r = requests.get(curr_page)
        htmlcontent = r.content
        soup = BeautifulSoup(htmlcontent, "html.parser")
        for a in soup.find_all('a', class_="link11"):
            internal_pages_url_list.append(weburl + a['href'])


    for local_link in url_list:
        r = requests.get(local_link)
        htmlcontent = r.content
        soup = BeautifulSoup(htmlcontent, "html.parser")
        for a in soup.find_all('a', class_="link11"):
            url_list_company.append(weburl + a['href'])
    # print(url_list_company)
    aa = []
    for i in url_list_company:
        try:
            print(i)
            r = requests.get(i)
            htmlcontent = r.content
            soup = BeautifulSoup(htmlcontent, "html.parser")
            company_name = soup.find_all("div",{"class":"box-text no-img"})
            z=([i.text for i in company_name])
            print(z)
            print(len(z))
            print("up to df")
            df = pd.DataFrame({
                "Field":[fld],
                "Data":[i for i in z]
            })
            print("low to df")
            df.to_csv("pakistan.csv",mode='a',index=False)
            print("write done")
            
            
            
   # there are some validations below , if you want to apply them, then make shower to apply certain changes according to your requirments.
            
            # x = [i.replace("Address", "||").replace("Email", "||").replace('Phone', "||") for i in z]
            # data = [i.split("||") for i in x]
            # print(data[0])
            # for k in data[0]:
            #     print(data[k])

            # print(fld)
            # print(len(data))

            # print((data[0][0]))
            # print((data[0][1]))
            # print((data[0][2]))
            # print((data[0][3]))

        except:
            pass
        # print(aa)
        # print(company_name)
    # print([i.text for i in company_name])
    # print(aa)

        # print("this is internal  url list",internal_pages_url_list)
        # i=0
        # for internal in internal_pages_url_list:
        #     print(internal)
        #     r = requests.get(internal)
        #     htmlcontent = r.content
        #     soup = BeautifulSoup(htmlcontent, "html.parser")
        #     text =soup.find_all("div",{'class':"box-text no-img"})
        #     text1=[i for i in text]
        #     print(i)
        #     driver.get(internal_pages_url_list[i+1])
            # print(internal)
            # print(text1)




            # final_data =soup.find_all("div",{"class":"box-text no-img"})
            # results = [i.text for i in final_data]

    # i=0
    # for inter_url in internal_pages_url_list:
    #     r = requests.get(inter_url)
    #     htmlcontent = r.content
    #     soup = BeautifulSoup(htmlcontent, "html.parser")
    #     text =soup.find_all("div",{'class':"box-text no-img"})
    #     text1=[i for i in text]
    #     print(text1)
    #     i+=1
    #     print(i)
        # final_data =soup.find_all("div",{"class":"box-text no-img"})
        # results = [i.text for i in final_data]

    print("changed globally")
    driver.get(weburl)

    ind+=1
    # driver.get(weburl)
