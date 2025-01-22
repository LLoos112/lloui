# streamlit_app.py
!pip install matplotlib
import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


st.title("Streamlit Demo Application")
st.write("This is a simple demonstration of Streamlit capabilities.")

# Sidebar
st.sidebar.header("User Input")
user_name = st.sidebar.text_input("Enter your name:", "Guest")
data_points = st.sidebar.slider("Number of data points:", min_value=10, max_value=500, value=100)
chart_type = st.sidebar.selectbox("Choose chart type:", ["Line", "Bar", "Area"])


st.write(f"Hello, **{user_name}!** Let's explore some data!")

# Generate random dataset
data = pd.DataFrame({
    "X": np.arange(1, data_points + 1),
    "Y": np.random.randn(data_points).cumsum()
})

# Display data
st.subheader("Generated Dataset")
st.dataframe(data)

# Descriptive stats
st.subheader("Basic Data Statistics")
st.write(data.describe())

# Visualization
st.subheader("Data Visualization")
if chart_type == "Line":
    st.line_chart(data.set_index("X"))
elif chart_type == "Bar":
    st.bar_chart(data.set_index("X"))
elif chart_type == "Area":
    st.area_chart(data.set_index("X"))

# Matplotlib plot
st.subheader("Matplotlib Plot")
fig, ax = plt.subplots()
ax.plot(data["X"], data["Y"], label="Cumulative Sum", color="blue", alpha=0.7)
ax.set_title("Matplotlib Plot")
ax.set_xlabel("X")
ax.set_ylabel("Y")
ax.legend()
st.pyplot(fig)

# Footer
st.write("Thank you for using this demo! 🎉")
