from openai_module import generate_text_with_messages
from sample_functions import get_weather
from prompts import react_system_prompt
import json

#prompt = "Should I take an umbrella with me in London today?"
#prompt = "Is it a good day to go to the beach in California?"
#prompt = "what is digital marketing?"
prompt = "should I walk or take a car in London today?"

# list of all available actions
available_actions = {
    "get_weather": get_weather
}

messages = [
    {"role": "system", "content": react_system_prompt},
    {"role": "user", "content": prompt}
]

counter = 0
max_iterations = 2

while counter < max_iterations:
    print(f"Iteration {counter}")
    counter += 1

    # generate the response
    response = generate_text_with_messages(messages)
    print(response)

    # extract & run action
    try:
        extract_json_action = response.split("Action:")[1].split("PAUSE")[0].strip()
    except:
        print("No action found")
        break

    # parse the json action
    action_name = json.loads(extract_json_action)["function_name"]
    action_parms = json.loads(extract_json_action)["function_parms"]
    
    # call the action
    if action_name in available_actions:
        action_response = available_actions[action_name](**action_parms)
    else:
        print(f"Action {action_name} not found")
        break

    # pass the action response back to the AI agent
    action_result = f"Action_Response: weather in {action_parms['city']} is {action_response}"

    # add the action result to the messages
    messages.append({"role": "user", "content": action_result})

print("bye")