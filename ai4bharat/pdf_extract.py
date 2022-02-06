import gdata.docs.data
import gdata.docs.client
import gdata.docs.service
import gdata.spreadsheet.service
import re, os
import json

username        = 'myemail@gmail.com'
password         = 'mypassword'
doc_name        = 'My document'

gd_client = gdata.spreadsheet.service.SpreadsheetsService()
gd_client.email = username 
gd_client.password = password  
gd_client.source = 'https://docs.google.com/spreadsheets/d/1I7hziCQGd0uKzh4RMnZtpkTspaE-1_bIL0FcGU_Y1DU/edit#gid=1169510777'
gd_client.ProgrammaticLogin()

q = gdata.spreadsheet.service.DocumentQuery()
q['title'] = doc_name
q['title-exact'] = 'true'
feed = gd_client.GetSpreadsheetsFeed(query=q)
spreadsheet_id = feed.entry[0].id.text.rsplit('/',1)[1]
feed = gd_client.GetWorksheetsFeed(spreadsheet_id)
worksheet_id = feed.entry[0].id.text.rsplit('/',1)[1]

rows = gd_client.GetListFeed(spreadsheet_id, worksheet_id).entry



urls = []
for row in rows:
    for key in row.custom:
        urls.append(row.custom[key].text)
        newlist = urls

elec_urls = newlist.strip()


with open ('output.json','w') as f:
    json.dump(newlist, f, indent=4)
    
    
f = open('output.json')
