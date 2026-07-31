from langgraph.prebuilt import create_react_agent

from llm import llm
from tools import (
    search_by_brand,
    search_by_budget_mock,
    search_by_ram,
)

agent = create_react_agent(
    model=llm,
    tools=[
        search_by_budget_mock,
        search_by_brand,
        search_by_ram,
    ],
)

# hoping the LLM to remember to chat history by appending all the messages and sending it to LLM
# def ask_agent(messages, brand=None):

#     graph_messages = []

#     for message in messages:
#         graph_messages.append(
#             (
#                 message["role"],
#                 message["content"]
#             )
#         )

#     response = agent.invoke(
#         {
#             "messages": graph_messages
#         }
#     )

#     return response["messages"][-1].content

# maintaining with langGraph state and send it to LLM as system prompt along with user prompt and (chat)assisstant promt
# instead hoping the LLM to remember to chat history. With this the model no longer has to infer the preference from the earlier chat.
# Everey request begins something like this: (send state in the systemPrompt so llm directly reads it without the need to infer)
# System:

# Brand: Lenovo
# Budget: None
# RAM: None

# Always honor these preferences.
from memory import agent_state


def ask_agent(messages):

    last_message = messages[-1]["content"].lower()

    if "lenovo" in last_message:
        agent_state["brand"] = "Lenovo"

    elif "dell" in last_message:
        agent_state["brand"] = "Dell"

    graph_messages = [(m["role"], m["content"]) for m in messages]

    system_prompt = f"""
User preferences

Brand: {agent_state["brand"]}
Budget: {agent_state["budget"]}
RAM: {agent_state["ram"]}

Always honor these preferences.
"""

    graph_messages.insert(0, ("system", system_prompt))

    response = agent.invoke({"messages": graph_messages})

    return response["messages"][-1].content


# Next improvement is to replace prebuilt create_react_agent with real LangGraph stateGraph
# replace :
# agent = create_react_agent(...)
# with and create nodes :
# builder = StateGraph(AgentState)
# Each node receives and updates the shared AgentState
# If we jump directly to a custom StateGraph, you'll need to learn several new LangGraph concepts at once: nodes, edges, state reducers, and message handling.
# By first introducing a typed state object and moving business logic out of Streamlit, you'll already have the architecture in the right place.
# Then, converting to a StateGraph becomes mostly a matter of replacing the orchestration mechanism rather than redesigning the whole application.
