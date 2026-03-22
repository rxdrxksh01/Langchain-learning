
from langchain_core.messages import SystemMessage,HumanMessage,AIMessage
from langchain_groq import ChatGroq
from dotenv import load_dotenv

load_dotenv()
llm = ChatGroq(model="llama-3.1-8b-instant")
messages = [
    SystemMessage(content="You are a helpful assistant"),
    HumanMessage(content='tell me about langchain')
    
]
ans = llm.invoke(messages)
# print(ans.content)
messages.append(AIMessage(content=ans.content))
print(messages)
