"""
Day Trip Agent - Part 1: Your First Agent

This script demonstrates how to create a simple but powerful AI agent using the
Google Agent Development Kit (ADK). The day_trip_agent generates spontaneous
full-day itineraries based on mood, interests, and budget.
"""

import asyncio
import os
from pathlib import Path
from dotenv import load_dotenv
from google.adk.agents import Agent
from google.adk.tools import google_search
from google.adk.runners import Runner
from google.adk.sessions import InMemorySessionService
from google.genai.types import Content, Part

# Load environment variables from .env file in the same directory as this script
env_path = Path(__file__).parent / '.env'
load_dotenv(dotenv_path=env_path)


def create_day_trip_agent():
    """Create the Spontaneous Day Trip Generator agent."""
    return Agent(
        name="day_trip_agent",
        model="gemini-2.5-flash",
        description="Agent specialized in generating spontaneous full-day itineraries based on mood, interests, and budget.",
        instruction="""
        You are the "Spontaneous Day Trip" Generator 🚗 - a specialized AI assistant that creates engaging full-day itineraries.

        Your Mission:
        Transform a simple mood or interest into a complete day-trip adventure with real-time details, while respecting a budget.

        Guidelines:
        1. **Budget-Aware**: Pay close attention to budget hints like 'cheap', 'affordable', or 'splurge'. Use Google Search to find activities (free museums, parks, paid attractions) that match the user's budget.
        2. **Full-Day Structure**: Create morning, afternoon, and evening activities.
        3. **Real-Time Focus**: Search for current operating hours and special events.
        4. **Mood Matching**: Align suggestions with the requested mood (adventurous, relaxing, artsy, etc.).

        RETURN itinerary in MARKDOWN FORMAT with clear time blocks and specific venue names.
        """,
        tools=[google_search]
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
    """Main function to run the Day Trip Agent demo."""
    
    # Initialize the session service and user ID
    session_service = InMemorySessionService()
    user_id = "adk_adventurer_001"
    
    # Create the agent
    print("🧞 Creating Day Trip Agent...")
    agent = create_day_trip_agent()
    print(f"✅ Agent '{agent.name}' is created and ready for adventure!\n")
    
    # Create a new session for this conversation
    session = await session_service.create_session(
        app_name=agent.name,
        user_id=user_id
    )
    print(f"📦 Created session: {session.id}\n")
    
    # Example query with budget constraint
    query = "Plan a relaxing and artsy day trip near Sunnyvale, CA. Keep it affordable!"
    
    # Run the query
    await run_agent_query(agent, session_service, session, user_id, query)


if __name__ == "__main__":
    # Run the async main function
    asyncio.run(main())