import streamlit as st
from transformers import GPT2LMHeadModel, GPT2Tokenizer
import torch

# GPT-2 모델 및 토크나이저 로드
model = GPT2LMHeadModel.from_pretrained('gpt2')
tokenizer = GPT2Tokenizer.from_pretrained('gpt2')

# Streamlit 앱 설정
st.set_page_config(page_title="My Chatbot", layout="wide")

# 1. 입력 데이터 전처리 개선
def preprocess_input(prompt):
    input_ids = tokenizer.encode(prompt, return_tensors='pt')
    attention_mask = torch.ones_like(input_ids)
    return input_ids, attention_mask

# 2. 대화 흐름 관리 개선
conversation_history = []

# 챗봇 대화 함수
def generate_response(prompt):
    # 입력 데이터 전처리
    input_ids, attention_mask = preprocess_input(prompt)

    # 대화 내용 저장
    conversation_history.append({"user": prompt})

    # 모델 출력 생성
    output = model.generate(input_ids, attention_mask=attention_mask, max_length=50, num_return_sequences=1, do_sample=True, top_k=50, top_p=0.95, num_beams=1)
    response = tokenizer.decode(output[0], skip_special_tokens=True)

    # 대화 내용 저장
    conversation_history.append({"bot": response})

    return response

# 3. 사용자 경험 개선
st.title("My Chatbot")
user_input = st.text_area("You:", height=200)

if st.button("Send"):
    try:
        # 4. 모델 성능 개선
        bot_response = generate_response(user_input)
        st.text_area("Chatbot:", value=bot_response, height=200)
    except Exception as e:
        # 5. 오류 처리 및 예외 처리
        st.error("An error occurred while generating the response.")
        st.error(str(e))
