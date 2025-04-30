
from openai_module import generate_text_with_system_prompt
from sample_functions import get_weather
from prompts import react_system_prompt
import json


prompt = "Should I take an umbrella with me in London today?"
#prompt = "Should I drive car in Arizona today?"

response = generate_text_with_system_prompt(prompt, system_prompt = react_system_prompt)
print(response)

"""
Thought: I should check the weather in California first.
Action:

{
  "function_name": "get_weather",
  "function_parms": {
    "city": "California"
  }
}

PAUSE
"""
# the AI agent thinks aboue the question and know the correect action to take

# list of all available actions
available_actions = {
    "get_weather": get_weather
}

# extract action from the response

extract_json_action = response.split("Action:")[1].split("PAUSE")[0].strip()
print(extract_json_action)

# parse the json action
action_name = json.loads(extract_json_action)["function_name"]
action_parms = json.loads(extract_json_action)["function_parms"]

# call the action

if action_name in available_actions:
    action_response = available_actions[action_name](**action_parms)
    print(action_response)
else:
    print(f"Action {action_name} not found")

# pass the action response back to the AI agent
prompt_v2 = f"Action_Response: weather in {action_parms['city']} is {action_response}"

response_v2 = generate_text_with_system_prompt(prompt_v2, system_prompt = react_system_prompt)
print(response_v2)

"""
Answer: Yes, you should take an umbrella with you today because the weather in London is rainy.
"""

