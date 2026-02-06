from langchain_openai import ChatOpenAI
from langgraph.graph import MessagesState
from langgraph.graph import StateGraph, START, END
from langgraph.prebuilt import ToolNode, tools_condition
import os, getpass

# Tool
def multiply(a: int, b: int) -> int:
    """Multiplies a and b.

    Args:
        a: first int
        b: second int
    """
    return a * b

# LLM with bound tool
# llm = ChatOpenAI(model="gpt-4o")
llm = ChatOpenAI(
    api_key=os.environ["OPENROUTER_API_KEY"],
    base_url="https://openrouter.ai/api/v1",
    # model="openai/gpt-oss-120b:free",   # OpenAI: gpt-oss-120b (free)
                                           # Free Users with $10+ in credits
                                           # - 1,000 requests per day
                                           # - 20 requests per minute
    model="openai/gpt-oss-120b",           # OpenAI: gpt-oss-120b (paid)
                                           # $0.039/M input, $0.19/M output
    temperature=0,
    default_headers={
        "HTTP-Referer": "localhost",  # Optional. Site URL for rankings on openrouter.ai.
        "X-Title": "langchain-academy",  # Optional. Site title for rankings on openrouter.ai.
    },
    extra_body={
        "provider": {
            "sort": "latency",           # prioritize lowest latency providers
            "allow_fallbacks": True,     # fall back to others if unavailable
        }
    }
)
llm_with_tools = llm.bind_tools([multiply])

# Node
def tool_calling_llm(state: MessagesState):
    return {"messages": [llm_with_tools.invoke(state["messages"])]}

# Build graph
builder = StateGraph(MessagesState)
builder.add_node("tool_calling_llm", tool_calling_llm)
builder.add_node("tools", ToolNode([multiply]))
builder.add_edge(START, "tool_calling_llm")
builder.add_conditional_edges(
    "tool_calling_llm",
    # If the latest message (result) from assistant is a tool call -> tools_condition routes to tools
    # If the latest message (result) from assistant is a not a tool call -> tools_condition routes to END
    tools_condition,
)
builder.add_edge("tools", END)

# Compile graph
graph = builder.compile()