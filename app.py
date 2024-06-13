import logging
import asyncio
from src.config import load_config
from src.data_loader import load_and_prepare_document
from src.llm_initializer import initialize_llm, close_llm_session
from src.vector_store import configure_vector_store
from src.sentence_index import build_sentence_window_index
from src.query_engine import get_sentence_window_query_engine

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

async def main():
    session = None
    try:
        # Load configuration
        config = load_config()

        # Initialize the LLM
        llm, session = await initialize_llm(config)

        # Load and prepare the document
        document = load_and_prepare_document(config)

        # Configure the Elasticsearch vector store
        vector_store = configure_vector_store(config)

        # Build the sentence window index
        sentence_index = build_sentence_window_index(document, vector_store, config, llm)

        # Get the query engine
        query_engine = get_sentence_window_query_engine(sentence_index, config)

        # Query the engine and print the result
        query_result = query_engine.query(config["QUERY_QUESTION"])
        logger.info(f"Query result: {query_result}")

    except Exception as e:
        logger.error(f"An error occurred: {e}")

    finally:
        if session:
            await close_llm_session(session)

if __name__ == "__main__":
    asyncio.run(main())
