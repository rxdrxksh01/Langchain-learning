from langchain_core.prompts import ChatPromptTemplate,MessagesPlaceholder
from langchain_core.messages import HumanMessage, AIMessage

chat_history=[]
# with open('chathistory.txt','r') as f:
#     chat_history.extend(f.readlines())
with open('chathistory.txt', 'r') as f:
    for line in f:
        line = line.strip()

        if line.startswith("HumanMessage"):
            content = line.split('content="')[1].split('"')[0]
            chat_history.append(HumanMessage(content=content))

        elif line.startswith("AIMessage"):
            content = line.split('content="')[1].split('"')[0]
            chat_history.append(AIMessage(content=content))
    


chat_template = ChatPromptTemplate([
    ('system','You are a helpful assistant'),
    MessagesPlaceholder(variable_name='chat_history'),
    ('human','{query}')
    
])
# print(chat_history)
prompt = chat_template.invoke({'chat_history':chat_history,'query':'where is my refund'})
print(prompt)
