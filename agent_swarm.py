from langchain.llms import OpenAI
import os

def get_llm():
    return OpenAI(openai_api_key=os.getenv('OPENAI_API_KEY'))
