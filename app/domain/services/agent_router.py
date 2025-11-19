from typing import Dict, Optional
from ..agent import Agent
from ..models import AgentRequest

AGENT_REGISTRY: Dict[str, Agent] = {}

def register_agent(agent: Agent) -> None:
    AGENT_REGISTRY[agent.name] = agent
    
def get_agent_by_name(name: str) -> Optional[Agent]:
    return AGENT_REGISTRY.get(name)

def route_by_intent(request: AgentRequest) -> Optional[Agent]:
    if not request.intent:
        return None
    return AGENT_REGISTRY.get(request.intent)
                              