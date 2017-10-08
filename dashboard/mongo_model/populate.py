from . import database
import json

tools = json.load(open('tools.json', 'r'))
mega = json.load(open('MEGA.json', 'r'))
domains = [x for x in open('omains.txt', 'r')]

database.createTools(tools)
database.createDomains(domains)
database.saveScan(mega)
