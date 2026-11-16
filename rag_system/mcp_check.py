import asyncio,json,os,sys
from fastmcp import Client
from fastmcp.client.transports import StdioTransport
from common import ROOT,native
async def call(query):
    t=StdioTransport(command=sys.executable,args=['-m','rag_system.mcp_server'],cwd=str(ROOT),env={'PYTHONPATH':str(ROOT),'OLLAMA_URL':native(),'EMBED_MODEL':os.getenv('EMBED_MODEL','embeddinggemma'),'ANONYMIZED_TELEMETRY':'false'})
    async with Client(t) as c:
        result=await c.call_tool('search_my_notes',{'query':query,'top_k':3})
        return result.data if hasattr(result,'data') else result.structured_content
if __name__=='__main__':print(json.dumps(asyncio.run(call(' '.join(sys.argv[1:]) or 'studio emergency reference')),indent=2,default=str))
