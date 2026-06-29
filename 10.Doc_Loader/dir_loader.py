from langchain_community.document_loaders import DirectoryLoader, PyPDFLoader
loader = DirectoryLoader(
    path = 'material',
    glob='*.pdf',
    loader_cls=PyPDFLoader
)

# docs = loader.load()
docs = loader.lazy_load()

# print(len(docs))
for x in docs:
    print(x.metadata)