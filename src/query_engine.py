import os
from llama_index.core.postprocessor import MetadataReplacementPostProcessor, SentenceTransformerRerank

def get_sentence_window_query_engine(sentence_index, config):
    rerank_model_path = os.path.join(config["BASE_MODEL_DIR"], config["RERANK_MODEL_NAME"])
    postproc = MetadataReplacementPostProcessor(target_metadata_key="window")
    rerank = SentenceTransformerRerank(
        top_n=config["RERANK_TOP_N"], model=rerank_model_path
    )
    sentence_window_engine = sentence_index.as_query_engine(
        similarity_top_k=config["SIMILARITY_TOP_K"], node_postprocessors=[postproc, rerank]
    )
    return sentence_window_engine
