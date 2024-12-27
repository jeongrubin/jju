from langchain_core.prompts import PromptTemplate
from langchain_openai import ChatOpenAI
import os 

os.environ['OPENAI_API_KEY'] = '' 


from langchain_core.prompts import PromptTemplate
from langchain_openai import ChatOpenAI

# template 정의
template = "{topic}은 어떤 학교인가요?"

# Prompt객체 생성
prompt_template = PromptTemplate.from_template(template)

# OpenAI 모델 
model = ChatOpenAI(
    model="gpt-3.5-turbo",
    max_tokens=2048,
    temperature=0.1,
)

# chain 생성
chain = prompt_template | model

# chain 실행
input= {"topic": "전주대 인공지능학과 "}
response = chain.invoke(input)  

print(response)