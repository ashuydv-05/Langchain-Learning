from langchain_core.prompts import ChatPromptTemplate
# from langchain_core.messages import SystemMessage, HumanMessage
chat_template = ChatPromptTemplate([
    # chat_template = ChatPromptTemplate.from_messages([.      This also work fine, same OP.
    # using tuple here rather than previous used parameter
    ('system','You are a helpfull {domain} expert'),
    ('human','Explain in simple terms, what is the {topic}')
    # SystemMessage(content="You are an AI researcher"),
    # HumanMessage(content="Tell me about Langchain")
])

prompt = chat_template.invoke({'domain': 'cricket',
                        'topic':'Dusra'
                        })
print(prompt)