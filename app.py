import streamlit as st
from langchain.prompts import PromptTemplate
from langchain_community.llms import CTransformers

def GetLamaResponse(input,no_Words,Style):
    llm=CTransformers(model= "Replace this by model path" ,model_type="llama", #Model Link Available In Readme File
                      config={"max_new_tokens":256,
                              "temperature":0.01})
    template="""
    write a blog for {Style} job profile for a topic {input}
    within {no_Words} words.
    """
    prompt=PromptTemplate(input_variables=["Style","input","no_Words"],
                          template=template)
    response=llm(prompt.format(Style=Style,input=input,no_Words=no_Words))
    return response
#StreamLit
st.set_page_config(page_title="Lama_2 Project",
                   page_icon="🤖",
                   layout="centered",
                   initial_sidebar_state="collapsed")

st.title("Generate Blog 🤖")

input_text=st.text_input("Enter the Topic")

cols1,cols2=st.columns([5,5])

with cols1:
    no_words=st.text_input("No of words")
with cols2:
    blog_style=st.selectbox("Writing Bog For",
                            ("Researcher","Data Scientists","Government","Common Pepole"),index=0)
    
submit=st.button("Generate")

if submit:
    st.write(GetLamaResponse(input_text,cols1,cols2))
