# VALID CODE , LACK OF CREDIT AND TOCKEN

from langchain_openai import OpenAIEmbeddings
from dotenv import load_dotenv
load_dotenv()

embedd = OpenAIEmbeddings(model ="text-embedding-3-small", dimensions=10);
documents = [
    "Patna is capital of bihar",
    "DElhi capital india"
]
# result = embedd.embed_query("what is capital of bihar")
result = embedd.embed_documents(documents)

# WITHOUT STR, EMBEDD GIVE LIST AS OUTPUT

print(str(result))