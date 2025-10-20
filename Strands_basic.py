import logging
from strands import Agent
from strands_tools import current_time,http_request,use_aws
from strands.models import BedrockModel



WEATHER_HOTEL_SYSTEM_PROMPT = """
You are a weather assistant with HTTP capabilities. You can:
1. Make HTTP requests to the National Weather Service API
2. Process and display weather forecast data
3. Provide weather information for locations in the United States

When displaying responses:
- Format weather data in a human-readable way
- Highlight important information like temperature, precipitation, and alerts
- Handle errors appropriately
- Convert technical terms to user-friendly language

Always explain the weather conditions clearly and provide context for the forecast.

"""

subject_expert = Agent(
    system_prompt = WEATHER_HOTEL_SYSTEM_PROMPT,
    tools = [current_time, http_request, use_aws],
    model=BedrockModel(model_id="amazon.nova-pro-v1:0",temperature=0.1)
)


query = """
Answer the following questions:
1. What is the current time in New York City?
2. What is the weather forecast for New York City for the next 3 days?
3. Are there any weather alerts for New York City?
"""

respone = subject_expert(query)