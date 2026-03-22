from langchain_groq import ChatGroq
from langchain_core.messages import SystemMessage,HumanMessage,AIMessage
from dotenv import load_dotenv

load_dotenv()
llm = ChatGroq(model="llama-3.1-8b-instant")
ChatHistory = [SystemMessage(content='You are a helpful AI system')]

while True:
    user_input = input("You: ")
    ChatHistory.append(HumanMessage(content=user_input))
    if user_input == "exit":
        break
    ans = llm.invoke(ChatHistory)
    ChatHistory.append(AIMessage(content=ans.content))
    print("Bot: ", ans.content)
print(ChatHistory)
