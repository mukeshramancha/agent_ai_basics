# we'll hard code agent, call weather function, then inject the response back into the prompt

from openai_module import generate_text_basic
from sample_functions import get_weather

current_weather = get_weather("California")

prompt = "Should I take an umbrella with me today?"

prompt_injected = f"""{prompt}

Here is the weather forecast:
{current_weather}
"""

response = generate_text_basic(prompt_injected)
print(response)

"""
There is no need to bring an umbrella with you today. Enjoy the sunny weather!
"""

# agent AI: automatically selects which API/function to call based on the prompt
