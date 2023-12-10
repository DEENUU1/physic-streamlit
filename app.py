import streamlit as st
from horizontal import create_trajectory_dataframe, HorizontalProjection

st.title("Calculate Horizontal Projection")

st.sidebar.write(
    "Add 2 values to get result (g doesn't count), remember about the relevant units (t - seconds, h0 - meters, v0 - meters per seconds, s - meters"
)
st.sidebar.number_input("g = (you don't need change this value)", key="g", value=9.81)
st.sidebar.number_input("v0 = ...", key="v0", value=None)
st.sidebar.number_input("t = ...", key="t", value=None)
st.sidebar.number_input("h0 = ...", key="h0", value=None)
st.sidebar.number_input("s = ...", key="s", value=None)

v0 = st.session_state.v0
t = st.session_state.t
ho = st.session_state.h0
s = st.session_state.s
g = st.session_state.g


def get_result():
    hp = HorizontalProjection(v0=v0, t=t, h0=ho, s=s, g=g)
    return hp


def get_dataframe():
    hp = HorizontalProjection(v0=v0, t=t, h0=ho, s=s, g=g)
    return create_trajectory_dataframe(hp)


def enough_values():
    counter = {"v0": v0, "t": t, "h0": ho, "s": s}

    res = 0
    for value in counter.values():
        if value:
            res += 1

    return res


ev = enough_values()

if ev == 2:

    with st.spinner('Wait for it...'):
        data = get_result()
        dataframe = get_dataframe()

    calc = data.calc()
    st.subheader(f"Starting speed: {calc["v0"]} m/s")
    st.subheader(f"Total time: {calc['t']} s")
    st.subheader(f"Starting height: {calc['h0']} m")
    st.subheader(f"Total distance: {calc['s']} m")
    st.line_chart(dataframe, x="X", y="Y")


elif ev < 2:
    st.info("Add at least 2 numbers to get result (g value doesn't count)")
else:
    st.exception("Too many values you can only add 2 (g value doesn't count)")
