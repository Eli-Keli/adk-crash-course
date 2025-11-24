# 🚀 ADK Crash Course - Agent Development Kit Learning Repository

Welcome to the **Google Agent Development Kit (ADK) Crash Course**! This repository is designed to help you master AI agent development through hands-on examples, structured across multiple branches for easy navigation.

---

## 📚 About This Repository

This crash course follows the official [Google ADK Codelab](https://codelabs.developers.google.com/onramp/instructions) and demonstrates concepts from the companion notebook `ADK_Learning_tools.ipynb`.

**Key Features**:
- ✅ Each branch = One complete lesson
- ✅ Self-contained examples with full setup instructions
- ✅ Production-ready Python code (not just notebook snippets)
- ✅ Real-world patterns for building AI agents

---

## 🎯 Learning Path

Follow these branches in order to progressively build your ADK skills:

### ✅ Part 1: Your First Agent - The Day Trip Genie 🧞
**Branch**: [`part-1-basic-agent`](../../tree/part-1-basic-agent)

**What You'll Learn**:
- Create a basic AI agent with the ADK
- Use built-in tools (Google Search)
- Understand the Agent-Runner-Session architecture
- Run agents with conversational sessions

**Agent Built**: Day Trip Planner that generates budget-aware itineraries

```bash
git checkout part-1-basic-agent
```

---

### 🔜 Part 2: Custom Tools & Agent Teams (Coming Soon)
**Branch**: `part-2-custom-tools`

**What You'll Learn**:
- Create custom function tools (Weather API)
- Build Agent-as-a-Tool hierarchies
- Orchestrate multi-agent systems
- Pass data between agents

---

### 🔜 Part 3: Memory & Sessions (Coming Soon)
**Branch**: `part-3-memory-sessions`

**What You'll Learn**:
- Implement conversational memory
- Manage multi-turn conversations
- Handle user feedback and adaptation
- Build stateful agents

---

### 🔜 More Parts Coming Soon!
Stay tuned for additional lessons covering:
- Structured outputs
- Persistent storage
- Callbacks and monitoring
- Sequential and parallel agent patterns

---

## 🚀 Quick Start

### 1. **Clone the Repository**
```bash
git clone https://github.com/Eli-Keli/adk-crash-course.git
cd adk-crash-course
```

### 2. **Choose Your Lesson**
```bash
# Start with Part 1
git checkout part-1-basic-agent

# Or jump to any other part
git checkout part-2-custom-tools
```

### 3. **Follow the Instructions**
Each branch contains:
- Complete, runnable code
- Detailed `instructions.md` or README
- Setup guide specific to that lesson

---

## 📖 Learning Resources

- 📘 **Official Codelab**: https://codelabs.developers.google.com/onramp/instructions
- 📗 **ADK Documentation**: https://google.github.io/adk-docs/get-started/python/
- 🔑 **Get Your API Key**: https://aistudio.google.com/apikey
- 📓 **Companion Notebook**: Available in the main course materials

---

## 🎓 Prerequisites

Before starting, make sure you have:

- ✅ **Python 3.10+** installed
- ✅ **Google API Key** (free from AI Studio)
- ✅ Basic knowledge of Python
- ✅ Familiarity with async/await (helpful but not required)

---

## Repository Structure

This main branch contains only this navigation guide. Each learning branch has its own structure:

```
part-1-basic-agent/
├── day_trip_agent/
│   ├── agent.py          # Complete working example
│   ├── instructions.md   # Detailed setup & explanations
│   ├── .env              # Your API key (gitignored)
│   └── __init__.py
├── .gitignore
└── README.md             # (optional branch-specific readme)
```

---

## 💡 How to Use This Repository

**For Learners**:
1. Start with `part-1-basic-agent`
2. Complete each lesson before moving to the next
3. Experiment with the code - modify queries, add features
4. Check out the next branch when ready

**For Instructors**:
- Each branch is self-contained and can be used independently
- Students can fork and work on their own pace
- Issues and PRs welcome for improvements!

---

## 🤝 Contributing

Found a bug or want to improve the examples? Contributions are welcome!

1. Fork the repository
2. Create a feature branch
3. Make your improvements
4. Submit a pull request

---

## 📄 License

MIT License - Feel free to use this for learning and experimentation.

---

## 🎯 Next Steps

**Ready to start?** Checkout the first lesson:

```bash
git checkout part-1-basic-agent
```

Then follow the instructions in that branch to build your first AI agent!

---

## Questions or Feedback?

- Open an issue on GitHub
- Check the official ADK documentation
- Review the codelab materials

---

**Happy Learning! 🚀 Let's build amazing AI agents together!**
