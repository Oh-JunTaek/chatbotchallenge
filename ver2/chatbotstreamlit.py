import streamlit as st
from transformers import GPT2LMHeadModel, GPT2Tokenizer

# 모델 및 토크나이저 로드
model_path = 'C:/Users/dev/Documents/GitHub/ChatBot/chatbot_model'
tokenizer_path = 'C:/Users/dev/Documents/GitHub/ChatBot/chatbot_tokenizer'

model = GPT2LMHeadModel.from_pretrained(model_path)
tokenizer = GPT2Tokenizer.from_pretrained(tokenizer_path)

# Streamlit 앱 구현
st.title("GPT-2 Chatbot")
user_input = st.text_input("You:", "")

if user_input:
    # 사용자 입력을 모델에 전달하여 응답 생성
    input_ids = tokenizer.encode(user_input, return_tensors='pt')
    output = model.generate(input_ids, max_length=50, num_return_sequences=1, do_sample=True, top_k=50, top_p=0.95, num_beams=1)
    response = tokenizer.decode(output[0], skip_special_tokens=True)
    st.write("Chatbot:", response)
