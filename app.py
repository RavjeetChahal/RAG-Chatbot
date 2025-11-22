import os
from dotenv import load_dotenv
import streamlit as st

from langchain_openai import ChatOpenAI, OpenAIEmbeddings
from langchain_community.vectorstores import FAISS
from langchain.chains import RetrievalQA

# Load environment variables
load_dotenv()
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

st.set_page_config(page_title="Aroma Restaurant Chatbot")
st.title("Ask Aroma's AI Assistant")

@st.cache_resource(show_spinner=False)
def load_vectorstore():
    if not os.path.isdir("restaurant_index"):
        raise RuntimeError("Vector index not found. Run build_index.py first.")
    embeddings = OpenAIEmbeddings(openai_api_key=OPENAI_API_KEY)
    return FAISS.load_local("restaurant_index", embeddings, allow_dangerous_deserialization=True)

def build_qa_chain():
    llm = ChatOpenAI(openai_api_key=OPENAI_API_KEY, model="gpt-4o-mini", temperature=0)
    retriever = load_vectorstore().as_retriever(search_kwargs={"k": 4})
    qa = RetrievalQA.from_chain_type(llm=llm, retriever=retriever, return_source_documents=True)
    return qa

query = st.text_input("Ask about our menu, allergens, hours, catering, or policies")

if query:
    if not OPENAI_API_KEY:
        st.error("OpenAI API key not found. Set OPENAI_API_KEY in your environment or .env file.")
    else:
        try:
            qa = build_qa_chain()
            with st.spinner("Thinking..."):
                result = qa.invoke({"query": query})
            answer = result.get("result", "").strip()
            sources = result.get("source_documents", []) or []

            if answer:
                st.success(answer)
            else:
                st.info("I did not find a confident answer. Please try rephrasing.")

        except Exception as e:
            st.error(f"Something went wrong: {type(e).__name__}: {e}")
