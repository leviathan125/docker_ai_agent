from typing import List
from fastapi import APIRouter, Depends
from sqlmodel import Session, select

from api.db import get_session
from .models import ChatMessage, ChatMessagePayload, ChatMessageListItem
router = APIRouter()

# /backend/src/api/chat/routing.py
# curl -X POST -d '{"message": "Hello, World!"}' -H "Content-Type: application/json" http://localhost:8080/api/chats/
@router.get("/")
def chat_health():
    return {"status": "healthy"}

# api endpoint
# /api/chats/recent/
@router.get("/recent/", response_model=List[ChatMessageListItem])
def chat_list_messages(session: Session = Depends(get_session)):
    query = select(ChatMessage) # sql -> query
    results = session.exec(query).fetchall()[:10]
    return results

@router.post("/", response_model=ChatMessageListItem)
def chat_create_message(
        payload: ChatMessagePayload,
        session: Session = Depends(get_session)
    ):
    data = payload.model_dump() # pydantic model to dict
    obj = ChatMessage.model_validate(data)
    session.add(obj)
    session.commit()
    session.refresh(obj) # ensure id/primary key added to the obj instance
    # ready to store in the database
    return obj