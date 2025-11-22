import os
from dotenv import load_dotenv
from langchain_community.document_loaders import TextLoader
from langchain_openai import OpenAIEmbeddings
from langchain_community.vectorstores import FAISS

def main():
    load_dotenv()
    api_key = os.getenv("OPENAI_API_KEY")
    if not api_key:
        raise RuntimeError("Missing OPENAI_API_KEY in environment")

    source_path = "restaurant_data.txt"
    if not os.path.isfile(source_path):
        raise FileNotFoundError(f"Missing {source_path}")

    loader = TextLoader(source_path, encoding="utf-8")
    documents = loader.load()
    if not documents:
        raise RuntimeError("No documents loaded from restaurant_data.txt")

    embeddings = OpenAIEmbeddings(openai_api_key=api_key)
    vectorstore = FAISS.from_documents(documents, embeddings)
    vectorstore.save_local("restaurant_index")
    print("Index built and saved to restaurant_index")

if __name__ == "__main__":
    main()
