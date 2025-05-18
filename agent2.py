import asyncio
from pathlib import Path
from textwrap import dedent

from agno.agent import Agent
from agno.tools.mcp import MCPTools
from agno.models.ollama import Ollama




async def run_agent(message: str) -> None:
    """Run the filesystem agent with the given message."""
    # Initialize the MCP server
    file_path = str(Path(__file__).parent.parent.parent.parent)

    # Create a client session to connect to the MCP server
    async with MCPTools(
        f"python3 server.py"
    ) as mcp_tools:
        agent = Agent(
            model=Ollama(id="qwen2.5-coder:7b-instruct", provider="Ollama"),
            tools=[mcp_tools],
            instructions=dedent("""\
                You are a basic agent. Help users do simple stuff like adding and subtracting. 
            """),
            markdown=True,
            show_tool_calls=True,
        )

        # Run the agent
        await agent.aprint_response(message, stream=True)


# Example usage
if __name__ == "__main__":
    # Basic example - exploring project license
    asyncio.run(
       run_agent('Get me a special number using the mcp server')
    )
    




