# 올라마 모델 llama3.1:8b

## 참고자료
* 유튜브 : https://www.youtube.com/watch?v=VkcaigvTrug&t=80s
* 유튜버 예시 코드 : https://github.com/teddylee777/langserve_ollama
* 랭체인 kr : https://github.com/teddylee777/langchain-kr
* 모델 : llama3.1:8b

## 모델파일의 설정 변경 반영
ollama create llama3.1:8b /Users/dev/GitHub/chatbotchallenge/ollama_windowmodel/Modelfile

## 올라마 실행
ollama run llama3.1:8b

## 서버 실행
cd /Users/dev/Documents/GitHub/chatbotchallenge/ollama_window/app
python server.py

## 가상환경
1. 시작 : conda activate chatbot_env
2. 종료 : conda deactivate

## 경로
1. cd /Users/dev/Documents/GitHub/chatbotchallenge/ollama_window

## 가상환경

cd C:\Users\dev\Documents\GitHub\chatbotchallenge\ollama_window
chatbot_env\Scripts\activate

종료 : deactivate

## 로컬 주소 

http://localhost:8000/