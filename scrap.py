from bs4 import BeautifulSoup


import requests

result=requests.get('http://www.ekantipur.com//',timeout=2)

c=result.content



#print(source.data)

soup=BeautifulSoup(c,'html.parser')



headlines=[]
for text in soup.find_all('h1'):
	a=text.text
	

	if len(a.split())>4:

        
		
		headlines.append(text.text)
#setting counter to display only 20 headlines
a=1
for i in headlines:
	if a<=20:
		print (i)
		print("")
		a=a+1


	





