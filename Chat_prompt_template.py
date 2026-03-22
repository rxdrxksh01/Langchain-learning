
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.messages import SystemMessage,HumanMessage,AIMessage


chat_template = ChatPromptTemplate([
    ('system','You are a helpful {domain} system'),
    ('human','Explain in simple terms what is {topic}')

    # SystemMessage(content="You are a helpful {domain} system"),
    # HumanMessage(content="Explain in simple terms what is {topic}")

    
])
prompt = chat_template.invoke({'domain':'cricket','topic':'lbw'})
print(prompt)