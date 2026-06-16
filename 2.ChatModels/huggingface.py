from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from dotenv import load_dotenv
load_dotenv()

llm = HuggingFaceEndpoint(
    repo_id="openai/gpt-oss-20b",
    task="text-generation"
)
model = ChatHuggingFace(llm=llm)
result = model.invoke("I am a SEASONAL FARMER, i plant mangoes share me the recent loan schemes under Govt. Of India with Year of launc")
print(result.content)
