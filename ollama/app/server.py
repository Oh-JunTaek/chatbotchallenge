from fastapi import FastAPI, Request
from fastapi.responses import RedirectResponse
from fastapi.middleware.cors import CORSMiddleware
from typing import List, Union
from langserve.pydantic_v1 import BaseModel, Field
from langchain_core.messages import HumanMessage, AIMessage, SystemMessage
from langserve import add_routes
from chain import chain
from chat import chain as chat_chain
from translator import chain as EN_TO_KO_chain
from llm import llm as model
from xionic import chain as xionic_chain
import asyncio
import httpx
import logging

app = FastAPI()

# 모든 CORS 허용 설정
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
    expose_headers=["*"],
)

@app.get("/")
async def redirect_root_to_docs():
    return RedirectResponse("/xionic/playground")

add_routes(app, chain, path="/prompt")

class InputChat(BaseModel):
    """채팅 엔드포인트의 입력 데이터 형식"""

    messages: List[Union[HumanMessage, AIMessage, SystemMessage]] = Field(
        ...,
        description="현재 대화를 나타내는 채팅 메시지들입니다.",
    )

add_routes(
    app,
    chat_chain.with_types(input_type=InputChat),
    path="/chat",
    enable_feedback_endpoint=True,
    enable_public_trace_link_endpoint=True,
    playground_type="chat",
)

add_routes(app, EN_TO_KO_chain, path="/translate")
add_routes(app, model, path="/llm")
add_routes(
    app,
    xionic_chain.with_types(input_type=InputChat),
    path="/xionic",
    enable_feedback_endpoint=True,
    enable_public_trace_link_endpoint=True,
    playground_type="chat",
)

@app.get("/some_endpoint")
async def some_endpoint():
    try:
        # 비동기 API 호출 예제
        async with httpx.AsyncClient() as client:
            response = await client.get('https://api.example.com/data')
            data = response.json()
        return {"data": data}
    except asyncio.CancelledError as e:
        logging.error(f"Request was cancelled: {e}")
        return {"error": "Request was cancelled"}
    except httpx.RemoteProtocolError as e:
        logging.error(f"Remote protocol error: {e}")
        return {"error": "Remote protocol error"}
    except Exception as e:
        logging.error(f"An error occurred: {e}")
        return {"error": "An unexpected error occurred"}

if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=8000, timeout_keep_alive=120, http2=True)
