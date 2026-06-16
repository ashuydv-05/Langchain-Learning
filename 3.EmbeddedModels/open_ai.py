# VALID CODE , LACK OF CREDIT AND TOCKEN

from langchain_openai import OpenAIEmbeddings
from dotenv import load_dotenv
load_dotenv()

embedd = OpenAIEmbeddings(model ="text-embedding-3-small", dimensions=10);

result = embedd.embed_query("what is capital of bihar")
# WITHOUT STR, EMBEDD GIVE LIST AS OUTPUT
print(str(result))