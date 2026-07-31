from typing import TypedDict, Optional


class AgentState(TypedDict):
    brand: Optional[str]
    budget: Optional[int]
    ram: Optional[int]
