from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
import streamlit as st
from langchain_core.prompts import PromptTemplate, load_prompt
from dotenv import load_dotenv
load_dotenv()

# Create the model
llm = HuggingFaceEndpoint(
    repo_id="openai/gpt-oss-20b",
    task="text-generation"
)
model = ChatHuggingFace(llm=llm)

st.header('Research tool')
paper_input= st.selectbox("select research paper name", ["Attention Is All You Need",
"BERT: Pre- training of Deep Bidirectional Transformer",
"Diffusion models beat GANs on Image Synthesis"
])
style_input = st.selectbox("Select Explaination Style",[
    "Beginner- Friendly",
    "Technical",
    "Code - Oriented",
    "Long(detailed Explanation)"
])

length_input= st.selectbox("Select explaination length",[
    "Short(1-2 paragraphs)",
    "Medium(3-5 paragraphs)",
    "Long(Detailed explaination)"
])

template = load_prompt('template.json')

# TEMPLATE
# template = PromptTemplate(
#     template="""Please summarize the research paper titled "{paper_input}" with the following specifications:

# Explanation Style: {style_input}
# Explanation Length: {length_input}

# 1. Mathematical Details:
#    - Include relevant mathematical equations if present in the paper.
#    - Explain the mathematical concepts using simple, intuitive code snippets where applicable.

# 2. Analogies:
#    - Use relatable analogies to simplify complex ideas.

# If certain information is not available in the paper, respond with:
# "Insufficient information available"
# instead of guessing.

# Ensure the summary is clear, accurate, and aligned with the provided style and length.""",
#     input_variables=['paper_input', 'style_input', 'length_input'],
#     validate_template=True
# )
# VALIDATE_TEMPLATE 

# FILL THE PLACEHOLDER
# prompt =template.invoke({
#     'paper_input':paper_input,
#     'style_input': style_input,
#     'length_input': length_input
# })
# user_ip = st.text_input("Enter the prompt")

if st.button("Summarize"):
    # result = model.invoke(user_ip)
    # st.write(result.content if hasattr(result, 'content') else result)
    chain = template | model
    result = chain.invoke({
    'paper_input':paper_input,
    'style_input': style_input,
    'length_input': length_input
    })
    # result = model.invoke(prompt)
    st.write(result.content)
