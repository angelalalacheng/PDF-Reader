
# Task 1: Import the Libraries
import streamlit as st
from dotenv import load_dotenv
from langchain.embeddings import HuggingFaceEmbeddings, OpenAIEmbeddings
from langchain.chat_models import ChatOpenAI
from langchain.chains import ConversationalRetrievalChain
from langchain.vectorstores import Chroma
from langchain.document_loaders import PyPDFLoader
from PyPDF2 import PdfReader, PdfWriter
from tempfile import NamedTemporaryFile
import base64
from htmlTemplate import expander_css, css, bot_template, user_template
# Task 4: Process the Input PDF



# Task 6: Method for Handling User Input



def main():
    load_dotenv()
    st.set_page_config(page_title='PDF Reader', layout='wide', page_icon=':books:')

    st.write(css, unsafe_allow_html=True)

    """
    設置 session_state 的初始值。
    你可以使用 st.session_state 來檢查是否已經設置了某個鍵(key)。
    如果沒有，可以初始化它。
    """
    if "conversation" not in st.session_state: # prompt engineering for querying the LLM
        st.session_state.conversation = None
    if "chat_history" not in st.session_state: # history of the conversation 
        st.session_state.chat_history = []
    if "N" not in st.session_state: # page number of the PDF page
        st.session_state.N = 0
    
    """
    st.columns 用於創建多行布局，可以在同一列内並排顯示多個元素
    st.columns([1, 1]) 表示創建兩行，每行的寬度比例為 1:1
    """
    st.session_state.col1, st.session_state.col2 = st.columns([1, 1])
    st.session_state.col1.header("PDF Reader :books:")

    # text box in the first column and save the input question to a variable
    user_question = st.session_state.col1.text_input("Ask a question on the contents of the uploaded PDF:")
    
    # scrollable area for displaying your chat in the first column
    st.session_state.expander1 = st.session_state.col1.expander('Your Chat', expanded=True)
    st.session_state.col1.markdown(expander_css, unsafe_allow_html=True) 



    # Task 5: Load and Process the PDF 
    

    
    # Task 7: Handle Query and Display Pages
    
       



if __name__ == '__main__':
    main()

