# Part 2: Custom Tools - Weather-Aware Planner 🌦️

Welcome to Part 2 of the ADK Crash Course! In this section, you'll learn how to create custom tools that extend your agent's capabilities.

## 🎯 What You'll Learn

- How to create custom function tools
- How to call external APIs (U.S. National Weather Service)
- How to integrate custom tools with built-in tools
- Best practices for tool docstrings and descriptions

## 📚 Learning Resources

- **Codelab**: https://codelabs.developers.google.com/onramp/instructions
- **ADK Documentation**: https://google.github.io/adk-docs/get-started/python/
- **Notebook Reference**: Section 2.1 from `ADK_Learning_tools.ipynb`
- **Weather API**: U.S. National Weather Service API (public, no key required)

---

## 🚀 Quick Start

### Prerequisites

1. **Python 3.10+** installed
2. **Google API Key** - Get yours here: https://aistudio.google.com/apikey

### Setup

1. **Create and activate virtual environment**:
   ```bash
   python3 -m venv .venv
   source .venv/bin/activate  # On Windows: .venv\Scripts\activate
   ```

2. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   # Or manually:
   # pip install google-adk python-dotenv requests
   ```

3. **Set up your API key**:
   
   The agent was created with `adk create` command which already configured your `.env` file with the API key. Make sure the `.env` file exists in the `day_trip_agent/` directory:
   
   ```bash
   # .env file should contain:
   GOOGLE_API_KEY=your_api_key_here
   ```

---

## 🏃 Running the Agent

From the `adk-crash-course/` directory:

```bash
# Make sure your virtual environment is activated
source .venv/bin/activate

# Run the agent
python day_trip_agent/agent.py
```

### Expected Output

You should see:
1. 🌦️ Agent creation message
2. 📦 Session creation
3. 🛠️ Weather tool being called with location
4. 📡 Events as the agent processes your query
5. ✅ Final response with weather details and hiking recommendations

---

## 🔍 What's Happening?

### The Agent Architecture

```
┌───────────────────────────────────────────────────┐
│       Weather-Aware Planner 🤖                    │
├───────────────────────────────────────────────────┤
│  Model: gemini-2.5-flash                          │
│  Tools: get_live_weather_forecast, Google Search  │
│  Instruction: Check weather before outdoor plans  │
└───────────────────────────────────────────────────┘
                    ↓
          ┌─────────────────┐
          │     Runner      │  ← Executes the agent
          └─────────────────┘
                    ↓
          ┌─────────────────┐
          │     Session     │  ← Stores conversation
          └─────────────────┘
```

### Key Components

1. **Agent** (`create_weather_aware_planner()`):
   - Defines the agent's personality and capabilities
   - Specifies the model to use (gemini-2.5-flash)
   - Adds custom tool (get_live_weather_forecast) and built-in tool (google_search)
   - Provides instruction to check weather before suggesting activities

2. **Custom Tool** (`get_live_weather_forecast()`):
   - Python function that calls U.S. National Weather Service API
   - Docstring serves as the tool's description for the LLM
   - Returns structured data (temperature and forecast)
   - Located in `tools/weather.py`

3. **Session** (`InMemorySessionService`):
   - Manages conversation history
   - In this example, we create a new session for each run
   - Later, you'll learn about persistent sessions

3. **Runner** (`Runner`):
   - Connects the agent to the session
   - Processes user queries
   - Streams events back to you

---

## 🎨 Customization Ideas

Try modifying the query in `agent.py` to test different scenarios:

```python
# Budget-conscious trip
query = "Plan a cheap day trip in San Francisco for students"

# Adventure seeker
query = "Plan an adventurous outdoor day trip near Lake Tahoe"

# Foodie experience
query = "Plan a food-focused day trip in Oakland, CA with the best local restaurants"

# Family-friendly
query = "Plan a family-friendly day trip with kids near San Jose, CA. Keep it affordable!"
```

---

## 🐛 Troubleshooting

### Issue: Import errors
```
Import "google.adk.agents" could not be resolved
```
**Solution**: Make sure you've installed the package:
```bash
pip install google-adk
```

### Issue: API Key not found
```
Error: GOOGLE_API_KEY not set
```
**Solution**: Check that your `.env` file exists in the `day_trip_agent/` directory with your API key.

### Issue: Virtual environment not activated
**Solution**: 
```bash
source .venv/bin/activate  # or .venv\Scripts\activate on Windows
```

---

## 📖 Code Walkthrough

### 1. Agent Creation
```python
def create_day_trip_agent():
    return Agent(
        name="day_trip_agent",
        model="gemini-2.5-flash",
        description="...",
        instruction="...",
        tools=[google_search]  # Built-in Google Search tool
    )
```

### 2. Running a Query
```python
async def run_agent_query(agent, session_service, session, user_id, query):
    runner = Runner(agent=agent, session_service=session_service, ...)
    
    async for event in runner.run_async(...):
        # Process events
        if event.is_final_response():
            final_response = event.content.parts[0].text
```

### 3. Main Execution
```python
async def main():
    session_service = InMemorySessionService()
    agent = create_day_trip_agent()
    session = await session_service.create_session(...)
    await run_agent_query(agent, session_service, session, user_id, query)

asyncio.run(main())
```

---

## ✅ What's Next?

Once you've successfully run this agent, you're ready for:

**Part 2: Custom Tools** - Learn how to add custom functions and create agent teams

---

## 💡 Key Takeaways

✅ **Agents** are defined by their model, instruction, and tools  
✅ **Sessions** manage conversation state  
✅ **Runners** execute the agent logic  
✅ **Built-in tools** like Google Search are easy to add  
✅ **Async/await** is used for non-blocking execution

---

Happy coding! 🚀
