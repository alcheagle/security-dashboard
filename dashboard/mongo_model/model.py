from mongoengine import *

class Tool(Document):
    name = StringField(max_length=40, required=True, unique=True)
    fields = ListField(StringField(max_length=40))

class Measure(Document):
    # scrapes = ListField(MapField(ReferenceField(Tool), ListField(StringField(max_length=40)))) #NOTICEME Z says EmbeddedDocuments
    scrapes = DictField(required=True)
    date = DateTimeField(required=True)

class Domain(Document):
    url = StringField(regex='^(?!:\/\/)([a-zA-Z0-9-_]+\.)*[a-zA-Z0-9][a-zA-Z0-9-_]+\.[a-zA-Z]{2,11}?$', max_length=256, required=True, unique=True)
    disabledTools = ListField(ReferenceField(Tool))
    measures = ListField(ReferenceField(Measure))
