from llama_index.core import SimpleDirectoryReader, Document

def load_and_prepare_document(config):
    reader = SimpleDirectoryReader(input_dir=config["INPUT_DIR"])
    docs = reader.load_data()
    document = Document(text="\n\n".join([doc.text for doc in docs]))
    return document
