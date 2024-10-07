import streamlit as st
import random
import datetime

# 제목 설정
st.title(':sparkles:로또 생성기 & 스포츠 선택:sparkles:')

# 로또 번호 생성 함수
def generate_lotto():
    lotto = set()
    while len(lotto) < 6:
        number = random.randint(1, 45)
        lotto.add(number)
    
    lotto = list(lotto)
    lotto.sort()  # 정렬
    return lotto

# 사용자에게 운동 성향을 선택하도록 셀렉트박스 제공
options = ['단체 운동', '개인 운동', '야외 운동']
selected_option = st.selectbox('어떤 운동이 좋으세요?', options)

# 운동 종목 추천
if selected_option == '단체 운동':
    sports = ['축구', '농구', '배구', '야구', '하키', '럭비', '크리켓', '핸드볼', '스쿼시', '체육관 그룹 수업']
elif selected_option == '개인 운동':
    sports = ['테니스', '탁구', '수영', '복싱', '주짓수', '킥복싱', '요가', '필라테스', '스케이팅', '레슬링']
else:  # 야외 운동
    sports = ['사이클', '조깅', '하이킹', '서핑', '골프', '캠핑', '패러글라이딩', '클라이밍', '스노우보드', '승마']

# 선택한 운동 종목을 랜덤으로 추천
recommended_sport = random.choice(sports)

# 추천 결과 출력
st.write(f"추천하는 운동 종목: :blue[{recommended_sport}]")

# 로또 번호 생성 버튼
button = st.button('로또를 생성해 주세요!')
if button:
    for i in range(1, 6):
        st.subheader(f'{i}. 행운의 번호: :green[{generate_lotto()}]')
    
    st.write(f"생성된 시각: {datetime.datetime.now().strftime('%Y-%m-%d %H:%M')}")
