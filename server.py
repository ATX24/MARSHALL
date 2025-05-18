'''
CUSTOM MCP SERVER
MCP server that is used to run a simple arithmetic operation
Integrates nicely with agno
@atx24 

'''


from mcp.server.fastmcp import FastMCP

mcp = FastMCP("Basic MCP service for arithmetic operations")

@mcp.tool()
def add(a: int, b: int) -> int:
    """Add two numbers."""
    return a + b

@mcp.tool()
def get_special_number() -> int:
    """Get a special number."""
    return 42

if __name__ == "__main__":
    mcp.run()