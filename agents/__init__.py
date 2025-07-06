from typing import TypeVar, Generic, Callable, Any, List, Optional
from dataclasses import dataclass
from functools import wraps
import asyncio
from openai import AsyncOpenAI
import os

# Type variable for context
T = TypeVar('T')

@dataclass
class ModelSettings:
    tool_choice: str = "auto"
    temperature: float = 0.0
    max_tokens: Optional[int] = None

class RunContextWrapper(Generic[T]):
    def __init__(self, context: T):
        self.context = context

def function_tool(strict_mode: bool = True):
    """Decorator to mark a function as a tool"""
    def decorator(func: Callable) -> Callable:
        @wraps(func)
        def wrapped(*args, **kwargs):
            # For direct function calls, just execute the function normally
            return func(*args, **kwargs)
        wrapped._is_tool = True
        wrapped._strict_mode = strict_mode
        wrapped._original_func = func  # Store the original function
        return wrapped
    return decorator

class Agent(Generic[T]):
    def __init__(
        self,
        name: str,
        instructions: str,
        model: str = "gpt-4-0613",
        tools: List[Callable] = None,
        model_settings: ModelSettings = None,
        output_type: type = str,
        mcp_servers: List = None
    ):
        self.name = name
        self.instructions = instructions
        self.model = model
        self.tools = tools or []
        self.model_settings = model_settings or ModelSettings()
        self.output_type = output_type
        self.mcp_servers = mcp_servers or []
        self.client = AsyncOpenAI(api_key=os.getenv("OPENAI_API_KEY"))

    async def run(self, input: str, context: T = None, config: Any = None) -> Any:
        """
        Run the agent using the first available tool and return the result.
        This simulates the behavior of a deterministic function-calling agent.
        """
        wrapper = RunContextWrapper(context) if context else None

        # Execute the first tool in the agent's tool list
        if self.tools:
            tool = self.tools[0]
            if getattr(tool, '_is_tool', False):
                try:
                    result = tool(wrapper, config=config) if wrapper else tool(config=config)
                except Exception as e:
                    result = f"[Error while running tool: {e}]"
            else:
                result = "[Tool is not properly decorated with @function_tool]"
        else:
            result = f"[Agent {self.name} has no tools configured]"

        # Return a compatible mock object with .final_output
        return type('Response', (), {'final_output': result})()