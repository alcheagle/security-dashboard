from mongo_model import database as db
import json

database = db.database

tools = json.load(open('tools.json', 'r'))
mega = json.load(open('MEGA.json', 'r'))
domains = [x for x in open('domains.txt', 'r')]

database.createTools(tools)
database.createDomains(domains)
database.saveScan(mega)
