from langchain_openai import ChatOpenAI
from langchain_community.tools.tavily_search import TavilySearchResults
from langchain_core.prompts import ChatPromptTemplate
from langchain.agents import AgentExecutor, create_tool_calling_agent
import os

os.environ["OPENAI_API_KEY"] = os.getenv("OPENAI_API_KEY")
os.environ["TAVILY_API_KEY"] = os.getenv("TAVILY_API_KEY")

model = ChatOpenAI(model_name="gpt-3.5-turbo")

searchtool = TavilySearchResults(max_results=3)
tools = [searchtool]

prompt = ChatPromptTemplate.from_messages(
    [
        ("system", "You are a helpful assistant. Make sure to invoke tavily_search_results_json."),
        ("human", "{input}"),
        ("placeholder", "{agent_scratchpad}"),
    ]
)

agent = create_tool_calling_agent(model, tools, prompt)
agent_executor = AgentExecutor(agent=agent, tools=tools, verbose=True, stream_runnable=False)
agent_executor.invoke({"input": "Who won the UEFA European Football Championship in 2024?"})
