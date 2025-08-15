# First, you need to install the necessary libraries.
# Run the following commands in your terminal:
# pip install langchain-google-genai
# pip install langchain

import os
import sys
# We will import the 'random' module to pick a prompt.
import random
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.prompts import PromptTemplate
from langchain_core.runnables import RunnablePassthrough
from langchain_core.output_parsers import StrOutputParser

# IMPORTANT: Your API key goes here.
# Be careful not to share this file if it contains your key!
api_key = "AIzaSyAgM8_VypnflbCnogw1MO0bDjf7Bc3mySk"

# Create a list of prompts to choose from.
# Feel free to add or change these prompts to whatever you like!
prompts = [
    "Write a short haiku about a rainy day.",
    "Explain why the sky is blue.",
    "Tell me a fun fact about space.",
    "Give me an idea for a simple Python project.",
    "What is the capital of Japan?",
    "Write a short, uplifting quote."
]

# Check if a command-line argument was provided.
# If no argument is given, we will pick a random prompt from our list.
if len(sys.argv) < 2:
    topic_to_generate = random.choice(prompts)
    print("No topic provided. Choosing a random topic from the list.")
    
# If an argument is given, we will use that as the topic.
else:
    topic_to_generate = sys.argv[1]

# 1. Initialize the LLM (Language Model)
# We will use the 'gemini-1.5-flash-latest' model.
llm = ChatGoogleGenerativeAI(model="gemini-1.5-flash-latest", google_api_key=api_key)

# 2. Define a Prompt Template
# The template is now more general to handle all the different prompts.
template = """
You are a friendly and helpful assistant.
{topic}
"""
prompt = PromptTemplate(input_variables=["topic"], template=template)

# 3. Create a RunnableSequence
chain = (
    {"topic": RunnablePassthrough()}
    | prompt
    | llm
    | StrOutputParser()
)

# 4. Run the Chain
print(f"Running the chain with the topic: '{topic_to_generate}'")
response = chain.invoke(topic_to_generate)

# 5. Print the response
print("\n--------------------")
print("Response from LangChain:")
print("--------------------")
print(response)

# To get a different response each time, just run the script:
# python Gemini.py
# You can still provide a specific topic like this:
# python Gemini.py "the benefits of meditation"
