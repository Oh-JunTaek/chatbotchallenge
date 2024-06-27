from flask import Flask, request, jsonify
import torch
from transformers import BlenderbotTokenizer, BlenderbotForConditionalGeneration

app = Flask(__name__)

# BlenderBot 모델 및 토크나이저 로드
model = BlenderbotForConditionalGeneration.from_pretrained('facebook/blenderbot-400M-distill')
tokenizer = BlenderbotTokenizer.from_pretrained('facebook/blenderbot-400M-distill')

@app.route('/chat', methods=['POST'])
def chat():
    # 사용자 입력 받기
    data = request.get_json()
    user_input = data['user_input']

    # 챗봇 응답 생성
    bot_response = generate_response(user_input)

    # 응답을 JSON 형식으로 반환
    return jsonify({'response': bot_response})

def generate_response(input_text):
    # 사용자 입력을 토큰화
    input_ids = tokenizer.encode(input_text, return_tensors='pt')
    
    # 모델을 통해 응답 생성
    output_ids = model.generate(input_ids, max_length=1000, num_beams=4, early_stopping=True)[0]
    
    # 생성된 응답 디코딩
    response = tokenizer.decode(output_ids, skip_special_tokens=True)
    
    return response

if __name__ == '__main__':
    app.run(debug=True)