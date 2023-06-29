import os
from apikey import apikey

import streamlit as st
from langchain.llms import openai
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain, SequentialChain
from langchain.memory import ConversationBufferMemory
from langchain.utilities import WikipediaAPIWrapper

os.environ["OPENAI_API_KEY"] = "YOUR_API KEY"
st.title("GPT CREATOR")
prompt = st.text_input("Plug in your prompt")

# Prompt templates
title_template = PromptTemplate(
    input_variables=['topic'],
    template='write me a youtube video title about {topic}'
)
script_template = PromptTemplate(
    input_variables=['title' , 'wikipedia_research'],  # Updated parameter name to lowercase 'title'
    template='write me a youtube video script based on this title TITLE  {title} but also while leveraging this wikipedia research: {wikipedia_research}'  # Updated reference to 'title'
)

#memory
title_memory= ConversationBufferMemory(input_key= 'topic', memory_key= 'chat_history')
script_memory= ConversationBufferMemory(input_key= 'title', memory_key= 'chat_history')



# LLM and chains
llm = openai.OpenAI(temperature=0.9)
title_chain = LLMChain(llm=llm, prompt=title_template, verbose=True, output_key='title', memory=title_memory)
script_chain = LLMChain(llm=llm, prompt=script_template, verbose=True, output_key='script', memory=script_memory)

wiki =WikipediaAPIWrapper()


if prompt:
    title = title_chain.run(prompt)
    wiki_research = wiki.run(prompt)
    script = script_chain.run(title= title, wikipedia_research = wiki_research )
   
    st.write(title)
    st.write(script)


    with st.expander('Title History'):
        st.info(title_memory.buffer)

    with st.expander('Script History'):
        st.info(script_memory.buffer)

    with st.expander('wikipedia Research History'):
        st.info(wiki_research)
