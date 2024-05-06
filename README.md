# PDF Reader

## Library Function

- streamlit: This library will be used to create the frontend of the application.
- load_dotenv: This library will be used to import the API keys from the .env file.
- HuggingFaceEmbeddings and OpenAIEmbeddings: These methods are from the langchain.embeddings module and will be used to create embeddings for the text.
- ChatOpenAI: This method is from the langchain.chat_models module and will be used to initialize the LLM chat model.
- ConversationalRetrievalChain: This is a method from the langchain.chains module and will be used to create prompt chains.
- Chroma: This is a method from the langchain.vectorstores module and creates the database that you’ll be using to store your PDF embeddings.
- PyPDFLoader: This is a method in the langchain.document_loaders module and will be used to load the PDF.
- PdfReader and PdfWriter: These are methods in the PyPDF2 library and will be used to extract sections of the PDF files.
- NamedTemporaryFile: This is a method in the tempfile library and will be used to create a temporary PDF file.
- base64: This method is used for encoding binary files as text for displaying them on web pages.
