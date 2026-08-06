from typing import Optional, TypedDict


class AgentState(TypedDict):
    brand: Optional[str]
    budget: Optional[int]
    ram: Optional[int]
