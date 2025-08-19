import os
import sys
import random
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.prompts import PromptTemplate
from langchain_core.runnables import RunnablePassthrough
from langchain_core.output_parsers import StrOutputParser
api_key = ""
prompts = [
    "Write a short haiku about a rainy day.",
    "Explain why the sky is blue.",
    "Tell me a fun fact about space.",
    "Give me an idea for a simple Python project.",
    "What is the capital of Japan?",
    "Write a short, uplifting quote."
]
if len(sys.argv) < 2:
    topic_to_generate = random.choice(prompts)
    print("No topic provided. Choosing a random topic from the list.")
else:
    topic_to_generate = sys.argv[1]
llm = ChatGoogleGenerativeAI(model="gemini-1.5-flash-latest", google_api_key=api_key)
template = """
You are a friendly and helpful assistant.
{topic}
"""
prompt = PromptTemplate(input_variables=["topic"], template=template)
chain = (
    {"topic": RunnablePassthrough()}
    | prompt
    | llm
    | StrOutputParser()
)
print(f"Running the chain with the topic: '{topic_to_generate}'")
response = chain.invoke(topic_to_generate)
print("\n--------------------")
print("Response from LangChain:")
print("--------------------")
print(response)

# You can still provide a specific topic like this:
# python Gemini.py "the benefits of meditation"


