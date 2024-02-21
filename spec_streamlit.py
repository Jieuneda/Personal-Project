import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

mkt_grad_fin = pd.read_csv('mkt_grad_fin.csv')
mkt_language_fin = pd.read_csv('mkt_language_fin.csv')
mkt_major_fin = pd.read_csv('mkt_major_fin.csv')
mkt_tool_fin = pd.read_csv('mkt_tool_fin.csv')

mkt_first = pd.read_csv('mkt_first.csv')


import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt


st.set_page_config(page_title='채용공고 기반 스펙 추천 시스템',  layout='wide', page_icon=':parrot:')

# Streamlit 애플리케이션의 제목 설정
st.title('🦜Welcome to 스펙 추천 시스템🦜')

st.write('')
st.markdown("직무 준비에 필요한 스펙을 추천해드릴게요!😊")

# st.markdown("<hr>", unsafe_allow_html=True)

# 카테고리 선택

categories = ['서비스 설명서','마케팅', '디자인', '무역', '건축', '토목', '회계']


st.sidebar.image("./jobkorea_pic 2.jpg", use_column_width=True )

st.sidebar.write('##### made by. 김지은')

st.sidebar.write('')

selected_category = st.sidebar.selectbox('직무를 선택하세요:', categories)

st.sidebar.header(("About"))
st.sidebar.markdown((
    "[잡코리아](https://www.jobkorea.co.kr/) 하위 서비스인 '채용공고 기반 스펙 추천 서비스'입니다."
))
    
st.sidebar.header(("Resources"))
st.sidebar.markdown((
    """
- [JOBKOREA 바로가기](https://www.jobkorea.co.kr/)    
- [JOBKOREA 직무별 채용공고](https://www.jobkorea.co.kr/recruit/joblist?menucode=duty)
- [JOBKOREA TOP100 채용공고](https://www.jobkorea.co.kr/top100/)
- [JOBKOREA 합격자소서](https://www.jobkorea.co.kr/starter/passassay)
"""
))

if selected_category == '서비스 설명서':
    st.write('')
    st.write('#### 안녕하세요. JOBKOREA 스펙 추천 서비스에 오신 것을 환영합니다.')
    st.write('취업과 진로 선택은 여러분의 미래를 좌우하는 중요한 순간입니다.')
    st.write('JOBKOREA 스펙 추천 서비스는 여러분이 원하는 직무에 필요한 스펙을 채용 공고를 기반으로 추천해주는 서비스입니다.')
    st.write('')
    st.write('')
    st.write('### 사용 설명서')
    st.write('')
    st.write('##### 1. 왼쪽 사이드바에서 스펙을 추천 받고자 하는 직무를 선택하세요.')
    st.write('')
    st.write("##### 2. '1순위 스펙🥇'를 클릭하면 해당 직무의 공고에서 가장 많이 언급된 스펙을 알려드려요.")
    st.write('')
    st.write("##### 3. '스펙 상세보기'를 클릭하면 스펙 종류 별 순위를 보여드려요.")
    st.write('')
    st.write('※ 업데이트 된 시점까지의 채용공고를 기반으로 스펙을 분석해서 보여드립니다.')

if selected_category == '마케팅':
    
    # st.write('마케팅 직무에 필요한 스펙을 요약해드릴게요!')
    
    tab1, tab2= st.tabs(["1순위 스펙🥇", "스펙 상세보기🧐"])
    
    with tab1:
    
        st.markdown("### '마케팅' 공고에서 가장 많이 언급된 스펙을 알려드릴게요.")
    
    
        # m2, m3, m4, m5 = st.columns((1,1,1,1))
    
        # m2.metric(label='학력', value=mkt_first['학력'].iloc[0])
        # m3.metric(label='언어', value=mkt_first['언어'].iloc[0])
        # m4.metric(label='전공', value=mkt_first['전공'].iloc[0])
        # m5.metric(label='기술', value=mkt_first['기술'].iloc[0])
        
        st.write("  ")
        st.markdown(f"#### 👑 학력: {mkt_first['학력'].iloc[0]}")
        st.markdown(f"#### 👑 언어: {mkt_first['언어'].iloc[0]}")
        st.markdown(f"#### 👑 전공: {mkt_first['전공'].iloc[0]}")
        st.markdown(f"#### 👑 기술: {mkt_first['기술'].iloc[0]}")


    with tab2:
        st.markdown("### '마케팅' 직무에서 선호하는 스펙을 보여드릴게요.")
    
        b1, b2, b3, b4 = st.columns((1,1,1,1))
    
        b1.markdown('### 🏫학력')
        b2.markdown('### 🆎언어')
        b3.markdown('### 📒전공')
        b4.markdown('### 🖥️기술')
    
        a1, a2, a3, a4 = st.columns((1,1,1,1))
    
        a1.dataframe(mkt_grad_fin,hide_index="True")
        a2.dataframe(mkt_language_fin,hide_index="True")
        a3.dataframe(mkt_major_fin,hide_index="True")
        a4.dataframe(mkt_tool_fin,hide_index="True")
    
    
  