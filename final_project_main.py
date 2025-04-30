from SimplerLLM.language.llm import LLM, LLMProvider
from SimplerLLM.tools.json_helpers import extract_json_from_text
from dotenv import load_dotenv
import os

from final_project_prompt import react_system_prompt
from final_project_action import get_seo_page_report


def analyze_webpage(prompt: str) -> str:
    """
    Analyzes a webpage using an LLM-powered SEO auditor agent
    
    Args:
        prompt (str): Question about a webpage to analyze
        
    Returns:
        str: LLM response about the webpage analysis
    """
    available_actions = {
        "get_seo_page_report": get_seo_page_report,
    }

    llm_instance = LLM.create(
        provider=LLMProvider.OPENAI,
        model_name="gpt-3.5-turbo", 
        api_key=os.getenv("OPENAI_API_KEY"),
    )

    messages = [
        {"role": "system", "content": react_system_prompt},
        {"role": "user", "content": prompt},
    ]

    response = llm_instance.generate_response(messages=messages)

    json_response = extract_json_from_text(response)

    if json_response is None:
        print(response)
        raise Exception("No JSON response found, please ask a webpage related question")

    if json_response[0]["function_name"] in available_actions.keys():
        action_response = available_actions[json_response[0]["function_name"]](
            **json_response[0]["function_params"]
        )
    else:
        raise Exception("No available action found")

    messages.append(
        {
            "role": "user",
            "content": f"Action Response: the full SEO report is {action_response}"
        }
    )

    response = llm_instance.generate_response(messages=messages)
    return response


if __name__ == "__main__":
    # SEO Auditor agent
    # we can ask anything about any webpage and it'll answer based on that webpage
    prompt = (
        "tell me about: https://github.com/mukeshramancha"
    )
    print(prompt)
    response = analyze_webpage(prompt)
    print(response)
