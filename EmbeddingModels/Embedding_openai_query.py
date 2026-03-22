# import warnings
# warnings.filterwarnings("ignore")

# from langchain_google_genai import GoogleGenerativeAIEmbeddings
# from dotenv import load_dotenv
# import os
# load_dotenv()

# # print(os.getenv("GOOGLE_API_KEY"))  # add this to confirm key is loading

# embeddings = GoogleGenerativeAIEmbeddings(model="text-embedding-004")

# result = embeddings.embed_query("what is the capital of india")
# print(result)
# print(len(result))
# import google.generativeai as genai
# import os
# from dotenv import load_dotenv
# load_dotenv()

# genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

# for m in genai.list_models():
#     if 'embed' in m.name:
#         print(m.name)
import warnings
warnings.filterwarnings("ignore")

from langchain_google_genai import GoogleGenerativeAIEmbeddings
from dotenv import load_dotenv
load_dotenv()
documents = [
    'Delhi is capital of india',
    'chand is capital of haryana',
    'paris is capital of france'
]

embeddings = GoogleGenerativeAIEmbeddings(model="models/gemini-embedding-001",output_dimensionality=32)

# result = embeddings.embed_query("what is the capital of india")
result = embeddings.embed_documents(documents)

print(result)
print(len(result))