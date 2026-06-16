from langchain_anthropic import ChatAnthropic
from dotenv import load_dotenv
load_dotenv()
model = ChatAnthropic( ) # write the model.. in the brackets
result = model.invoke("what is the capital of india")
print(result)