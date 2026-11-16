"""Stdio only. Never publish an unauthenticated MCP HTTP port."""
from fastmcp import FastMCP
from rag_system.rag_common import search
mcp=FastMCP('Parker Notes')
@mcp.tool
def search_my_notes(query:str,top_k:int=6)->list[dict]:
    """Search fictional private notes, returning citation, source, page and text. No actions."""
    return search(query,max(1,min(top_k,6)))
if __name__=='__main__':mcp.run()
