import streamlit as st

st.title("Streamlit 배포 테스트")
st.write("안녕하세요! 이 앱은 배포 테스트를 위한 간단한 Streamlit 앱입니다.")

name = st.text_input("이름을 입력하세요:")
if name:
    st.write(f"반갑습니다, {name}님!")
