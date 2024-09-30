import streamlit as st
import pandas as pd
from datetime import datetime as dt
import datetime



button = st.button ('버튼을 눌러보세요')
if button:
  st.write (':blue[버튼]이 눌렸습니다. :sparkles:')
dataframe = pd.DataFrame({
  'first column ' : ['kor','eng','math','science'],
  'second column': [10, 20, 30, 40]
})
st.download_button(
    label='CSV로 성적표 다운로드',
    data=dataframe.to_csv(), 
    file_name='sample.csv',
    mime='text/csv'
)                 
agree =st.checkbox('동의 하십니까?')
if agree:
  st.write('동의 해주셔서 감사합니다 :100:')
  mbti =st.radio(
  '당신이 좋아하는 선수는 누구인가요?',
  ('손흥민','르브론 제임스','김연경','메이웨더'))
  if mbti == 'ISTJ':
    st.write('당신은 :blue[축구팬] 이시네요')
  elif mbti == 'ENFP':
    st.write('당신은 :green[농구팬] 이시네요')
  else:
    st.write("당신은 :red[배구팬]: 이시네요')
    else
             st.write("당신은 :yellow[복싱팬]: 이시네요')
    
    
