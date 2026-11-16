"""Backend configuration: values never sent to the browser."""
import json, os, urllib.request
from pathlib import Path
ROOT=Path(__file__).resolve().parent
def load_env():
    f=ROOT/'.env'
    if f.exists():
        for line in f.read_text().splitlines():
            if line.strip() and not line.lstrip().startswith('#') and '=' in line:
                k,v=line.split('=',1)
                os.environ.setdefault(k.strip(),v.strip())
load_env()
def request_json(url, payload=None, timeout=600):
    data=None if payload is None else json.dumps(payload).encode()
    req=urllib.request.Request(url,data=data,headers={'Content-Type':'application/json','Authorization':'Bearer '+os.getenv('MODEL_API_KEY','ollama')})
    with urllib.request.urlopen(req,timeout=timeout) as r:return json.load(r)
def native():return os.getenv('OLLAMA_URL','http://127.0.0.1:11435').rstrip('/')
def chat(prompt, system='Answer accurately using only the supplied data.'):
    j=request_json(os.getenv('MODEL_BASE_URL','http://127.0.0.1:11435/v1').rstrip('/')+'/chat/completions',{
      'model':os.getenv('MODEL_NAME','qwen3:4b'),'messages':[{'role':'system','content':system},{'role':'user','content':prompt+'\n/no_think'}],
      'temperature':0,'reasoning_effort':'none','max_tokens':1536,'stream':False})
    choice=j['choices'][0]
    answer=(choice['message'].get('content') or '').strip()
    if '</think>' in answer:answer=answer.rsplit('</think>',1)[1].strip()
    if '<think>' in answer:answer=''
    if not answer or choice.get('finish_reason')=='length':
        raise RuntimeError('No complete final answer from Ollama; finish_reason='+str(choice.get('finish_reason')))
    return answer
def embed(texts):
    return request_json(native()+'/api/embed',{'model':os.getenv('EMBED_MODEL','embeddinggemma'),'input':texts,'keep_alive':0})['embeddings']
