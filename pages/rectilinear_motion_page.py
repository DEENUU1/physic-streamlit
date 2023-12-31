import streamlit as st
from calcs.rectilinear_motion import (
    calculate_displacement,
    calculate_average_speed,
    calculate_avg_acceleration,
    calculate_free_fall_ending_speed,
    calculate_free_fall_total_time,
    free_fall_trajectory
)

st.set_page_config(
    page_title="Physic streamlit - Rectilinear motion",
    page_icon="icon.png",
)

st.title("Calculate Rectilinear Motion")
st.subheader("Displacement")
with st.container():
    col1, col2 = st.columns(2)

    with col1:
        st.number_input("Starting position", key="xs_displacement")
    with col2:
        st.number_input("Ending position", key="xk_displacement")

xs_displacement = st.session_state.xs_displacement
xk_displacement = st.session_state.xk_displacement

if xs_displacement and xk_displacement:
    with st.spinner("Wait for it..."):
        data = calculate_displacement(xs_displacement, xk_displacement)
        st.success(f"Displacement: {data} m")

st.subheader("Average speed")
with st.container():
    col1, col2 = st.columns(2)

    with col1:
        st.number_input("Starting position", key="xs_speed")
        st.number_input("Ending position", key="xe_speed")
    with col2:
        st.number_input("Ending time", key="te_speed")
        st.number_input("Starting time", key="ts_speed")

xs_speed = st.session_state.xs_speed
xe_speed = st.session_state.xe_speed
te_speed = st.session_state.te_speed
ts_speed = st.session_state.ts_speed

if xs_speed and xe_speed and te_speed and ts_speed:
    with st.spinner("Wait for it..."):
        data = calculate_average_speed(xs_speed, xe_speed, te_speed, ts_speed)
        st.success(f"Average speed: {data} m/s")

st.subheader("Average acceleration")

with st.container():
    col1, col2 = st.columns(2)
    with col1:
        st.number_input("Starting position", key="xs_acceleration")
        st.number_input("Ending position", key="xe_acceleration")
    with col2:
        st.number_input("Ending time", key="te_acceleration")
        st.number_input("Starting time", key="ts_acceleration")

xs_acceleration = st.session_state.xs_acceleration
xe_acceleration = st.session_state.xe_acceleration
te_acceleration = st.session_state.te_acceleration
ts_acceleration = st.session_state.ts_acceleration

if xs_acceleration and xe_acceleration and te_acceleration and ts_acceleration:
    with st.spinner("Wait for it..."):
        data = calculate_avg_acceleration(xs_acceleration, xe_acceleration, te_acceleration, ts_acceleration)
        st.success(f"Average acceleration: {data} m/s2")

st.subheader("Free fall ending speed")
st.number_input("Starting height", key="h_speed")
st.number_input("Acceleration of gravity ", key="g_speed", value=9.81)

h_speed = st.session_state.h_speed
g_speed = st.session_state.g_speed

if h_speed and g_speed:
    with st.spinner("Wait for it..."):
        data = calculate_free_fall_ending_speed(h_speed, g_speed)
        st.success(f"Free fall ending speed: {data} m/s")

st.subheader("Free fall total time")
with st.container():
    col1, col2 = st.columns(2)
    with col1:
        st.number_input("Starting height", key="h_time")
    with col2:
        st.number_input("Acceleration of gravity ", key="g_time", value=9.81)

h_time = st.session_state.h_time
g_time = st.session_state.g_time
if h_time and g_time:
    with st.spinner("Wait for it..."):
        data = calculate_free_fall_total_time(h_time, g_time)
        st.success(f"Free fall total time: {data} s")

st.subheader("Free fall trajectory")
with st.container():
    col1, col2 = st.columns(2)
    with col1:
        st.number_input("Total time", key="t_trajectory")
    with col2:
        st.number_input("Acceleration of gravity ", key="g_trajectory", value=9.81)

t_trajectory = st.session_state.t_trajectory
g_trajectory = st.session_state.g_trajectory

if t_trajectory and g_trajectory:
    with st.spinner("Wait for it..."):
        data = free_fall_trajectory(t_trajectory, g_trajectory)
        st.line_chart(data, x="time", y="speed")
