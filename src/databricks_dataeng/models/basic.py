from pydantic import BaseModel, Field
from datetime import datetime

class Basic(BaseModel):
    id: str = Field(..., description="The id of the document")
    name: str = Field(..., description="The name of the document")
    age: int = Field(..., description="The age of the document")
    email: str = Field(..., description="The email of the document")
    created_at: datetime = Field(..., description="The created_at of the document")
    updated_at: datetime = Field(..., description="The updated_at of the document")

