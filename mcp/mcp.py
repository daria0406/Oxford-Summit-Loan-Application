class MCPChannel:
    def send(self, name: str, params:dict, message: str = '', metadata: dict = {}):
        raise NotImplementedError("Send method must be implemented by subclasses")
