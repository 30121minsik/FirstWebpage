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
  sports = st.radio(
  '당신이 좋아하는 선수는 누구인가요?',
  ('손흥민', '르브론 제임스', '메이웨더'))
  
  if sports == '손흥민':
    st.write('당신은 :blue[축구팬] 이시네요')
  elif sports == '르브론 제임스':
    st.write('당신은 :green[농구팬] 이시네요')
  else sports =='메이웨더':
    st.write('당신은 :red[복싱팬]: 이시네요')
title = st.text_input(
  label='가고 싶은 여행지가 있나요?',
  placeholder='여행지를 입력해 주세요'
)
st.write(f'당신이 선택한 여행지: :violet[{title}]')
values = st.slider(
  '범위의 값을 다음과 같이 지정할 수 있어요:sparkles:',
  st.write('선택 범위:',values)
    
    
