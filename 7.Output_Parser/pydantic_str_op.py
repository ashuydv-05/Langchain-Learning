from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from langchain_core.prompts import PromptTemplate
from dotenv import load_dotenv
from langchain_core.output_parsers import PydanticOutputParser
from pydantic import BaseModel, Field
load_dotenv()

llm = HuggingFaceEndpoint(
    repo_id="openai/gpt-oss-20b",
    task="text-generation"
)
model = ChatHuggingFace(llm=llm)

#Create Pydantic object , Defining the Schema
class Person(BaseModel):
    name: str = Field(description='Name of the person')
    age: int = Field(gt = 18, description='Age of the person')
    city: str = Field(description='Name of the city the person belong to')

parser = PydanticOutputParser(pydantic_object=Person)

# Template creation
template1 = PromptTemplate(
    template='Generate the name, age and the city of the person who is resident of {place} {format_instr}',
    input_variables=['place'],
    partial_variables={'format_instr': parser.get_format_instructions()}

)
# prompt = template1.invoke({'place':'Uttar Pardesh'})
# result = model.invoke(prompt)
# final_result = parser.parse(result.content)

chain = template1 | model | parser
final_result = chain.invoke({'place':'Uttar Pardesh'})
print(final_result)