import streamlit as st
#from pandas.compat import StringIO
import re

uploaded_file = st.file_uploader("Choose a file")
if uploaded_file is not None:
    if not uploaded_file.name.endswith(".pdf"):
        st.error("Please Upload a pdf")
    else:
        st.success("File Uploaded")












st.header("Take Survey Here")
num1 = st.radio("1. Have you mapped your family's health history back one or two generations?",
                 ("Yes, I've researched my family's health and have the information available.",
                  "I'm not sure how accurate my family's health information is but I'll do the best I can.",
                  "No, I haven't been able to do the research, so I'll be using my best recollections",
                  "Other"))
if num1 == "Other":
    num1Extra = st.text_input("Please Specify")

num2 = st.radio("2. Are you located in the United States?",
                 ("Yes",
                  "No",
                  "Other"))
if num2 == "Other":
    num2Extra = st.text_input("Please Specify")

num3 = st.radio("3. Are you of Ashkenazi Jewish descent?",
                 ("Yes",
                  "No",
                  "I don't know"))
num4 = st.radio("4. Have you been tested for gene changes?",
                 ("Yes, I have been. I'll list the gene changes identified below.",
                  "No, I've never had genetic tests before.",
                  "Other"))
if num4 == "Other":
    num4Extra = st.text_input("Please Specify")

num5 = st.text_input("5. What is the email address you would like to for the survey results be sent to?")

if not re.match(r"[^@]+@[^@]+\.[^@]+", num5) and not num5 == "":
    st.error("Please put proper formatted email address")


num6 = st.multiselect("6. Has your mother or father been diagnosed with cancer? Only 'blood' relatives need to be considered for the survey.",
                 ["Yes, my mother was diagnosed with cancer. I'll enter her age at diagnosis and type of cancer below.",
                  "Yes, my father was diagnosed with cancer. I'll enter his age at diagnosis and type of cancer below.",
                  "I don't know or remember.",
                  "My mother and father have never been diagnosed with cancer.",
                  "Age at diagnosis & type of cancer:"])
if (num6 == "Yes, my mother was diagnosed with cancer. I'll enter her age at diagnosis and type of cancer below." or
    num6 == "Yes, my father was diagnosed with cancer. I'll enter his age at diagnosis and type of cancer below." or
    num6 == "Age at diagnosis & type of cancer:"):
    num6Extra = st.text_input("Please Specify")


num7 = st.multiselect("7. Were your mother's parents ever diagnosed with cancer? Only 'blood' relatives need to be considered for the survey.",
                 ["Yes, my grandmother was diagnosed with cancer. I'll enter her age at diagnosis and type of cancer below.",
                  "Yes, my grandfather was diagnosed with cancer. I'll enter his age at diagnosis and type of cancer below.",
                  "I don't know or remember.",
                  "My grandmother and grandfather have never been diagnosed with cancer.",
                  "Age at diagnosis & type of cancer:"])
if ( "Yes, my grandmother was diagnosed with cancer. I'll enter her age at diagnosis and type of cancer below."  in num7 or
    "Yes, my grandfather was diagnosed with cancer. I'll enter his age at diagnosis and type of cancer below."  in num7 or
    "Age at diagnosis & type of cancer:" in num7):
    num7Extra = st.text_input("Please Elaborate")
    st.write("")

num8 = st.multiselect("8. Were your father's parents ever diagnosed with cancer? Only 'blood' relatives need to be considered for the survey.",
                 ["Yes, my grandmother was diagnosed with cancer. I'll enter her age at diagnosis and type of cancer below.",
                  "Yes, my grandfather was diagnosed with cancer. I'll enter his age at diagnosis and type of cancer below.",
                  "I don't know or remember.",
                  "My grandmother and grandfather have never been diagnosed with cancer.",
                  "Age at diagnosis & type of cancer:"])
if ("Yes, my grandmother was diagnosed with cancer. I'll enter her age at diagnosis and type of cancer below." in num8 or
    "Yes, my grandfather was diagnosed with cancer. I'll enter his age at diagnosis and type of cancer below." in num8 or
    "Age at diagnosis & type of cancer:" in num8):
    num8Extra = st.text_input("Please Specify")


num9 = st.text_input("9. For some of our recommendations, we'll need to know where in the world you are. So, please share your zipcode.")
if not re.match(r"\d{5}(-\d{4})?$", num9) and not num9 == "":
    st.error("Please put proper formatted zip code")

num10 = st.multiselect("10. Were your parents' brothers and sisters ever diagnosed with cancer? Only 'blood' relatives need to be considered for the survey.",
                 ["Yes, my aunt(s) was diagnosed with cancer. I'll enter her age at diagnosis and type of cancer below.",
                  "Yes, my uncle(s) was diagnosed with cancer. I'll enter his age at diagnosis and type of cancer below.",
                  "I don't know or remember.",
                  "My aunt(s) and uncle(s) have never been diagnosed with cancer.",
                  "Age at diagnosis & type of cancer:"])
if ("Yes, my aunt(s) was diagnosed with cancer. I'll enter her age at diagnosis and type of cancer below." in num8 or
    "Yes, my uncle(s) was diagnosed with cancer. I'll enter his age at diagnosis and type of cancer below." in num8 or
    "Age at diagnosis & type of cancer:" in num8):
    num10Extra = st.text_input("Please Specify")
if (num1 == "Yes, I've researched my family's health and have the information available." and num2 == "Yes" and num3 == "Yes" and
    num4 == "Yes, I have been. I'll list the gene changes identified below." and num5 == "" and
    num6 == [] and  num7 == [] and num8 == []):
    st.warning("You haven't changed any of the question choices, please double check the survey.")

num11_Other = st.text_input("11. We respect your privacy and never share your information. That's a promise! We like to know who we are working with so please enter your name.")

num12_Other = st.text_input("12. Additional comments?")

