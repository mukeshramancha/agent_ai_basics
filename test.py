from openai_module import generate_text_basic

prompt = "Should I take an umbrella with me in California today?"

response = generate_text_basic(prompt)

print(prompt)
print(response)

"""
Should I take an umbrella with me today?
I don't have real-time weather updates. To know if you need an umbrella today, 
I recommend checking a local weather website, using a weather app, or viewing a weather channel for the most 
current forecast in your area.
"""
# does not have access to real-time weather updates
