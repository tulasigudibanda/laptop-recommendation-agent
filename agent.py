from langgraph.prebuilt import create_react_agent

from llm import llm
from tools import (
    search_by_budget_mock,
    search_by_brand,
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


def ask_agent(messages, brand=None):

    graph_messages = []

    for message in messages:
        graph_messages.append(
            (
                message["role"],
                message["content"]
            )
        )

    response = agent.invoke(
        {
            "messages": graph_messages
        }
    )

    return response["messages"][-1].content