from pydantic import BaseModel,Field
from typing import List, Optional
import requests
class MessageEntity(BaseModel):
    offset: int
    length: int
    type: str

class User(BaseModel):
    id: int
    is_bot: bool
    first_name: str
    username: Optional[str] = None
    language_code: Optional[str] = None

class Chat(BaseModel):
    id: int
    first_name: Optional[str] = None
    username: Optional[str] = None
    type: str

class Message(BaseModel):
    message_id: int
    from_: User=Field(..., alias="from")
    chat: Chat
    date: int
    text: Optional[str] = None
    entities: Optional[List[MessageEntity]] = None

class Update(BaseModel):
    update_id: int
    message: Optional[Message] = None

class TelegramResponse(BaseModel):
    ok: bool = False
    result: Update
def getupdate():
    res=requests.get("https://api.telegram.org/bot6640559959:AAElVoUIZZ-TBXUFpHgG2e7hVNmz33qsQnc/getUpdates")
    updates=res.json()
    updates["result"]=updates["result"][0]
    return TelegramResponse.parse_obj(updates)
def sendMessage(text):
    res=requests.post("https://api.telegram.org/bot6640559959:AAElVoUIZZ-TBXUFpHgG2e7hVNmz33qsQnc/sendMessage",params={"chat_id":1687012335,"text":text})
