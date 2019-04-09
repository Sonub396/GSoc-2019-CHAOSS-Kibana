from elasticsearch import Elasticsearch, helpers
import os,sys, json

es = Elasticsearch()

filepath = os.getcwd() + '/sample2.json'

with open(filepath, 'r') as new_file:
    data = json.load(new_file)

def load():
    for x in data:
        yield x

helpers.bulk(es, load(), index='git_timezones', doc_type='item_new')