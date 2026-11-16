# Parker teaching tools

A small document connector that lets an assistant find cited passages in fictional studio notes and a sample policy. This is a reviewed source-only extract of a reconstructed tutorial project, not the missing original course source.

## What is included

- A stdio MCP tool, `search_my_notes`, returning text with filename/page citations.
- A Chroma document-search implementation and command-line indexing/query helpers.
- Newly authored fictional notes and a three-page sample PDF. No real customer or insurance data.
- Generic configuration examples. No deployment credentials, existing database, private manual or operational backups.

The companion [fictional evaluation examples](https://huggingface.co/datasets/ParkerPrompt/parker-reconstructed-eval) contain three smoke-test cases, not a performance benchmark.

## Use with your existing server

Use an existing private Ollama service with a chat model and the `embeddinggemma` embedding model already available. No model weights are bundled, and this tutorial does not require downloading a model to your Mac.

Create an isolated Python environment on the intended machine and install `requirements-rag.txt`. Copy `.env.example` to a local `.env` and set the endpoints for your own environment. Keep that file private. Then, from this repository root:

```sh
python -m rag_system.ingest
python -m rag_system.mcp_check 'studio emergency reference'
python -m rag_system.ask 'What is the fictional excess?'
```

The first command creates a NEW local index. It refuses to overwrite an existing manifest; do not use it to replace an index you need to preserve. The notes contain the fictional reference ORCHID-472 and a fictional $750 excess.

For an MCP client, launch `python -m rag_system.mcp_server` from this directory over stdio. Do not publish an unauthenticated HTTP MCP endpoint.

## Evidence and limits

The corresponding existing server produced cited search results from the sample PDF and notes during recording. That demonstrates retrieval, not guaranteed answer accuracy or protection against all prompt injection. The source snapshot passes Python syntax checks; this extracted package has not been installed and retested as a new standalone deployment. Dependencies and their licences remain their own.

This subset does not contain FinTrack, CrewAI, n8n, Telegram delivery, a trained adapter or a full server restore. Those are separate demonstrations; they are not implied by this connector.

## Licence

MIT for the newly authored code and fictional fixtures; see LICENSE. Third-party packages retain their own licences. No model weights are redistributed.
