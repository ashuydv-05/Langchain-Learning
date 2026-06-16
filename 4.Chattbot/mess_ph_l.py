from langchain_core.prompts import PromptTemplate
from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from dotenv import load_dotenv

load_dotenv()

llm = HuggingFaceEndpoint(repo_id="openai/gpt-oss-20b", task="text-generation")
model = ChatHuggingFace(llm=llm)

prompt_template = PromptTemplate(
    template="You are a helpful customer support agent.\nHuman: {query}\nAssistant:",
    input_variables=["query"],
)
# chain creation

chain = prompt_template | model
result = chain.invoke({"query": "where is my refund?"})
print(result.content if hasattr(result, "content") else result)