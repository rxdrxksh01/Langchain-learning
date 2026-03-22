from langchain_groq import ChatGroq
from dotenv import load_dotenv

load_dotenv()

llm = ChatGroq(model="llama-3.1-8b-instant",temperature=0.5,model_kwargs={"max_completion_tokens": 10} )
# more temp more it is creative 
# max_completion_tokens = output words roughly

ans = llm.invoke('write a 5 line poem on cricket')
print(ans.content)