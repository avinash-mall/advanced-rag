from llama_index.vector_stores.elasticsearch import ElasticsearchStore

def configure_vector_store(config):
    vector_store = ElasticsearchStore(
        es_url=config["ES_URL"],
        index_name=config["ES_INDEX_NAME"],
        es_user=config["ES_USER"],
        es_password=config["ES_PASSWORD"]
    )
    return vector_store
