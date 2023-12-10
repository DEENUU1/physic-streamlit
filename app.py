import streamlit as st
from horizontal import create_trajectory_dataframe, HorizontalProjection

st.title("Calculate Horizontal Projection")

st.sidebar.number_input("v0 = ...", key="v0", value=None)
st.sidebar.number_input("t = ...", key="t", value=None)
st.sidebar.number_input("h0 = ...", key="h0", value=None)
st.sidebar.number_input("s = ...", key="s", value=None)

v0 = st.session_state.v0
t = st.session_state.t
ho = st.session_state.h0
s = st.session_state.s


def get_result():
    hp = HorizontalProjection(v0=v0, t=t, h0=ho, s=s)
    return hp


def get_dataframe():
    hp = HorizontalProjection(v0=v0, t=t, h0=ho, s=s)
    return create_trajectory_dataframe(hp)


result_load_state = st.text("Loading data...")
result = get_result().calc()
result_load_state.text("Done!")
st.write(result)

dataframe_load_state = st.text("Loading data...")
dataframe = get_dataframe()
dataframe_load_state.text("Done!")

st.line_chart(dataframe, x="X", y="Y")
