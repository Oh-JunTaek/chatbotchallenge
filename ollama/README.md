# 올라마 모델 EEVE-Korean-10.8B

## 참고자료
* 유튜브 : https://www.youtube.com/watch?v=VkcaigvTrug&t=80s
* 유튜버 예시 코드 : https://github.com/teddylee777/langserve_ollama
* 랭체인 kr : https://github.com/teddylee777/langchain-kr
* 모델 : https://huggingface.co/yanolja/EEVE-Korean-Instruct-10.8B-v1.0

## 모델파일의 설정 변경 반영
ollama create EEVE-Korean-10.8B -f /Users/eunma/Documents/model/Modelfile

## 올라마 실행
ollama run EEVE-Korean-10.8B:latest

## 서버 실행
cd /Users/eunma/Documents/GitHub/chatbotchallenge/ollama/app
python server.py

## 가상환경
1. 시작 : conda activate chatbot_env
2. 종료 : conda deactivate

## 경로
1. cd /Users/eunma/Documents/GitHub/langserve_ollama
