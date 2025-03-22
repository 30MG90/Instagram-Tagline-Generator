import os

os.environ['GOOGLE_API_KEY']  = "AIzaSyClx1WkdM1kYYGVn1zmieEjcU-nQbc4eCM"
# Using Google Models (Gemini Pro)
from langchain_google_genai import ChatGoogleGenerativeAI

# Initialize Google's Gemini model
gemini_model = ChatGoogleGenerativeAI(model = "gemini-1.5-flash-latest")
from langchain import PromptTemplate

# Create prompt template for generating Instagram text

tweet_template_insta = """Give me {number} post content on {topic} in English under {character} limit.

2. Ensure all content is respectful and appropriate for all audiences.
3. Avoid creating content on offensive, controversial, or sensitive topics.
4. Understand the context and give the content
5. Add the top 3 relevant hashtags
6. Consider the SEO value of the content and write it with keyword value
7. Write it like a story narrative
""" 


tweet_prompt_insta = PromptTemplate(template = tweet_template_insta, input_variables = ['number', 'topic','character'])

from langchain import LLMChain

# Create LLM chain using the prompt template and model
tweet_chain_insta = tweet_prompt_insta | gemini_model

response = tweet_chain_insta.invoke({"number" : 10, "topic" : "India"})
print(response.content)


import streamlit as st
st.header("Instagram Content Generator")
st.subheader("Generate Instagram text for your posts!")

Topic = st.text_input("Please enter the topic of your post")
Number = st.number_input("How Many Suggestions would You Like to Generate", min_value=1, max_value=10, step=1)
Character = st.number_input("How many word characters should I generate"_
if st.button("Generate"):
    tweet = tweet_chain_insta.invoke({"number" : Number, "topic" : Topic, "character" : Character})
    st.write(tweet.content)
