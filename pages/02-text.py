import streamlit as st


st.title('대한민국 1등 커뮤니티')



st.title('스마일 :sunglasses:')


st.header('대한민국 최고의 커뮤니티 :sparkles:')


st.subheader(' 대한민국의 자랑')




st.caption('캡션은 짧은 설명을 추가하는 것!')


sample_code = '''
def function():
    print("life is too short,you need the python")
'''
st.code(sample_code, language="python")


st.text('이 커뮤니티는 인스타그램을 뛰어넘을 것입니다.')


st.markdown('streamlit은 **마크다운 문법을 지원 **합니다.')

st..markdown("텍스트의 색상을 green[초록색]으로, 그리고 **blue[파란색]** 볼트체로 설정할 수 있습니다.")
st.markdown("green[$/sqrt{1+1}=2$'] 와 같이 latex 문법의 수식 표현도 가능합니다 :pencil")


st.latex(r' \sqrt{1+1}=2')
