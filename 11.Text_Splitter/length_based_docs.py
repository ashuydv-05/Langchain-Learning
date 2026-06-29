from langchain_text_splitters import CharacterTextSplitter
from langchain_community.document_loaders import PyPDFLoader

loader = PyPDFLoader('India_Agentic_AI_Open_Hackathon_2026_T&C.pdf')

docs = loader.load()

splitter = CharacterTextSplitter(
    chunk_size = 100,
    chunk_overlap=0,
    separator=''
)

result = splitter.split_documents(docs)
print(result[0])