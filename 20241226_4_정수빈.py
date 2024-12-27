import os 

os.environ['OPENAI_API_KEY'] = '' 
from langchain_teddynote.messages import stream_response
from langchain_core.prompts import PromptTemplate
from langchain.prompts import PromptTemplate
from langchain_openai import ChatOpenAI

model = ChatOpenAI(
      model ="gpt-3.5-turbo",
      max_tokens=2048,
      temperature=0.1,
)

# template 정의
template = "{country1}과 {country2}의 수도는 어디인가요?"

# PromptTemplate 객체 생성
prompt = PromptTemplate(
    template=template,
    input_variables=["country1"],      
    partial_variables={"country2": "미국"},  
)
prompt.format(country1="대한민국")
prompt_partial = prompt.partial(country2="미국")

chain = prompt_partial | model

a = chain.invoke({'country1':'대한민국','country2':"호주"}).content
print(a)
