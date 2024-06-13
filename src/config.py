import os
from dotenv import load_dotenv

def load_config():
    load_dotenv()
    config = {
        "LLM_MODEL": os.getenv("LLM_MODEL"),
        "LLM_REQUEST_TIMEOUT": float(os.getenv("LLM_REQUEST_TIMEOUT")),
        "LLM_BASE_URL": os.getenv("LLM_BASE_URL"),
        "INPUT_DIR": os.getenv("INPUT_DIR"),
        "ES_URL": os.getenv("ES_URL"),
        "ES_INDEX_NAME": os.getenv("ES_INDEX_NAME"),
        "ES_USER": os.getenv("ES_USER"),
        "ES_PASSWORD": os.getenv("ES_PASSWORD"),
        "BASE_MODEL_DIR": os.getenv("BASE_MODEL_DIR"),
        "MODEL_NAMES": os.getenv("MODEL_NAMES").split(','),
        "WINDOW_SIZE": int(os.getenv("WINDOW_SIZE")),
        "SIMILARITY_TOP_K": int(os.getenv("SIMILARITY_TOP_K")),
        "RERANK_TOP_N": int(os.getenv("RERANK_TOP_N")),
        "RERANK_MODEL_NAME": os.getenv("RERANK_MODEL_NAME"),
        "QUERY_QUESTION": os.getenv("QUERY_QUESTION"),
        "NUM_OUTPUT": int(os.getenv("NUM_OUTPUT")),
        "CONTEXT_WINDOW": int(os.getenv("CONTEXT_WINDOW")),
    }
    return config
