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
            return Measure.objects(domain.measures).order_by('-date')[0]
        else:
            raise RuntimeError('domain={} doesn\'t exist'.format(domain))

    def getDomainsAndTools():
        domains = Domain.objects

        result = {}
        for domain in domains:
            result[domain.url] = [tool.name for tool in Tools.objects(domain.disabledTools)]

        return result

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

    def addMeasuresToDomain(self, domain_url, measures):
        import datetime
        domain = Domain.objects(url=domain_url)
        if domain:
            domain = domain[0]
            measures = Measure(date=datetime.datetime.now(), scrapes=escape_scrapes(measures))
            measures.save()
            return domain.update(add_to_set__measures=measures.id)
        else:
            raise RuntimeError('domain={} doesn\'t exist'.format(domain_url))

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

from pprint import pprint as pp

def escape_scrapes(scrapes):

    def change_key(d, old, new):
        d[new] = d[old]
        del d[old]

    for domain, measures in scrapes.items():
        for measure_name in measures.keys():
            new_name = measure_name.replace('.', '_').replace('$', '_')
            if measure_name != new_name:
                change_key(measures, measure_name, new_name)
    return scrapes
