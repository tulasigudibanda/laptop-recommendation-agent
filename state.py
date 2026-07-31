from typing import Optional, TypedDict


class AgentState(TypedDict):
    brand: str | None
    budget: int | None
    ram: int | None
