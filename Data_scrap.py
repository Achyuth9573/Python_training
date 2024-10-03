# from bs4 import BeautifulSoup
# import requests
# import pandas as pd
#
# url="https://www.snapdeal.com/search?keyword=shoes&santizedKeyword=&catId=&categoryId=0&suggested=false&vertical=p&noOfResults=20&searchState=&clickSrc=go_header&lastKeyword=&prodCatId=&changeBackToAll=false&foundInAll=false&categoryIdSearched=&cityPageUrl=&categoryUrl=&url=&utmContent=&dealDetail=&sort=rlvncy&q=Color_s%3ABlue%7CSize_s%3A11%7CPrice%3A189%2C493%7C"
#
# x=requests.get(url)
# print(x)
# em=[]
# #ep=[]
# new=BeautifulSoup(x.content,'html.parser')
# name=new.find_all("p",class_='product-title')
# name=new.find_all("div",class_='product-price-row clearfix')
#
# for n in name:
#     shoes=n.text
#     em.append(shoes)
#
# df=pd.DataFrame({'shoes name and price':em})
# #df1=pd.DataFrame({'price':ep})
# print(df)
# # print(df1)
# df.to_excel('C:\\Users\\91863\\Desktop\\Python classes\\Automation\\shoes.xlsx')
#
# ##string-->list---->dataframe---->export data### format to convert from tag to excel




from bs4 import BeautifulSoup
import requests
import pandas as pd
url='https://www.snapdeal.com/search?keyword=shoes&santizedKeyword=&catId=&categoryId=0&suggested=false&vertical=p&noOfResults=20&searchState=&clickSrc=go_header&lastKeyword=&prodCatId=&changeBackToAll=false&foundInAll=false&categoryIdSearched=&cityPageUrl=&categoryUrl=&url=&utmContent=&dealDetail=&sort=rlvncy&q=Color_s%3ABlue%7CSize_s%3A11%7CPrice%3A189%2C493%7C'

x=requests.get(url)
em=[]
pr=[]
of=[]
new=BeautifulSoup(x.content,'html.parser')
name=new.find_all("p",class_='product-title')
p_name=new.find_all("span",class_='lfloat product-price')
of_name=new.find_all("div",class_='product-discount')
for n in name:
    shoes=n.text
    em.append(shoes)
for p in p_name:
    pp=p.text
    pp=pp.replace('Rs.','').strip()
    pr.append(pp)
for o in of_name:
    ofp=o.text
    ofp=ofp.replace('Off','').strip()
    #print(ofp)
    of.append(ofp)
df=pd.DataFrame({'shoes name':em,'shoes price':pr,'offer price':of})
print(df)
df.to_excel('C:\\Users\\91863\\Desktop\\Python classes\\Automation\\shoes1.xlsx')