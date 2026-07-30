from langgraph.prebuilt import create_react_agent

from llm import llm
from tools import (
    search_by_budget_mock,
    search_by_brand,
    search_by_ram,
    search_laptops_by_budget,
)

agent = create_react_agent(
    model=llm,
    # tools=[search_laptops_by_budget],
    tools=[search_by_budget_mock,
    search_by_brand,
    search_by_ram],
)


def ask_agent(question: str):
    response = agent.invoke(
        {
            "messages": [
                ("user", question)
            ]
        }
    )

    return response["messages"][-1].content