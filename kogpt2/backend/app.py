from flask import Flask, request, jsonify
from flask_cors import CORS
from pymongo import MongoClient
from dotenv import load_dotenv
import os
from load_model import load_kogpt2

# .env 파일에서 환경 변수를 로드합니다.
load_dotenv()

# Flask 애플리케이션을 생성하고 CORS 설정을 적용합니다.
app = Flask(__name__)
CORS(app)

# 모델과 토크나이저를 로드합니다.
model, tokenizer = load_kogpt2()

# 환경 변수에서 MongoDB URI를 가져옵니다.
mongodb_uri = os.getenv('MONGODB_URI')

# MongoDB URI가 올바르게 로드되었는지 확인합니다.
print(f"MongoDB URI: {mongodb_uri}")

# MongoDB 설정을 수행합니다.
client = MongoClient(mongodb_uri)
db = client.chatbot

@app.route('/api/chat', methods=['POST'])
def chat():
    try:
        data = request.json  # 클라이언트로부터 JSON 데이터를 가져옵니다.
        if not data:
            raise ValueError("No JSON payload received")

        user_message = data.get('message')  # 사용자가 보낸 메시지를 추출합니다.

        if not user_message:
            raise ValueError("No 'message' field in JSON payload")

        print(f"User message: {user_message}")

        # 사용자의 메시지를 인코딩합니다.
        input_ids = tokenizer.encode(user_message, return_tensors='pt')  # 메시지를 토크나이저로 인코딩합니다.
        print(f"Encoded input IDs: {input_ids}")

        # 응답 생성 시 max_new_tokens를 사용하여 생성된 토큰의 수를 제한합니다.
        output = model.generate(
            input_ids,
            max_new_tokens=50,  # 새로 생성되는 토큰의 수를 제한합니다.
            repetition_penalty=2.0,  # 반복 페널티를 적용합니다.
            pad_token_id=tokenizer.pad_token_id,
            eos_token_id=tokenizer.eos_token_id,
            bos_token_id=tokenizer.bos_token_id,
            use_cache=True,
            temperature=0.7,  # 다양성을 위해 온도를 설정합니다.
            top_p=0.9,  # top_p를 설정하여 확률이 높은 단어들만 선택합니다.
            top_k=50,  # top-k 샘플링을 추가합니다.
            no_repeat_ngram_size=2,  # n-그램 반복을 방지합니다.
            num_beams=5,  # 빔 서치를 사용하여 더 나은 결과를 찾습니다.
            do_sample=True  # 샘플링 모드를 사용합니다.
        )
        print(f"Generated output IDs: {output}")

        # 생성된 응답을 디코딩합니다.
        response_text = tokenizer.decode(output[0], skip_special_tokens=True)
        response_text = response_text.replace("\n", " ").strip()  # 불필요한 줄바꿈 및 공백 제거
        print(f"KoGPT-2 response: {response_text}")

        # 메시지와 응답을 MongoDB에 저장합니다.
        db.chats.insert_one({
            'message': user_message,
            'response': response_text
        })

        # 응답을 클라이언트에게 JSON 형식으로 반환합니다.
        return jsonify({'response': response_text})
    except Exception as e:
        print(f"General error: {e}")  # 에러가 발생한 경우 에러 메시지를 출력합니다.
        return jsonify({'error': str(e)}), 500  # 에러 응답을 클라이언트에게 반환합니다.

if __name__ == '__main__':
    app.run(port=5000)  # Flask 애플리케이션을 5000번 포트에서 실행합니다.
