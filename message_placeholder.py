from langchain_core.prompts import ChatPromptTemplate,MessagesPlaceholder
chat_history=[]
with open('chathistory.txt','r') as f:
    chat_history.extend(f.readlines())
    


chat_template = ChatPromptTemplate([
    ('system','You are a helpful assistant'),
    MessagesPlaceholder(variable_name='chat_history'),
    ('human','{query}')
    
])
# print(chat_history)
prompt = chat_template.invoke({'chat_history':chat_history,'query':'where is my refund'})
# print(prompt)
