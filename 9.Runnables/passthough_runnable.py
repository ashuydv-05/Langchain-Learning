from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from dotenv import load_dotenv
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import PromptTemplate
from langchain_core.runnables import RunnableSequence, RunnableParallel, RunnablePassthrough
load_dotenv()
llm = HuggingFaceEndpoint(
    repo_id="openai/gpt-oss-20b",
    task="text-generation"
)
model = ChatHuggingFace(llm=llm)
parser = StrOutputParser()

passthrough = RunnablePassthrough()

# print(passthrough.invoke(2))
template1 = PromptTemplate(
    template="write a joke on {topic}",
    input_variables=['topic']
)

template2 = PromptTemplate(
    template="explain the following :{text}",
    input_variables=['text']
)

chain1 = RunnableSequence(template1 , model, parser)

chain2 = RunnableParallel(
    {
        "joke": RunnablePassthrough(),
        "explain" : RunnableSequence(template2 , model, parser)
    }
)

main_chain = RunnableSequence(chain1, chain2)

result = main_chain.invoke({'topic': 'cricket'})
print(result)