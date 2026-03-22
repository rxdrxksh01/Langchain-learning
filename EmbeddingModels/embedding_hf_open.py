from langchain_huggingface import HuggingFaceEmbeddings

embedding = HuggingFaceEmbeddings(model_name='sentence-transformers/all-MiniLM-L6-v2')
text = 'delhi is capital of india'
documents = [
    'Delhi is capital of india',
    'chand is capital of haryana',
    'paris is capital of france'
]
# vector = embedding.embed_query(text)
# print(len(vector))
vector = embedding.embed_documents(documents)
print(len(vector))