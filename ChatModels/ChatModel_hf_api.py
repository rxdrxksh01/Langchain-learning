import warnings
warnings.filterwarnings("ignore")

from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from dotenv import load_dotenv
load_dotenv()

llm = HuggingFaceEndpoint(
    repo_id="meta-llama/Llama-3.3-70B-Instruct",
    task='text-generation',
    provider="hyperbolic"
)

model = ChatHuggingFace(llm=llm)
result = model.invoke('who is prime minister of india')
print(result.content)

# # 
# import warnings
# warnings.filterwarnings("ignore")

# from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
# from dotenv import load_dotenv
# load_dotenv()

# llm = HuggingFaceEndpoint(
#     repo_id="meta-llama/Llama-3.2-1B-Instruct",
#     task='text-generation',
#     provider="novita"
# )

# model = ChatHuggingFace(llm=llm)
# result = model.invoke('who is prime minister of india')
# print(result.content)
# worked but wrong output rishi kumar modi cz of small paramteres 1 b 
