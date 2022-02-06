import wikipedia
import json
import wikipediaapi

keyword=input("keyword=")
num_url= input("no. of links=")

wiki_wiki = wikipediaapi.Wikipedia(
        language='en',
        extract_format=wikipediaapi.ExtractFormat.WIKI
)



my_file={}
for items in wikipedia.search(keyword, results= num_url):
    
    my_file[items] = wiki_wiki.page(items).summary


with open ('output.json','w') as f:
    json.dump(my_file, f, indent=4)
    
    
f = open('output.json')