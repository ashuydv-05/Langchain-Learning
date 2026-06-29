from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from dotenv import load_dotenv
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import PromptTemplate
from langchain_core.runnables import RunnableSequence, RunnableParallel, RunnableLambda, RunnablePassthrough, RunnableBranch


load_dotenv()
llm = HuggingFaceEndpoint(
    repo_id="openai/gpt-oss-20b",
    task="text-generation"
)
model = ChatHuggingFace(llm=llm)
parser = StrOutputParser()

template1 = PromptTemplate(
    template="Write a detailed report on {topic}",
    input_variables=['topic']
)

template2 = PromptTemplate(
    template="summarize the following {text}",
    input_variables=['text']
)

chain_1 = RunnableSequence(template1, model,parser)

branch_chain = RunnableBranch(
    # ( condition , runnable)
    #  default runnable
    (lambda x: len(x.split())>500 , RunnableSequence(template2, model, parser)),
    RunnablePassthrough()
)

main_chain = RunnableSequence(chain_1,branch_chain)
result= main_chain.invoke({'topic':'India'})
print(result)

