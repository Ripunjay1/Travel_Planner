import streamlit as st
import google.generativeai as genai

st.set_page_config(page_title= "Travel Planner")
st.title("I am your Travel Planner")

genai.configure(api_key = API_Key)

sys_prompt=("""You are Travel planner who will ask for three inputs which is Location , Days for how many 
traveller wants to travel and date. Location and days would the mandotary inputs. After getting response you 
will look out the information you have and give 3 different responses which would be travel plans. If anyone
asks a query which is not related to travel planning ask them gentely to ask related question""")

model = genai.GenerativeModel('models/gemini-2.0-pro-exp')

user_prompt = st.text_input("Enter your Details")
btn_click = st.button("Generate response")

if btn_click ==True:
    response = model.generate_content(user_prompt)
    st.write(response.text)
