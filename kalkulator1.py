import streamlit as st

#Header
st.header('Syerlina :sparkles:')
st.subheader('Plot')

c1, c2, c3, c4 = st.columns(4)

with c1:
  x = st.number_input('x ', value=0)
with c2:
    operan = st.selectbox(
      'Operan',
      ('+', '-', ':', 'x'),key='k1')
with c3:
  y = st.number_input('y ', value=0)
with c4:
  z = st.number_input('z ', value=0)
  if(operan=='+'):
    st.write('= ', x+y)
  if(operan=='-'):
    st.write('= ', x-y)
  if(operan==':'):
    st.write('= ', x/y)
  if(operan=='x'):
    st.write('= ', x*y)
  
st.write(x, ' ', operan, y, ' ', '=', ' ')
