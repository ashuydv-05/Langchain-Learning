from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from dotenv import load_dotenv
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import PromptTemplate
from langchain_core.runnables import RunnableSequence

llm = HuggingFaceEndpoint(
    repo_id="openai/gpt-oss-20b",
    task="text-generation"
)
model = ChatHuggingFace(llm=llm)

template1 = PromptTemplate(
    template="Write a joke about {topic}",
    input_variables=['topic']
)
parser = StrOutputParser()

template2 = PromptTemplate(
    template='Explain me the following text : {text}',
    input_variables=['topic']
)

# Both statement do same function..
chain = RunnableSequence(template1, model, parser, template2, model , parser)
# chain = template1 | model | parser |template2 | model | parser
result = chain.invoke({'topic':'AI'})
print(result)