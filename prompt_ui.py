from langchain_groq import ChatGroq
from dotenv import load_dotenv
import streamlit as st
from langchain_core.prompts import PromptTemplate,load_prompt

load_dotenv()
model = ChatGroq(model="llama-3.1-8b-instant")
st.header('Reasearch Tool')

paper_input = st.selectbox( "Select Research Paper Name", ["Attention Is All You Need", "BERT: Pre-training of Deep Bidirectional Transformers", "GPT-3: Language Models are Few-Shot Learners", "Diffusion Models Beat GANs on Image Synthesis"] )

style_input = st.selectbox( "Select Explanation Style", ["Beginner-Friendly", "Technical", "Code-Oriented", "Mathematical"] ) 

length_input = st.selectbox( "Select Explanation Length", ["Short (1-2 paragraphs)", "Medium (3-5 paragraphs)", "Long (detailed explanation)"] )
template=load_prompt('template.json')





if st.button('Summarize'):
    Chain = template|model
    result = Chain.invoke(({
    'paper_input': paper_input,
    'style_input': style_input,
    'length_input': length_input}))
    # prompt = template.invoke({
    # 'paper_input': paper_input,
    # 'style_input': style_input,
    # 'length_input': length_input})
    
    st.write(result.content)


# # fill the place holders
# prompt = template.invoke({
#     'paper_input': paper_input,
#     'style_input': style_input,
#     'length_input': length_input
# })

# if st.button('Summarize'):
#     result = model.invoke(prompt)
#     st.write(result.content)



# why not used f string instead of prmpottemplate
# yes we can do and it will work but then why use this class there r multiple reasons 
# 1 default validation - meaning think by chance u forgot to give len then if you add parameter validate_parameter then it woill give error same for if u add extra 
# 2 reusable 
# 3 Langchain Ecosystem
