from dataclasses import dataclass
from typing import Optional, Dict, Any

@dataclass(frozen=True)
class User:
    id: int
    username: Optional[str] = None
    
@dataclass(frozen=True)
class AgentRequest:
    user: User
    quetry: str
    context: Dict[str, Any]
    intent: Optional[str] = None
    
@dataclass(frozen=True)
class AgentResponse:
    text: str
    metadata: Dict[str,Any]