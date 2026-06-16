from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import JsonOutputParser
from langchain.output_parsers import ResponseSchema, StructuredOutputParser

print("Imported Successfully")
# from dotenv import load_dotenv
# load_dotenv()

# llm = HuggingFaceEndpoint(
#     repo_id="openai/gpt-oss-20b",
#     task="text-generation"
# )
# model = ChatHuggingFace(llm=llm)