import aiohttp
from llama_index.llms.ollama import Ollama

async def initialize_llm(config):
    session = aiohttp.ClientSession()
    llm = Ollama(
        model=config["LLM_MODEL"],
        request_timeout=config["LLM_REQUEST_TIMEOUT"],
        base_url=config["LLM_BASE_URL"],
        session=session
    )
    return llm, session

async def close_llm_session(session):
    if not session.closed:
        await session.close()
