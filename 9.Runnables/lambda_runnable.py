from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from dotenv import load_dotenv
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import PromptTemplate
from langchain_core.runnables import RunnableSequence, RunnableParallel, RunnableLambda, RunnablePassthrough

load_dotenv()
llm = HuggingFaceEndpoint(
    repo_id="openai/gpt-oss-20b",
    task="text-generation"
)
model = ChatHuggingFace(llm=llm)
template1 = PromptTemplate(
    template="Generate an 5 important about {topic}",
    input_variables=['topic']
)
parser = StrOutputParser()


def word_count(text):
    return len(text.split())

chain_1 = RunnableSequence(template1,model,parser)

chain_2 = RunnableParallel(
    {
        "joke": RunnablePassthrough(),
        # Both of Runnable lambda calling method will works
        # "words" : RunnableLambda(word_count)
        'words': RunnableLambda(lambda x: len(x.split()))
    }
)

main_chain = RunnableSequence(chain_1,chain_2)

result = main_chain.invoke({'topic':'bullet'})
print(result)