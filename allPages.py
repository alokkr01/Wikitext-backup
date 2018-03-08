from bs4 import BeautifulSoup
import requests 


baseWiki_url = 'https://wncc-iitb.org/wiki/index.php' #Enter baseURL of wiki to be parsed...
action_url= '&action=edit'

allPages_url = baseWiki_url + '/Special:AllPages'

r = requests.get(allPages_url) 		# print(r.text)
temp = r.content					# print(temp)


soup = BeautifulSoup(temp, "html.parser")
wiki_Text= soup.find_all('ul', {'class': 'mw-allpages-chunk'})

global index ;global title_url ;global wiki_title;global wiki_file
index =0 ;title_url =[] ;wiki_title =[] ;wiki_file=[];page_url=[];

for ultag in wiki_Text:
    for litag in ultag.find_all('li'):
    	wiki_title.append(litag.text)
    	wiki_file.append(litag.text.replace(" " , "_" ))
    	title_url.append('?title='+litag.text.replace(" " , "_" ).replace("?" ,"%3F"))	
    	##Other symbols(like '+'etc) needed to be replaced too
    	index= index+1       
# print(wiki_title[0:index])
# print(title_url[0:index]) 

for i in range(0,index):
	page_url.append(baseWiki_url+str(title_url[i]) +action_url)
# print(page_url[0:index])
print("Total number of pages =" + str(index))


import wikiText
for i in range(0,index):
	wikiText.WikiTextScp(page_url[i],wiki_file[i])
