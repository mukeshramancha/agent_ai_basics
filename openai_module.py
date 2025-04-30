from openai import OpenAI
from dotenv import load_dotenv
import os

print("hello")

# load the environment variables
load_dotenv()

# initialize the OpenAI client
openai = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

# define the function to generate text
def generate_text_basic(prompt: str, model: str = "gpt-3.5-turbo"):
    response = openai.chat.completions.create(
        model=model,
        messages=[
            {"role": "user", "content": prompt}
        ]
    )
    return response.choices[0].message.content

# define the function to generate text with a system prompt
"""
The system prompt (system_prompt) is used to:
Define the AI's role or personality (e.g., "You are a helpful assistant")
Set specific guidelines or constraints (e.g., "Always respond in Spanish")
Provide context or background information
Establish response format or style
"""
def generate_text_with_system_prompt(prompt: str, system_prompt: str, model: str = "gpt-3.5-turbo"):
    response = openai.chat.completions.create(
        model=model,
        messages=[
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": prompt}
        ]
    )
    return response.choices[0].message.content


# generate text with messages
def generate_text_with_messages(messages: list, model: str = "gpt-3.5-turbo"):
    response = openai.chat.completions.create(
        model=model,
        messages=messages
    )
    return response.choices[0].message.content

