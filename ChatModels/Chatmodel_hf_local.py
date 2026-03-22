from langchain_huggingface import ChatHuggingFace, HuggingFacePipeline

llm = HuggingFacePipeline.from_model_id(
    model_id='TinyLlama/TinyLlama-1.1B-Chat-v1.0',  # supports chat
    task='text-generation',
    pipeline_kwargs={
        "max_new_tokens": 100
    }
)

model = ChatHuggingFace(llm=llm)

ans = model.invoke('what is the capital of india')

# Remove everything before and including <|assistant|>
clean = ans.content.split("<|assistant|>")[-1].strip()
print(clean)








# ans = model.invoke('what is the capital of india')
# print(ans.content)
# 
# Both `max_new_tokens` (=100) and `max_length`(=2048) seem to have been set. `max_new_tokens` will take precedence. Please refer to the documentation for more information. (https://huggingface.co/docs/transformers/main/en/main_classes/text_generation)
# <|user|>
# what is the capital of india</s>
# <|assistant|>
# The capital of India is New Delhi.

# References:

# 1. Wikipedia. "Capitals of sovereign states and dependent territories." Accessed April 11, 2021. https://en.wikipedia.org/wiki/Capitals_of_sovereign_states_and_dependent_territories
# 2. Ministry of Home Affairs, Government of India. "India's Capital." Accessed April 1
# (venv) rudraksh@Rudrakshs-MacBook-Pro-4 Langchain % 

