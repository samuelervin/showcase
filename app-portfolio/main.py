import streamlit as st
import pandas as pd
st.set_page_config(page_title="Sam Ervin", page_icon=":smiley:", layout="wide")
col1, col2 = st.columns(2)

with col1:
    st.image("app-portfolio/images/photo.jpg", width=300, caption="Sam Ervin")

with col2:  
    st.title("Samuel(Sam) Ervin")
    content =""" Experienced Senior Software Engineering Manager, Staff Software Engineer and Project Manager
    with multiple years of experience at several companies. I have led and coached several diversely geographically located agile teams 
    to produce enterprise systems and applications that met or exceeded audit, legal and customer satisfaction goals. I have designed and 
    developed global applications and enterprise systems that were/are used by the number one  Retail, Store Layout, Manufacturing 
    and Hospitality industries using several different programming languages and frameworks such as C, C++. C#, VB.Net, Java, Python, 
    GO, NodeJS, and React deployed on both cloud and internal infrastructures. As a software engineer and manager, I have worked on 
    designing strategies, implementing and documenting best practices for my own and enterprise teams for DevOps at Walmart using the
    tooling required to implement these such as ServiceDesk, Jira, Concord Ansible, Looper, Jenkins, ArgoCd, git, and GitHub to ensure CI/CD. """
    st.info(content)    
    
content2 = """Below are some of the python projects I have worked on as examples. 
Please click on the links to view the projects and the code."""

st.write(content2)

#use pandsa to read the csv file
df = pd.read_csv("app-portfolio/data/data.csv", sep=";")

col3, col4 = st.columns(2)

with col3:
    for index, row in df[:10].iterrows():
        st.header(row["title"])

with col4:
    for index, row in df[10:].iterrows():
        st.header(row["title"])