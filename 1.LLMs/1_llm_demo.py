from langchain_openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

# create openai object and write modell in it

llm = OpenAI(model ='gpt-4o-mini')

# invoke() - method allow us to communication with to llm model
# here OpenAI;

result = llm.invoke("What is the capital of Bihar")

print(result)

##Fail:->  Lack of credit of OPENAI API.