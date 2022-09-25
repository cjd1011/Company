import streamlit as st

st.set_page_config(
     page_title="BBIS Corp - Portfolio",
     page_icon=":moneybag:",
     layout="wide",
     initial_sidebar_state="expanded",
     #menu_items={
         #'Get Help': 'https://www.extremelycoolapp.com/help',
         #'Report a bug': "https://www.extremelycoolapp.com/bug",
         #'About': "# This is a header. This is an *extremely* cool app!"
     #}
 )


st.title("Our Business Intelligence Portfolio")

st.header("Improve Processes")

col1, col2, col3 = st.columns(3)

with col1:

    st.subheader(" 1. Review processes")

    st.image("Organice.jpg")

    st.caption("Understanding and reviewing processes")
    #st.caption("      Reviewing the process")         
                    
            
        
with col2:       

    st.subheader(" 2. Standardize processes")     
        
    st.image("Standard3.jpg")

    st.caption("Organizing databases and eliminating duplicate processes") #and improve the quality of your information    

        
with col3:        
        
    st.subheader(" 3. Deliver the information")  
    
    st.image("Send.jpg")

    st.caption("Deliver the information to the stakeholders ")
    
st.header("Data Visualization")    

col4, col5, col6 = st.columns(3)

with col4:

    st.subheader(" 1. Identify the type of report")

    st.image("type.jpg")

    st.caption("Knowing your report needs")
    #st.caption("      Reviewing the process")       
    
    
with col5:

    st.subheader(" 2. Choose the best visual tool")

    st.image("tool.jpg")

    st.caption("With our knowledge we can identify the best tool for our customers")
    #st.caption("      Reviewing the process")
    
    
with col6:

    st.subheader(" 3. Create the report")

    st.image("dashboard.jpg")

    st.caption("Showing you the relevant information to take the best decisions")
    #st.caption("      Reviewing the process")    
    

st.header("Corporate Finance")

col7, col8, col9 = st.columns(3)

with col7:

    st.subheader(" 1. Company Valuation")

    st.image("valuation.jpg")

    st.caption("Fundamental value of your company")
    #st.caption("      Reviewing the process") 
    
    
with col8:

    st.subheader(" 1. Investment Opportunities")

    st.image("invest.jpg")

    st.caption("Invest and diversify part of your profit")
    #st.caption("      Reviewing the process")   
    
    
with col9:

    st.subheader(" 1. Investment Dashboard")

    st.image("dash.jpg")

    st.caption("We will provide you a dashboard to control your investments")
    #st.caption("      Reviewing the process")
