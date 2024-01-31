import numpy as np
import matplotlib.pyplot as plt
import streamlit as st

# --Header--
st.header('ojotakon : sparkles')
st.subheader('plot')

x = np.linspace(-2 * np.pi, 2 * np.pi, 1000) 
y = np.sin(x)
z = np.cos(x)

fig, ax = plt.subplots(figsize=(16, 8))
ax.plot(x, y, label='sin(x)', color='b')
ax.plot(x, y, label='cos(x)', color='g')
ax.set_ylabel("")
ax.set_xlabel("x")
ax.tick_params(axis='y', labelsize=20)
ax.set_xticklabels(ax.get(xticklabels(), rotation=30, ha='right')
ax.tick_params(axis='x', labelsize=15)

st.pyplot(fig)
