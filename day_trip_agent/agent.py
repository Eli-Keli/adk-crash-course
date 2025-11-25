"""
Day Trip Agent - Part 2: Custom Tools

This script demonstrates how to create an AI agent with custom tools using the
Google Agent Development Kit (ADK). The weather_aware_planner checks real-time
weather before making trip recommendations.
"""

import asyncio
import os
from pathlib import Path
import requests
from dotenv import load_dotenv
from google.adk.agents import Agent
from google.adk.runners import Runner
from google.adk.sessions import InMemorySessionService
from google.genai.types import Content, Part

# Load environment variables from .env file in the same directory as this script
env_path = Path(__file__).parent / '.env'
load_dotenv(dotenv_path=env_path)

# --- Tool Definition: A function that calls a live public API ---

# A simple lookup to avoid needing a separate geocoding API for this example
LOCATION_COORDINATES = {
    "sunnyvale": "37.3688,-122.0363",
    "san francisco": "37.7749,-122.4194",
    "lake tahoe": "39.0968,-120.0324"
}

def get_live_weather_forecast(location: str) -> dict:
    """Gets the current, real-time weather forecast for a specified location in the US.

    Args:
        location: The city name, e.g., "San Francisco".

    Returns:
        A dictionary containing the temperature and a detailed forecast.
    """
    print(f"🛠️ TOOL CALLED: get_live_weather_forecast(location='{location}')")

    # Find coordinates for the location
    normalized_location = location.lower()
    coords_str = None
    for key, val in LOCATION_COORDINATES.items():
        if key in normalized_location:
            coords_str = val
            break
    if not coords_str:
        return {"status": "error", "message": f"I don't have coordinates for {location}."}

    try:
        # NWS API requires 2 steps: 1. Get the forecast URL from the coordinates.
        points_url = f"https://api.weather.gov/points/{coords_str}"
        headers = {"User-Agent": "ADK Example Notebook"}
        points_response = requests.get(points_url, headers=headers)
        points_response.raise_for_status()  # Raise an exception for bad status codes
        forecast_url = points_response.json()['properties']['forecast']

        # 2. Get the actual forecast from the URL.
        forecast_response = requests.get(forecast_url, headers=headers)
        forecast_response.raise_for_status()

        # Extract the relevant forecast details
        current_period = forecast_response.json()['properties']['periods'][0]
        return {
            "status": "success",
            "temperature": f"{current_period['temperature']}°{current_period['temperatureUnit']}",
            "forecast": current_period['detailedForecast']
        }
    except requests.exceptions.RequestException as e:
        return {"status": "error", "message": f"API request failed: {e}"}


def create_weather_aware_planner():
    """Create the Weather-Aware Trip Planner agent."""
    return Agent(
        name="weather_aware_planner",
        model="gemini-2.5-flash",
        description="A trip planner that checks the real-time weather before making suggestions.",
        instruction="You are a cautious trip planner. Before suggesting any outdoor activities, you MUST use the `get_live_weather_forecast` tool to check conditions. Incorporate the live weather details into your recommendation.",
        tools=[get_live_weather_forecast]
    )


async def run_agent_query(agent, session_service, session, user_id, query):
    """
    Execute a query for the given agent and session.
    
    Args:
        agent: The Agent instance to run
        session_service: The session service managing sessions
        session: The session object for this conversation
        user_id: The user ID
        query: The user's query string
    
    Returns:
        The final response text from the agent
    """
    print(f"\n🚀 Running query for agent: '{agent.name}'")
    print(f"📝 Query: '{query}'")
    print("-" * 70)
    
    runner = Runner(
        agent=agent,
        session_service=session_service,
        app_name=agent.name
    )

    final_response = ""
    
    try:
        async for event in runner.run_async(
            user_id=user_id,
            session_id=session.id,
            new_message=Content(parts=[Part(text=query)], role="user")
        ):
            # Print events to see what the agent is thinking
            print(f"📡 EVENT: {event}")
            
            if event.is_final_response():
                final_response = event.content.parts[0].text
    except Exception as e:
        final_response = f"❌ An error occurred: {e}"
        print(final_response)
        return final_response

    print("\n" + "=" * 70)
    print("✅ FINAL RESPONSE:")
    print("=" * 70)
    print(final_response)
    print("=" * 70 + "\n")

    return final_response


async def main():
    """Main function to run the Weather-Aware Planner demo."""
    
    # Initialize the session service and user ID
    session_service = InMemorySessionService()
    user_id = "adk_adventurer_001"
    
    # Create the agent
    print("🌦️ Creating Weather-Aware Planner Agent...")
    weather_agent = create_weather_aware_planner()
    print(f"✅ Agent '{weather_agent.name}' is created and can now call a live weather API!\n")
    
    # Create a new session for this conversation
    session = await session_service.create_session(
        app_name=weather_agent.name,
        user_id=user_id
    )
    print(f"📦 Created session: {session.id}\n")
    
    # Example query that will trigger the weather tool
    query = "I want to go hiking near Lake Tahoe, what's the weather like?"
    print(f"🗣️ User Query: '{query}'\n")
    
    # Run the query
    await run_agent_query(weather_agent, session_service, session, user_id, query)


if __name__ == "__main__":
    # Run the async main function
    asyncio.run(main())