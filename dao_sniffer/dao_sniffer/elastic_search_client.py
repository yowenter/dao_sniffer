from elasticsearch import Elasticsearch

from dao_sniffer.settings import ELASTIC_SEARCH_HOST, ELASTIC_SEARCH_PORT

es_client = Elasticsearch(hosts=[{"host": ELASTIC_SEARCH_HOST, "port": ELASTIC_SEARCH_PORT}])


def index_elastic_search(index, id, doc_type, item):
    es_client.index(index=index, doc_type=doc_type, id=id, body=item)
