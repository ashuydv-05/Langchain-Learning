from langchain_openai import ChatOpenAI
from dotenv import load_dotenv

load_dotenv()
'''model = ChatOpenAI(model= 'gpt-4o-mini', temperature , max_completion_tokens=)
temperature - paramenter control the randomness of the language model
max_completion_tokens-  used when u are having limited tokens
token refers as words
Also if u want stable result use fixed temperature near to zero
and for visa versa make is temp good near to 1.5 - 2'''
 
model = ChatOpenAI(model= 'gpt-4o-mini')
result = model.invoke("What is the capital of INDIA")
print(result)

#FAIL , same reason: lack of token/credits;