from langgraph.prebuilt import create_react_agent

from llm import llm
from tools import (
    search_by_budget,
    search_by_brand,
    search_by_ram,
    search_laptops_by_budget,
)

agent = create_react_agent(
    model=llm,
    tools=[search_laptops_by_budget],
    # tools=[search_by_budget,
    # search_by_brand,
    # search_by_ram],
)
