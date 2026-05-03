import os
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
MODEL_NAME = "gpt-5.4-mini"

client = OpenAI(api_key=OPENAI_API_KEY)

def generate_raw_response(user_message: str) -> str:
    completion = client.chat.completions.create(
        model=MODEL_NAME, 
        messages=[
            {
                "role": "system", 
                "content": "Answer the user message in a concise and comprehensive way. Only provide information based on the context of the question.",
            },
             {
                "role": "user", 
                "content": user_message,
            },
        ],
    )

    result = completion.choices[0].message.content

    return result 

def summarize(user_message: str) -> str:
    completion = client.chat.completions.create(
        model=MODEL_NAME, 
        messages=[
            {
                "role": "system", 
                "content": "Summarize the user message in a concise and comprehensive way. Only provide information based on the context of the question.",
            },
             {
                "role": "user", 
                "content": user_message,
            },
        ],
    )

    result = completion.choices[0].message.content

    return result

def generate_structured_response(user_message: str, structured_response: dict) -> str:
    completion = client.chat.completions.parse(
        model=MODEL_NAME, 
        messages=[
            {
                "role": "system", 
                "content": "Answer the user message in a concise and comprehensive way. Only provide information based on the context of the question. Format the response according to the provided structured response format.",
            },
             {
                "role": "user", 
                "content": user_message,
            },
        ],
        response_format=structured_response
    )

    result = completion.choices[0].message.parsed

    return result 