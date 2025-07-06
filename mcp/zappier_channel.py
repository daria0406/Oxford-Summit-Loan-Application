import requests
from typing import Optional
from mcp.mcp import MCPChannel

class ZapierChannel(MCPChannel):
    def __init__(self, webhook_url: str):
        self.webhook_url = webhook_url

    def send(self, message: str, metadata: Optional[dict]=None):
        data = {"message": message, "metadata": metadata or {}}
        requests.post(self.webhook_url, json=data)