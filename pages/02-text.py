import streamlit as st


st.title('대한민국을 소개합니다.')



st.title('스마일 :sunglasses:')


st.header('대한민국은 동경 124도와 132도 사이, 북위 33도와 43도 사이, 유라시아 대륙 동쪽, 북태평양 북서쪽에 위치한 반도 국가입니다 :sparkles:')


st.subheader('수도: 서울특별시
출산율: 0.81 명(여성 1인당) (2021년) 세계은행
인구: 7744만 (2024년) 
정부: 단일 국가, 대통령제, 입헌 공화국
국내총생산: 1.674조 USD (2022년) 세계은행
통화: 대한민국 원
대통령: 윤석열
면적:223,663㎢
')




st.caption('대한민국 시민인걸 자랑스럽게 생각하세요!')


sample_code = '''
def function():
    print("life is too short,you need the python")
'''
st.code(sample_code, language="python")


st.text('이 커뮤니티는 인스타그램을 뛰어넘을 것입니다.')


st.markdown('streamlit은 **마크다운 문법을 지원 **합니다.')

st.markdown("텍스트의 색상을 :green[초록색]으로, 그리고 **:blue[파란색]** 볼트체로 설정할 수 있습니다.")
st.markdown(":green[$/sqrt{1+1}=2$'] 와 같이 latex 문법의 수식 표현도 가능합니다 :pencil")


st.latex(r' \sqrt{1+1}=2')
