from datetime import datetime
from pydantic import BaseModel 
from pydantic import ConfigDict 

class create_user(BaseModel):
   
    username: str
    email: str
    password: str

class user_response(BaseModel):
    
    id: int
    username: str
    email: str

    model_config = ConfigDict(from_attributes=True)



class token_response(BaseModel):
    
    access_token: str
    token_type: str 

class product_create(BaseModel):
   
    title: str
    description: str
    owner_id: int
    stutus: str = "activet"

    model_config = ConfigDict(from_attributes=True)

