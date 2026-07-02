# LangChain Web Search Agent POC

## Project Overview

This project demonstrates the implementation of an AI-powered LangChain Agent that combines the reasoning capabilities of OpenAI's GPT model with real-time web search using the Tavily Search API.

The solution was developed as a Proof of Concept (POC) to showcase how Large Language Models (LLMs) can dynamically retrieve up-to-date information from the internet and generate accurate responses using external tools.

---

## Business Scenario

Financial services organizations often require access to real-time information that may not be available within an LLM's training data.

This project addresses that challenge by enabling an AI Agent to:

- Access live information from the web
- Retrieve current data using Tavily Search
- Analyze search results using an OpenAI LLM
- Generate accurate responses based on retrieved information

---

## Solution Architecture

```text
User Query
    │
    ▼
Prompt Template
    │
    ▼
LangChain Agent
    │
    ▼
OpenAI GPT Model (LLM)
    │
    ├── Answer Directly
    │
    └── Invoke Tool
            │
            ▼
      Tavily Search API
            │
            ▼
      Search Results
            │
            ▼
      Final Response
```

---

## Technologies Used

- Python
- LangChain
- OpenAI GPT-3.5 Turbo
- Tavily Search API
- Prompt Engineering
- LangChain Agents
- Agent Executor
- Tool Calling

---

## Features

- Real-time web search integration
- OpenAI LLM integration
- Tool-calling agent implementation
- Prompt template design
- Agent reasoning and decision-making
- Current information retrieval

---

## Project Components

### 1. OpenAI Language Model

```python
model = ChatOpenAI(model_name="gpt-3.5-turbo")
```

Provides reasoning, decision-making, and response generation capabilities.

---

### 2. Tavily Search Tool

```python
searchtool = TavilySearchResults(max_results=3)
```

Fetches relevant information from the web.

---

### 3. Prompt Template

```python
prompt = ChatPromptTemplate.from_messages(
    [
        ("system", "You are a helpful assistant. Make sure to invoke tavily_search_results_json."),
        ("human", "{input}"),
        ("placeholder", "{agent_scratchpad}"),
    ]
)
```

Defines the interaction pattern between the user, LLM, and tools.

---

### 4. LangChain Agent

```python
agent = create_tool_calling_agent(
    model,
    tools,
    prompt
)
```

Combines the LLM, prompt, and tools into a tool-calling AI Agent.

---

## Example Question

```text
Who won the UEFA European Football Championship in 2024?
```

### Agent Execution

1. Receives user question
2. Determines whether external information is needed
3. Invokes Tavily Search Tool
4. Retrieves information from the web
5. Uses GPT model to analyze results
6. Returns final answer

### Sample Response

```text
Spain won the UEFA European Football Championship in 2024. They defeated England in the final with a score of 2-1.
```

---

## Skills Demonstrated

- Generative AI
- Agentic AI
- Prompt Engineering
- LLM Integration
- LangChain Framework
- Tool Calling
- Retrieval Augmented Search
- AI Application Development

---

## Future Enhancements

Planned improvements include:

- Streamlit-based web interface
- Financial market data integration
- Multi-tool agents
- LangGraph implementation
- Multi-agent workflows
- Conversation memory
- RAG-based document retrieval

---

## Repository Structure

```text
LangChain-WebSearch-Agent-Poc/
│
├── README.md
├── app.py
├── requirements.txt
└── screenshots/
```

---

## Learning Outcomes

This project helped develop practical experience in:

- LangChain Agents
- Prompt Templates
- Tavily Search API
- OpenAI Integration
- AI Agent Development
- Tool-Oriented LLM Applications

---

## Author

Sandeep Kumar

Senior Consultant | Generative AI Enthusiast

GitHub: https://github.com/321sandeepkumar123
