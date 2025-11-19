from abc import ABC, abstractmethod
from .models import AgentRequest, AgentResponse

class Agent(ABC):
    
    @property
    @abstractmethod
    def name(self) -> str:
        pass
    
    @abstractmethod
    async def run(self, request: AgentResponse) -> AgentResponse:
        pass