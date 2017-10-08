from mongoengine import *
from .model import *


MONGO_URL = 'mongodb'
MONGO_DATABASE = 'measures'

class Database:

    def __init__(self, database, url):
        self.client = connect(database, host=url)
    def getLastDomainScan(self, domain):
        domain = Domain.objects(url=domain)
        if domain:
            domain = domain[0]

            #TODO find the measures with the highest date
            # domain.measures.
        else:
            raise RuntimeError('domain={} doesn\'t exist'.format(domain))

    def saveScan(self, scan):
        for domain, measures in scan.items():
            self.addMeasuresToDomain(domain, measures)

    def createTools(self, tools):
        mongo_tools = []

        for name, fields in tools.items():
            t = Tool(name=name, fields=fields)
            mongo_tools.append(t.save())

        return mongo_tools

    def createDomains(self, domains):
        mongo_domains = []

        for domain in domains:
            d = Domain(url=domain, )

            mongo_domains.append(d.save())

        return mongo_domains

    def addMeasuresToDomain(self, domain, measures):
        import datetime
        domain = Domain.objects(url=domain)
        if domain:
            domain = domain[0]
            measures = Measure(date=datetime.datetime.now(), measures=measures)
            measures.save()
            return domain.update(add_to_set__measures=measures.id)
        else:
            raise RuntimeError('domain={} doesn\'t exist'.format(domain))

    def addDisabledTools(self, domain, tools):
        domain = Domain.objects(url=domain)
        if domain:
            domain = domain[0]

            tools_ids = Tool.objects(name__in=tools)

            if tools:
                return domain.update(add_to_set__disabledTools=tools_ids)
        else:
            raise RuntimeError('domain={} doesn\'t exist'.format(domain))

database = Database(MONGO_DATABASE, MONGO_URL)
