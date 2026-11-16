import json,sys
from rag_system.rag_common import answer,status
print(json.dumps(status() if sys.argv[1:]==['--status'] else answer(' '.join(sys.argv[1:]) or 'What is the studio emergency reference?'),indent=2))
