"""
Create SEO content for any webpage using the website-seo-analyzer RapidAPI tool.

This module provides functionality to analyze SEO metrics for a given webpage URL
using the Website SEO Analyzer API from RapidAPI.
"""

from SimplerLLM.tools.rapid_api import RapidAPIClient
from dotenv import load_dotenv
import os
from typing import Any
load_dotenv()


def get_seo_page_report(url: str) -> Any:
    """
    Get SEO analysis report for a webpage.

    Args:
        url (str): The URL of the webpage to analyze

    Returns:
        dict: The SEO analysis report containing various metrics
    """
    rapid_api_client = RapidAPIClient(api_key=os.getenv("RAPID_API_KEY"))

    api_params = {
        "url": url,
    }

    response = rapid_api_client.call_api(
        api_url="https://website-seo-analyzer.p.rapidapi.com/seo/seo-audit-basic",
        method="GET",
        params=api_params,
    )

    return response


if __name__ == "__main__":
    print(get_seo_page_report("https://github.com/mukeshramancha"))














