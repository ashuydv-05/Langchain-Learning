from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import JsonOutputParser
from dotenv import load_dotenv
load_dotenv()

llm = HuggingFaceEndpoint(
    repo_id="openai/gpt-oss-20b",
    task="text-generation"
)
model = ChatHuggingFace(llm=llm)
parser = JsonOutputParser()
# similar to the static prompt, no input variables
template1 = PromptTemplate(
    template="Give me a the name, age and city of fictional person \n {format_instr}",
    input_variables=[],
    partial_variables={'format_instr':parser.get_format_instructions}
)

# propmt = template1.format()
# result = model.invoke(propmt)
# final_result = parser.parse(result.content)

# USING CHAINS
chain = template1 | model | parser
# pass the empty dict in chain.invoke when ever there is not input_varible
result = chain.invoke({})
print(result)


# print(final_result)