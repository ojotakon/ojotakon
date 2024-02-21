import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

x = st.slider('Pilih rentang', 0.0, 2.0, (.2, .5))
st.write('nilai x:', x)
y = st.slider('Set nilai',0.0, 10.0, 6.0)
st.write('nilai y:', y)

t = np.linspace(x[0]*np.pi,x[1]*np.pi,100)
u = np.sin(y*t)
#st.write('nilai t:', t)

fig, ax = plt.subplots(figsize=(16, 8))
ax.plot(t, u, label='sin(t)', color='b')
ax.set_ylabel("")
ax.set_xlabel("t")
ax.tick_params(axis='y', labelsize=20)
ax.set_xticklabels(ax.get_xticklabels(), rotation=30, ha='right')
ax.tick_params(axis='x', labelsize=15)
plt.grid(color='green', linestyle='-.', linewidth=.5)
st.pyplot(fig)

def f(x):
  a = 19
  b = 25
  c = 5
  return a*x*x+b*x-c

x = st.slider('Pilih rentang', -10, 10, (2, 5))
st.write('nilai x:', x)

t = np.linspace (x[0], x[1], 100)
u = f(t)
fig, ax = plt.subplots(figsize=(16, 8))
ax.plot(t, u, label='sin(t)', color='b')
ax.set_ylabel("")
ax.set_xlabel("t")
ax.tick_params(axis='y', labelsize=20)
ax.set_xticklabels(ax.get_xticklabels(), rotation=30, ha='right')
ax.tick_params(axis='x', labelsize=15)
plt.grid(color='green', linestyle='-.', linewidth=.5)
st.pyplot(fig)

import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

# Fungsi yang akan diintegrasikan
def f(x):
    a = 19
    b = 25
    c = 5
    return a*x*x + b*x - c

# Metode trapesium untuk integral
def trapezoidal_rule(f, a, b, n=100):
    x = np.linspace(a, b, n+1)
    y = f(x)
    h = (b - a) / n
    s = 0.5 * (y[0] + y[-1]) + np.sum(y[1:-1])
    return h * s

# Streamlit sliders untuk fungsi sin(t)
x = st.slider('Pilih rentang untuk sin(t)', 0.0, 2.0, (.2, .5))
st.write('Nilai x:', x)
y = st.slider('Set nilai untuk sin(t)', 0.0, 10.0, 6.0)
st.write('Nilai y:', y)

t = np.linspace(x[0]*np.pi, x[1]*np.pi, 100)
u = np.sin(y*t)

fig, ax = plt.subplots(figsize=(16, 8))
ax.plot(t, u, label='sin(t)', color='b')
ax.set_xlabel("t")
plt.grid(color='green', linestyle='-.', linewidth=.5)
st.pyplot(fig)

# Streamlit sliders untuk fungsi polinomial
x_range = st.slider('Pilih rentang untuk fungsi polinomial', -10, 10, (2, 5))
st.write('Nilai x:', x_range)

t = np.linspace(x_range[0], x_range[1], 100)
u = f(t)
fig, ax = plt.subplots(figsize=(16, 8))
ax.plot(t, u, label='f(x) = 19x^2 + 25x - 5', color='b')
ax.set_xlabel("t")
plt.grid(color='green', linestyle='-.', linewidth=.5)
st.pyplot(fig)

# Integral menggunakan metode trapesium
integral_range = st.slider('Pilih rentang untuk integral fungsi polinomial', -10.0, 10.0, (1.0, 3.0))
integral_result = trapezoidal_rule(f, integral_range[0], integral_range[1])
st.write(f"Hasil integral dari fungsi polinomial pada rentang {integral_range} adalah: {integral_result}")
