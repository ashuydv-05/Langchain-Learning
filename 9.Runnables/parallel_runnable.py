from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from dotenv import load_dotenv
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import PromptTemplate
from langchain_core.runnables import RunnableSequence, RunnableParallel

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

template2 = PromptTemplate(
    template="Generate an linkedin post about the {topic}",
    input_variables=['topic']
)

parser = StrOutputParser()

parallel_chain = RunnableParallel(
    {
    'tweet': RunnableSequence( template1 , model, parser),
    'linkedin' : RunnableSequence( template2 , model, parser)
}
    
)

result = parallel_chain.invoke({'topic': 'AI'})
# print(result)
print("following is the tweet")
print(result['tweet'])
print("following is the LinkedIn Post")
print(result['linkedin'])
