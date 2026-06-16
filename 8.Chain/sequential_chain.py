from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from dotenv import load_dotenv
load_dotenv()

llm = HuggingFaceEndpoint(
    repo_id="openai/gpt-oss-20b",
    task = "text-generation"
)
model = ChatHuggingFace(llm=llm)

template1 = PromptTemplate(
    template="Generate an 2 paragraph summary about the {topic}",
    input_variables=['topic']
)

template2 = PromptTemplate(
    template="Extract 5 main points from the {content}",
    input_variables=['content']
)

parser = StrOutputParser()

chain = template1 | model | parser | template2 | model | parser
result = chain.invoke({'topic':'cricket'})
print(result)

# chain visuliser
chain.get_graph().print_ascii()
