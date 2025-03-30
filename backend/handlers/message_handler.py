from fastapi import APIRouter, Request
from fastapi.responses import JSONResponse

from pydantic import BaseModel

from models.models import RequestTable

import hashlib

from sqlalchemy.orm import Session

import jwt

from utils import runbot


router = APIRouter(prefix="/chat")

class ChatRequest(BaseModel):
    message: str

@router.post("/")
async def chat(request: Request, chat_request: ChatRequest):
    """
    return response for user's chat
    """
    with Session(request.app.state.db) as session:
        
        # 2. call chatbot
        #chat_response = "Hi hi hi hi hi hi!"
        chat_response, emissions_val = runbot.frontend_chat(chat_request.message)

        # 1. add user message to db
        # 3. add chatbot message to db
        request = RequestTable(
            usr_message=chat_request.message,
            chat_response=chat_response,
            emissions=emissions_val
        )
        session.add(request)
        session.commit()
        # 4. return chatbot msg
        return JSONResponse(
            status_code=200,
            content={"chat_response": chat_response,"emissions": emissions_val, }
        )



    
    

    



    user_message = session.query(Request).last()
    message_response = "Hi hi hi hi hi hi!"

    return JSONResponse(
        status_code=200,
        content={"message": message_response}
    )


class RegisterRequest(BaseModel):
    message: str

@router.post("/register")
async def register(request: Request, register_request: RegisterRequest):
    """
    Register a new message
    """ 
    # Create a new message
    with Session(request.app.state.db) as session:
        request = Request(
            message=register_request.message,
        )
        session.add(request)
        session.commit()
    
    return JSONResponse(
        status_code=200,
        content={"message": "Message registered successfully"}
    )