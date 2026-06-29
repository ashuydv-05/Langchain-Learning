from langchain_community.document_loaders import PyPDFLoader

loader = PyPDFLoader('India_Agentic_AI_Open_Hackathon_2026_T&C.pdf')

docs = loader.load()
# print(len(docs))
# print(docs[0].page_content)
print(docs[0].metadata)

