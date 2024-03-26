from typing import TypedDict, Optional, Any


class ProviderOptions(TypedDict):
    id: Optional[str]
    config: Optional[dict[str, Any]]


class CallApiContextParams(TypedDict):
    vars: dict[str, Any]


class TokenUsage(TypedDict):
    total: int
    prompt: int
    completion: int


class ProviderResponse(TypedDict):
    output: Optional[str]
    error: Optional[str]
    tokenUsage: Optional[TokenUsage]
    cost: Optional[float]
    cached: Optional[bool]
    logProbs: Optional[list[float]]
