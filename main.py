
from dotenv import load_dotenv
from pydantic import BaseModel
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.agents import create_agent
from langchain.agents.structured_output import ToolStrategy
from tools import search_tool,wiki_tool,save_tool

load_dotenv()


class ResearchResponse(BaseModel):
    topic: str
    summary: str
    sources: list[str]
    tools_used: list[str]


llm = ChatGoogleGenerativeAI(
    model="gemini-2.5-flash"
)

tools = [search_tool, wiki_tool, save_tool]

agent = create_agent(
    model=llm,
    tools=tools,
    system_prompt=f"""
    You are a research assistant that generates research summaries.
    Answer the user's query and use the available tools when necessary.
    """,
    response_format=ToolStrategy(ResearchResponse),
)

query = input("What can I help you research? ").strip()

if not query:
    print("Please enter a research question.")
    raise SystemExit(1)

try:
    raw_response = agent.invoke(
        {
            "messages": [
                {"role": "user", "content": query}
            ]
        }
    )

    research_response = raw_response["structured_response"]

    print(research_response.model_dump())

except Exception as e:
    print("Error processing response:", e)
