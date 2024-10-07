import streamlit as st
import random
import datetime

st.title(':sparkled:로또 생성기:sparkles:')



def gemerate_lotto():
  lotto = set()
  while len(lotto) < 6:
    number = random.randint(1, 46)
    lotto.add(number)
    lotto =list(lotto)
    lotto.sort()
    return lotto
        
