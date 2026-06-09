from pydantic import BaseModel, Field, ConfigDict
from datetime import datetime

class LogCreate(BaseModel):
    client_id : int = Field(ge=1)
    message : str = Field(min_length=1)

class LogRead(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id:int
    client_id:int
    message:str
    created_at:datetime