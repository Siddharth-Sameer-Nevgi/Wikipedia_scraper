import requests
from bs4 import BeautifulSoup
def dataExtractWikipedia(userText):
    try:
        link="https://en.wikipedia.org/wiki/"+userText
        r=requests.get(link)
        content=r.text
        html_content=BeautifulSoup(content,'html.parser')
        head=html_content.find('span',{'class':"mw-page-title-main"})
        print(head.get_text())
        l=html_content.find_all('p')
        for i in range(len(l)):
            print(l[i].get_text())
    except:
        print('An error occured. Please try again!!!')
text=input("Enter the text which u wish to search for in wikipedia:")
text=text.replace(' ','_')
dataExtractWikipedia(text)
