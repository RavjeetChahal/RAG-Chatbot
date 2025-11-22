# Aroma Restaurant Chatbot

An AI-powered chatbot for Aroma Bar & Grill that answers customer questions about the restaurant's menu, hours, policies, and services using Retrieval-Augmented Generation (RAG) technology.

## Features

- 🤖 **AI-Powered Q&A**: Answers questions about menu items, allergens, operating hours, catering, and restaurant policies
- 🔍 **Semantic Search**: Uses FAISS vector store for efficient document retrieval
- 💬 **Interactive UI**: Built with Streamlit for a user-friendly chat interface
- 📚 **Knowledge Base**: Powered by restaurant data including FAQs, menu information, and policies

## Tech Stack

- **Frontend**: Streamlit
- **LLM**: OpenAI GPT-4o-mini (via LangChain)
- **Vector Store**: FAISS (Facebook AI Similarity Search)
- **Framework**: LangChain
- **Language**: Python 3.11+

## Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/RavjeetChahal/RAG-Chatbot.git
   cd Aroma_ChatBot
   ```

2. **Create a virtual environment**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Set up environment variables**
   
   Create a `.env` file in the root directory:
   ```env
   OPENAI_API_KEY=your_openai_api_key_here
   ```

## Setup

Before running the chatbot, you need to build the vector index:

1. **Build the vector store**
   ```bash
   python build_Index.py
   ```
   
   This will:
   - Load the restaurant data from `restaurant_data.txt`
   - Generate embeddings using OpenAI
   - Create and save the FAISS index to `restaurant_index/`

## Usage

1. **Start the Streamlit app**
   ```bash
   streamlit run app.py
   ```

2. **Open your browser**
   
   The app will automatically open in your default browser, typically at `http://localhost:8501`

3. **Ask questions**
   
   Type your questions about the restaurant in the input field, such as:
   - "What are your operating hours?"
   - "Do you have vegetarian options?"
   - "How can I make a reservation?"
   - "Do you offer catering services?"

## Project Structure

```
Aroma_ChatBot/
├── app.py                    # Main Streamlit application
├── build_Index.py            # Script to build the FAISS vector index
├── build_vector_store.py     # Alternative script for building vector store
├── restaurant_data.txt       # Restaurant knowledge base (Q&A data)
├── restaurant_index/         # Generated FAISS index files
│   ├── index.faiss
│   └── index.pkl
├── requirements.txt          # Python dependencies
├── .env                      # Environment variables (not in repo)
└── README.md                 # This file
```

## Requirements

- Python 3.11 or higher
- OpenAI API key
- Internet connection (for API calls)

## Dependencies

- `streamlit` - Web framework for the UI
- `langchain` - LLM framework
- `langchain-openai` - OpenAI integration for LangChain
- `langchain-community` - Community integrations
- `faiss-cpu` - Vector similarity search
- `python-dotenv` - Environment variable management

## Notes

- The vector index must be built before running the app
- Ensure your OpenAI API key is set in the `.env` file
- The chatbot uses GPT-4o-mini for cost-effective responses
- Source documents are retrieved and displayed for transparency

## License

This project is open source and available for use.

## Contact

For questions or issues, please open an issue on GitHub.

