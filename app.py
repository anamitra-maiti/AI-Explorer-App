from langchain.llms import OpenAI
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain, SequentialChain
from dotenv import load_dotenv
import streamlit as st
import os

load_dotenv()

st.set_page_config(page_title="🌍 AI World Explorer")
st.title("✈️ Welcome to AI World Explorer")
st.markdown("Get travel tips, places to visit, and more—powered by AI!")

country_input = st.text_input("Enter a country to explore:", key="input")
submit = st.button("Plan My Trip")

if submit and country_input:

    llm = OpenAI(model_name="gpt-3.5-turbo-instruct", temperature=0.7, openai_api_key=os.getenv("OPEN_API_KEY"))

    capital_prompt = PromptTemplate(
        input_variables=["country"],
        template="What is the capital of {country}?"
    )
    capital_chain = LLMChain(llm=llm,prompt=capital_prompt,output_key="capital")

    places_prompt =PromptTemplate(
        input_variables=["capital"],
        template="List 3 must-visit places in {capital}, with short description."
        )
    places_chain = LLMChain(llm=llm, prompt=places_prompt,output_key="places")

    fun_fact_prompt = PromptTemplate(
        input_variables=["country"],
        template="Tell me an interesting and unusual fact about {country}."
    )
    fun_fact_chain = LLMChain(llm=llm, prompt=fun_fact_prompt, output_key="fun_fact")

    food_prompt = PromptTemplate(
        input_variables=["country"],
        template="What is a must-try traditional dish in {country} and why is it special?"
    )
    food_chain = LLMChain(llm=llm, prompt=food_prompt, output_key="food")

    teaser_prompt = PromptTemplate(
        input_variables=["country"],
        template="Write a short 3-line poetic travel teaser about visiting {country}."
    )
    teaser_chain = LLMChain(llm=llm, prompt=teaser_prompt, output_key="teaser")

    chain = SequentialChain(
            chains=[capital_chain, places_chain, fun_fact_chain, food_chain, teaser_chain],
            input_variables=["country"],
            output_variables=["capital", "places", "fun_fact", "food", "teaser"],
            verbose=False
        )

    result = chain({"country": country_input})

    st.subheader("📍 Capital City")
    st.write(result["capital"])

    st.subheader("🏞️ Must-Visit Places")
    st.write(result["places"])

    st.subheader("🤯 Fun Fact")
    st.write(result["fun_fact"])

    st.subheader("🍽️ Local Cuisine")
    st.write(result["food"])

    st.subheader("🎭 Travel Teaser")
    st.markdown(f"📝 *{result['teaser']}*")