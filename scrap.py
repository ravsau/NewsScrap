from bs4 import BeautifulSoup


import requests



result=requests.get('http://www.ekantipur.com//',timeout=2)

c=result.content



#print(source.data)

soup=BeautifulSoup(c,'html.parser')



headlines=[]
for text in soup.find_all('h1'):
	a=text.text
	

	if len(a.split())>3:

        
		
		headlines.append(text.text)


for i in headlines:
	print (i[5])





