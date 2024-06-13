import os
from llama_index.core import VectorStoreIndex, StorageContext
from llama_index.core import Settings
from llama_index.core.node_parser import SentenceWindowNodeParser

def build_sentence_window_index(document, vector_store, config, llm):
    embed_model_path = "local:" + os.path.join(config["BASE_MODEL_DIR"], config["MODEL_NAMES"][0])
    Settings.llm = llm
    Settings.embed_model = embed_model_path
    Settings.node_parser = SentenceWindowNodeParser.from_defaults(
        window_size=config["WINDOW_SIZE"],
        window_metadata_key="window",
        original_text_metadata_key="original_text",
    )
    Settings.num_output = config["NUM_OUTPUT"]
    Settings.context_window = config["CONTEXT_WINDOW"]

    storage_context = StorageContext.from_defaults(vector_store=vector_store)
    sentence_index = VectorStoreIndex.from_documents(
        [document], storage_context=storage_context
    )
    return sentence_index
