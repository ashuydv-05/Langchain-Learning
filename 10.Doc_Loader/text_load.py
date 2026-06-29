from langchain_community.document_loaders import TextLoader
from langchain_huggingface import HuggingFaceEndpoint, ChatHuggingFace
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import PromptTemplate
from dotenv import load_dotenv
load_dotenv()

llm = HuggingFaceEndpoint(
    repo_id="openai/gpt-oss-20b",
    task="text-generation"
)
model = ChatHuggingFace(llm=llm)
parser = StrOutputParser()

# Below loader object is created
loader = TextLoader('AI.txt', encoding='utf-8') 

# .load() function is being called
docs = loader.load()

# print(type(docs)) --LIST
# print(len(docs))

# From below command, both metadata and page_content is shown 
# print(docs[0]) 
# print(docs)
# print(docs[0].page_content)
# print(docs[0].metadata)


template1 = PromptTemplate(
    template = "Write a summarize of the following text {text}",
    input_variables=['text']
)

chain = template1 | model | parser
result = chain.invoke({'text':docs[0].page_content })
print(result)


