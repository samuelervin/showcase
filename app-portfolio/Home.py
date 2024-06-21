import streamlit as st
import pandas as pd
st.set_page_config(page_title="Sam Ervin", page_icon=":smiley:", layout="wide")
col1, col2 = st.columns(2)

with col1:
    st.image("app-portfolio/images/photo.jpg", width=300, caption="Sam Ervin")

with col2:  
    st.title("Samuel(Sam) Ervin")
    content =""" Experienced Sr. SWR Mgr, Staff SWE and Project Manager with multiple years of experience. I graduated from Capella University with my Masters of Science in Project Management 
    Organizational Leadership. I have worked for the worlds largest retailer where I held several roles. I have also held roles at other companies and a non-profit 
    organization as a programmer and project manager.  Outside of work I enjoy video games, fishing, baseball, softball, sailing, and boating. """
    st.info(content)    
    
content2 = """Below are some of the python projects I have worked on as examples. 
Please click on the links to view the projects and the code."""

st.write(content2)

#use pandsa to read the csv file
df = pd.read_csv("app-portfolio/data/data.csv", sep=";")

#create new columns for the lists with ratio dimensions not just number of columns
col3,empty_col, col4 = st.columns([1.5,0.5,1.5])

with col3:
    for index, row in df[:10].iterrows():
        st.header(row["title"])
        st.write(row["description"])
        st.image("app-portfolio/images/" + row["image"], width=300)
        st.write(f"[Source Code]({row['url']})")
        
with col4:
    for index, row in df[10:].iterrows():
        st.header(row["title"])
        st.write(row["description"])
        st.image("app-portfolio/images/" + row["image"], width=300)
        st.write(f"[Source Code]({row['url']})")