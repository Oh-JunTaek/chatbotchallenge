# app.py
from flask import Flask, request, jsonify
import datetime

app = Flask(__name__)

# 사진 업로드 기록을 저장할 임시 저장소 (데이터베이스 대신 사용)
upload_records = {}

@app.route('/')
def home():
    return "Hello, this is the KakaoTalk chatbot!"

@app.route('/upload_photo', methods=['POST'])
def upload_photo():
    data = request.json
    user = data.get('user')
    if not user:
        return jsonify({"error": "User not specified"}), 400
    upload_records[user] = datetime.datetime.now()
    return jsonify({"message": f"Photo uploaded by {user}"}), 200

@app.route('/check_uploads', methods=['GET'])
def check_uploads():
    now = datetime.datetime.now()
    not_uploaded_users = [user for user, time in upload_records.items() if (now - time).days >= 1]
    return jsonify({"not_uploaded_users": not_uploaded_users}), 200

if __name__ == '__main__':
    app.run(debug=True)
