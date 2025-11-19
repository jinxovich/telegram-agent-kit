from app.domain.models import User, AgentRequest
from app.agents.echo_agent import EchoAgent

def test_echo_agent():
    agent = EchoAgent()
    request = AgentRequest(
        user=User(id=123),
        query='Hello',
        context={}
    )
    response = agent.run(request)
    assert response.text == 'Echo: Hello'