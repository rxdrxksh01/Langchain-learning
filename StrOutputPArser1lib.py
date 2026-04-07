
from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser


load_dotenv()

llm = HuggingFaceEndpoint(
    repo_id="meta-llama/Llama-3.3-70B-Instruct",
    task='text-generation',
    provider="hyperbolic"
)
model = ChatHuggingFace(llm=llm)

# 1st prompt deatil report 
template1 = PromptTemplate(
    template='Write a detail report on {topic}',
    input_variables=['topic']
)

# 2nd summary
template2 = PromptTemplate(
    template='Write a 2 line summary on the following text./n {text}',
    input_variables=['text']
)

parser = StrOutputParser()
chain = (template1 
|model
|parser
# |(lambda x:{'input':x})
|template2
|model
|parser)

result = chain.invoke({'topic':'AI'})
print(result)



