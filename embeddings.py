from langchain_openai import OpenAIEmbeddings
import os
from dotenv import load_dotenv
from langchain_community.embeddings import OllamaEmbeddings

load_dotenv()
openai_api_key = os.environ["OPENAI_API_KEY"]

def get_embeddings():
    embeddings = OpenAIEmbeddings(
        model = "text-embedding-3-small",
    )
    # embeddings = OllamaEmbeddings(model = "nomic-embed-text")
    return embeddings