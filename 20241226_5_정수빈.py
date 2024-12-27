import os
from datetime import datetime

# OpenAI API Key 설정
os.environ['OPENAI_API_KEY'] = ''

# 오늘 날짜 반환 함수
def get_today():
    return datetime.now().strftime("%B %d")

# 템플릿 설정
from langchain.prompts import PromptTemplate
template = "오늘의 날짜는 {today} 입니다. 오늘이 생일인 {star}를 나열해 주세요."

prompt = PromptTemplate(
    template=template,
    input_variables=["star"],
    partial_variables={"today": get_today}
)

# 모델 설정
from langchain_openai import ChatOpenAI
model = ChatOpenAI(
    model="gpt-4o",  # GPT-4로 변경
    max_tokens=3000,  # 필요에 따라 토큰 길이 설정
    temperature=0.1
)


# 체인 생성
chain = prompt | model

# 체인 실행
response = chain.invoke({"star"}).content

# 날짜를 강제로 추가 
if "오늘의 날짜는" not in response:
    response = f"오늘의 날짜는 {get_today()} 입니다.\n\n{response}"
print(response)
