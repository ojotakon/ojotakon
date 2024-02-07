import streamlit as st

#Header
st.header('Syerlina :sparkles:')
st.subheader('Plot')

c1, c2, c3, c4 = st.columns(4)

with c1:
  x = st.number_input('Variabel kesatu ', value=100)
with c2:
    operan = st.selectbox(
      'Operan',
      ('+', '-', '/', 'x')
with c3:
  y = st.number_input('Variabel kedua ', value=100)
with c4:
  z = st.number_input('hasil ', value=100)
  st.write('=>: ')
  
st.write(x, ' ', operan, ' ', hasil, ' = ')
