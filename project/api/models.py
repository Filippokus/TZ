from pydantic import BaseModel
from typing import Optional
from datetime import datetime

class MessageModel(BaseModel):
    username: str
    text: str
    timestamp: Optional[datetime] = None
