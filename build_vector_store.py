from dotenv import load_dotenv
load_dotenv()

from langchain_openai import OpenAIEmbeddings
from langchain_community.vectorstores import FAISS
from langchain_community.document_loaders import TextLoader

# Load restaurant knowledge base
loader = TextLoader("restaurant_data.txt")
documents = loader.load()

# Generate and store vector embeddings
embeddings = OpenAIEmbeddings()
vectorstore = FAISS.from_documents(documents, embeddings)
vectorstore.save_local("restaurant_index")
