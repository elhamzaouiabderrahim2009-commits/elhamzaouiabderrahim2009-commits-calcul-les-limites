import streamlit as st
from sympy import symbols, limit, sympify, oo

st.title("حاسبة النهايات")

x = symbols('x')
func = st.text_input("الدالة:", "(x**2 - 1)/(x - 1)")
point = st.text_input("النهاية عند:", "1")

if st.button("احسب"):
    try:
        f = sympify(func)
        p = oo if point == "oo" else float(point)
        st.success(f"النتيجة: {limit(f, x, p)}")
    except Exception as e:
        st.error(f"خطأ: {e}")
