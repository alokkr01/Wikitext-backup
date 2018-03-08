from bs4 import BeautifulSoup
import requests 

def WikiTextScp(page_url,wiki_title):

	r = requests.get(page_url)
	temp = r.content
	# print(r.text)
	# print(temp)

	soup = BeautifulSoup(temp, "html.parser")

		# 	# print(soup.title)
		# wiki_Title = soup.find('title').contents[0]
		# 	# print(wiki_Title)
		# wiki_title = wiki_Title
		# wiki_title =wiki_title.strip('View source Satellite Wiki') 
		# wiki_title =wiki_title.strip('for -')

	wiki_Text = soup.find('textarea').contents[0]	# print(wikiText)

	file_format = '.txt'	# [fn])() ; !!What other formats can be supported
	file_name = wiki_title + file_format
	print(file_name)

	with open(file_name, 'w') as file:
	   file.write(wiki_Text)   
	# with open("Output.txt", "w") as text_file:
	#     print(wikiT, file=text_file)


