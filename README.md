# 챗봇 개발을 위한 기술 및 과정

## 프로젝트 소개 및 목적
* 이 챗봇개발은 개인의 학습을 위해 제작되었습니다.
* 이 프로젝트를 통해 '챗봇이 만들어 지는 과정', '챗봇을 만드는 방법', 'gpt모델을 학습시키는 방법', '데이터의 전처리 및 활용', '파인튜닝', '프레임워크 활용하기', '제작 및 베포' 등을 학습할 수 있습니다.

## 진행과정 및 방향
 1. chatbot2(파인튜닝1차시기)
* gpt2에 첫 훈련을 시켜보았고 챗봇으로 구현해본 결과 훈련상태에 이상이 있음을 확인[2024/06/24]
* 재훈련을 위해 chatbot3로 다시 재교육 시작. [2024/06/25]

 2. chatbot3(파인튜닝 2차시기)
* gpt2에 새로운 코드를 적용하여 훈련 시작. 훈련시간 이상으로 중간과정을 확인 및 코드점검이 필요[2024/06/25]

## 프로젝트의 구조 및 주요 구성요소

## 설치 및 실행 방법

## 사용 예시 및 데모
[2024/06/25]
![image](https://github.com/Oh-JunTaek/ChatBot/assets/143782929/2059090d-5bcf-45ab-82c0-17dab2da410e)
{"question": "In what city and state did Beyonce  grow up? ", "id": "56bf6b0f3aeaaa14008c9601", "answers": [{"text": "Houston, Texas", "answer_start": 166}], "is_impossible": false},
![image](https://github.com/Oh-JunTaek/ChatBot/assets/143782929/f49f7eb3-9c19-4870-a050-b4f8edbb7126)


## 기여방법

## 프로젝트 로드맵
* 주요 마일스톤
 - 6월 24일 프로젝트 기획 완료
 - 6월 25일 첫 훈련모델 완료
## 연락처 및 지원

## 필요한 기술
1. 자연어 처리(NLP): 사용자의 입력 문장을 이해하고 분석하는 기술이 필요합니다.
대표적인 라이브러리: NLTK, spaCy, Hugging Face Transformers 등
2. 대화 관리: 사용자의 질문에 적절한 응답을 생성하고 대화 흐름을 관리하는 기술이 필요합니다.
대화 흐름 관리, 문맥 이해, 질문 답변 생성 등
3. 기계 학습/딥러닝: 챗봇의 지능을 높이고 자연스러운 대화를 생성하기 위해 기계 학습 기술이 필요합니다.
대표적인 모델: seq2seq, transformer, GPT 등
4. 데이터베이스: 대화 내용, 사용자 정보, 지식 베이스 등을 저장하고 관리하는 데이터베이스 기술이 필요합니다.
관계형 데이터베이스, NoSQL 데이터베이스 등
5. API 개발: 사용자 인터페이스, 외부 서비스 연동 등을 위한 API 개발 기술이 필요합니다.
Flask, Django, FastAPI 등의 웹 프레임워크 활용
6. 배포 및 운영: 챗봇 서비스를 안정적으로 운영하기 위한 배포, 모니터링, 유지보수 기술이 필요합니다.
Docker, Kubernetes, CI/CD 등의 DevOps 기술 활용

## 챗봇 개발 과정
1. 요구사항 분석: 챗봇의 목적, 사용자, 기능 등을 정의합니다.
2. 데이터 수집 및 전처리: 대화 데이터, 지식 베이스 등을 수집하고 정제합니다.
3. 모델 설계 및 구현: 대화 관리, 질문 답변 생성 등을 위한 모델을 설계하고 구현합니다.
4. API 개발: 사용자 인터페이스, 외부 서비스 연동 등을 위한 API를 개발합니다.
5. 테스트 및 디버깅: 챗봇의 기능, 성능, 안정성 등을 테스트하고 필요한 수정을 합니다.
6. 배포 및 운영: 챗봇 서비스를 안정적으로 배포하고 운영합니다.
7. 모니터링 및 개선: 사용자 피드백을 수집하고 지속적으로 챗봇을 개선합니다.
8. 이와 같은 기술과 과정을 통해 효과적인 챗봇을 개발할 수 있습니다. 

## License

This work is licensed under the Apache License 2.0 and the Creative Commons Attribution-ShareAlike 4.0 International (CC BY-SA 4.0) License.

The Apache License 2.0 applies to the GPT-2 model provided by OpenAI.
The Creative Commons Attribution-ShareAlike 4.0 International (CC BY-SA 4.0) License applies to the SQuAD dataset provided by Rajpurkar et al.
