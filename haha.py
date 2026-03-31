import os
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI

# 1. .env 파일의 환경변수 로드
load_dotenv()

# 2. 모델 초기화 (GPT-4o mini 등 원하는 모델 선택)
llm = ChatOpenAI(model="gpt-4o-mini")

# 3. 질문 던지기
response = llm.invoke("안녕! 너는 누구니?")

# 4. 결과 출력
print(f"답변: {response.content}")