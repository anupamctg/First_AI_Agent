from turtledemo.sorting_animate import instructions1
from phi.agent import Agent
from phi.model.groq import Groq
from phi.model.openai import OpenAIChat
from phi.tools.duckduckgo import DuckDuckGo
from phi.tools.yfinance import YFinanceTools
from dotenv import load_dotenv

load_dotenv()

web_agent = Agent(
    name = "Web Agent",
#    model=Groq(id="llama-3.3-70b-versatile"),
    model = OpenAIChat(id="gpt-4o"),
    tools = [DuckDuckGo()],
    instructions = ["Always include sources"],
    show_tool_calls= True,
    markdown= True,
)

stock_agent = Agent(
    name="Stock Agent",
    role= "Get Financial data",
#    model=Groq(id="llama-3.3-70b-versatile"),
    model=OpenAIChat(id="gpt-4o"),
    tools=[YFinanceTools(stock_price=True, analyst_recommendations=True, stock_fundamentals=True)],
    instructions=["Use table to display data"],
    show_tool_calls=True,
    markdown=True,
)

agent_team = Agent(
    model=Groq(id="llama-3.3-70b-versatile"),
    team=[web_agent, stock_agent],
    instructions= ["Always include sources", "Use table to display data"],
    show_tool_calls=True,
    markdown=True,
)

agent_team.print_response("Summarize analyst recommendation and share latest news on MSFT shares",stream=True)