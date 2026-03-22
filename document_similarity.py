# from cv2 import sort
from langchain_huggingface import HuggingFaceEmbeddings
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np 


embedding = HuggingFaceEmbeddings(
    model_name='sentence-transformers/all-MiniLM-L6-v2',
    model_kwargs={'truncate_dim': 32}  
)
documents = [
    "Virat Kohli is an Indian cricketer known for his aggressive batting and leadership.",
    "MS Dhoni is a former Indian captain famous for his calm demeanor and finishing skills.",
    "Sachin Tendulkar, also known as the 'God of Cricket', holds many batting records.",
    "Rohit Sharma is known for his elegant batting and record-breaking double centuries."
]
query = 'tell me about virat kohli '

doc_embed = embedding.embed_documents(documents)
query_embed = embedding.embed_query(query)

scores = (cosine_similarity([query_embed], doc_embed))[0]
index,score = (sorted(list(enumerate(scores)),key=lambda x:x[1])[-1])
print(documents[index])

# print(scores)