from langchain_openai import ChatOpenAI, OpenAIEmbeddings
import streamlit as st
from langchain.document_loaders import PyPDFLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.memory import ConversationBufferWindowMemory
from langchain.vectorstores import Chroma
from langchain.chains import ConversationalRetrievalChain
from langchain.prompts import PromptTemplate
import shutil
import os
import tempfile

os.environ["ANONYMIZED_TELEMETRY"] = "False"
uploaded_file_path = os.path.join(tempfile.gettempdir(), "chatbot_datafolder")
vec_db_path = os.path.join(tempfile.gettempdir(), "chatbot_vec_db")


def clean(docs):
    cleaned_data = docs.page_content.encode('utf-8', 'ignore').decode('utf-8')
    docs.page_content = cleaned_data
    return docs


st.set_page_config(page_title="QAbot")
st.title("Intelligent AI system 🤖⚡")

uploaded_file = st.file_uploader(label="Please upload the file", type="pdf")

if not uploaded_file:
    if "current_file" in st.session_state:
        del st.session_state["current_file"]
    if "memory" in st.session_state:
        st.session_state.memory.clear()

    st.info("Please upload document to proceed")
    st.stop()

if "current_file" not in st.session_state or st.session_state.current_file != uploaded_file.name:
    st.session_state.current_file = uploaded_file.name
    if "memory" in st.session_state:
        st.session_state.memory.clear()
    else:
        st.session_state.memory = ConversationBufferWindowMemory(
            k=5,
            memory_key="chat_history",
            return_messages=True,
            output_key="answer"
        )

    if os.path.exists(vec_db_path):
        shutil.rmtree(vec_db_path)

if "memory" not in st.session_state:
    st.session_state.memory = ConversationBufferWindowMemory(
        k=5,
        memory_key="chat_history",
        return_messages=True,
        output_key="answer"
    )
memory = st.session_state.memory

content = uploaded_file.read()
os.makedirs(uploaded_file_path, exist_ok=True)
new_file_path = os.path.join(uploaded_file_path, "abc.pdf")
with open(new_file_path, 'wb') as new_file:
    new_file.write(content)

document_loader = PyPDFLoader(new_file_path)
docs = document_loader.load()

splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=150)
text_chunks = splitter.split_documents(docs)
cleaned_text = [clean(each_text_chunk) for each_text_chunk in text_chunks]

embed_model = OpenAIEmbeddings()

vector_db = Chroma.from_documents(
    documents=cleaned_text,
    embedding=embed_model,
    persist_directory=vec_db_path,
    collection_name="candidate_data"
)
retriever = vector_db.as_retriever(search_kwargs={'k': 3})

st.markdown("Thanks for uploading the document, ask your question")

template = """you are a helpful assistant. user will upload a document and he will ask questions
           based on the questions you should retrieve the data from the uploaded document 
           
           Chat History:
           {chat_history}

           Context:
           {context}

           Questions:
           {question}

           Answer:
           
           """

llm_model = ChatOpenAI()
prompt = PromptTemplate(template=template, input_variables=['chat_history', 'context', 'question'])
chain = ConversationalRetrievalChain.from_llm(
    llm=llm_model,
    retriever=retriever,
    combine_docs_chain_kwargs={'prompt': prompt},
    memory=memory
)

query = st.text_input("Ask your query")
if query:
    response = chain.run(query)
    st.markdown(response)
