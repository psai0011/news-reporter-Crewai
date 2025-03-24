# 📰 News Reporter CrewAI

> *Transform research into compelling tech stories with AI*

## ✨ Overview

News Reporter CrewAI creates professionally written technology articles through an intelligent collaboration between AI research and writing agents, powered by Google's Gemini model.

## 🚀 Features

* 🔍 **AI Research** - Uncovers emerging tech trends and developments
* ✍️ **Smart Writing** - Crafts engaging, accessible narratives
* 🎯 **Topic Flexibility** - Easily customize your focus areas
* 🔄 **Seamless Workflow** - Research flows naturally into polished content
* 📄 **Markdown Ready** - Articles delivered in clean, publishable format

## 📋 Requirements

* Python 3.9+
* Google API Key
* SERPER API Key (optional)

## 🛠️ Quick Setup

```bash
# Install dependencies
pip install crewai langchain-google-genai python-dotenv

# Create .env file with your keys
echo 'GOOGLE_API_KEY="your_key_here"' > .env
echo 'SERPER_API_KEY="your_key_here"' >> .env

# Update agent.py for secure API usage
# Replace hardcoded key with: google_api_key=os.getenv("GOOGLE_API_KEY")

# Run the application
python crew.py
```

## 📂 Project Structure

```
news-reporter-crewai/
├── agent.py    # Research & Writer agents
├── crew.py     # Workflow orchestration
├── tasks.py    # Task definitions
├── tools.py    # Agent capabilities
└── .env        # API configuration
```

## 🎛️ Customization

```python
# Change your topic in crew.py
result = crew.kickoff({'topic': "Quantum Computing"})
```

## 🔎 Need Help?

* Check API keys in `.env` for authentication errors
* Ensure all packages are properly installed
* Implement required methods in `tools.py`
