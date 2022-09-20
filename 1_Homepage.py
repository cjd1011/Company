import streamlit as st

st.set_page_config(
     page_title="BBIS Corp",
     page_icon=":moneybag:",
     layout="wide",
     initial_sidebar_state="expanded",
     #menu_items={
         #'Get Help': 'https://www.extremelycoolapp.com/help',
         #'Report a bug': "https://www.extremelycoolapp.com/bug",
         #'About': "# This is a header. This is an *extremely* cool app!"
     #}
 )

st.title('Welcome to BBIS Corp:chart_with_upwards_trend:')
st.subheader('Best Business Intelligence Solutions')

st.text("Our company is focused on improve your business performance with technological solutions")


st.markdown('---')


col1, col2, col3 = st.columns(3)

with col1:
    st.subheader("Improve Processes")
    st.image("Process.jpg")

with col2:
    st.subheader("Data Visualization")
    st.image("dashboard.jpg")

with col3:
    st.subheader("Corporate Finance")
    st.image("Corporate2.jpg")

    
st.markdown("---")
    
st.subheader("How we do it?")

col4, col5, col6 = st.columns(3)

with col4:
    st.subheader("Diagnosis")
    st.image("diagnosis.jpg")

with col5:
    st.subheader("Development")
    st.image("development.jpg")

with col6:
    st.subheader("Implementation")
    st.image("implementation.jpg")

#st.text("We make a business diagnosis to determinate what is the best option for YOU")



#Diagnosis
#Development
#Implementation