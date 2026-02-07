from pydantic import BaseModel, Field
from datetime import datetime

class Comm(BaseModel):
    comm_id: str = Field(..., description="The comm_id of the document")
    comm_name: str = Field(..., description="The comm_name of the document")
    comm_type: str = Field(..., description="The comm_type of the document")
    comm_status: str = Field(..., description="The comm_status of the document")
    comm_created_at: datetime = Field(..., description="The comm_created_at of the document")
    comm_updated_at: datetime = Field(..., description="The comm_updated_at of the document")


