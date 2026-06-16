from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_groq  import ChatGroq
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.output_parsers import PydanticOutputParser
from langchain_core.runnables import RunnableParallel, RunnableBranch , RunnableLambda
from pydantic import BaseModel, Field
from typing import Literal
from dotenv import load_dotenv
load_dotenv()

llm = HuggingFaceEndpoint(
    # repo_id="openai/gpt-oss-20b",
    repo_id="Qwen/Qwen3-8B",
    task = "text-generation"
)
model1 = ChatHuggingFace(llm=llm)

# model2= ChatGoogleGenerativeAI(model="gemini-3.5-flash")
parser = StrOutputParser()

#  class creation  that provide consistent output
class Feedback(BaseModel):
    sentiment : Literal['positive','negative'] = Field(description="Give the sentiment of the feedback")

parser2 = PydanticOutputParser(pydantic_object=Feedback)

template1 = PromptTemplate(
    template="classify the sentiment of the feedback into positive and negation \n {feedback} \n {format_instr}",
    input_variables=['feedback'],
    partial_variables={'format_instr': parser2.get_format_instructions()}
)

classifier_chain = template1 | model1 | parser2

# result = classifier_chain.invoke({'feedback': 'This is a terrible smartphone'})
# STRUCTURED OUTPUT
# result = classifier_chain.invoke({'feedback': 'This is a terrible smartphone'}).sentiment

template2 = PromptTemplate(
    template="Write  an appropriate response to this postive feedback \n {feedback}",
    input_variables=['feedback']
)

template3 = PromptTemplate(
    template="Write  an appropriate response to this negative feedback \n {feedback}",
    input_variables=['feedback']
)

# BRANCH CHAIN
branch_chain = RunnableBranch(
    # (condition1, chain1),
    (lambda x : x.sentiment == 'positive', template2|model1|parser),

    # (condition2, chain2),
    (lambda x : x.sentiment == 'negative', template3|model1|parser),

    # default chain
    RunnableLambda(lambda x:"could not find the setiment")
)

# Final chain

chain = classifier_chain|branch_chain
result = chain.invoke({'feedback':'This is a intelligent phone'})
print(result)
chain.get_graph().print_ascii()
